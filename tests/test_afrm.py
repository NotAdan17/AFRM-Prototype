
import csv
import tempfile
import unittest
from pathlib import Path

from afrm.fuel_model import (
    FlightData,
    calculate_fuel,
    calculate_endurance,
    calculate_range
)
from afrm.fuel_status import assess_fuel_status
from afrm.csv_handler import load_flights


class TestAFRM(unittest.TestCase):

    def setUp(self):
        self.flight = FlightData(
            flight_id="TEST001",
            initial_fuel=5000,
            burn_rate=800,
            flight_duration=3,
            ground_speed=750,
            reserve_fuel=1000
        )

    def test_fuel_consumption(self):
        used, remaining = calculate_fuel(self.flight)
        self.assertAlmostEqual(used, 2400)
        self.assertAlmostEqual(remaining, 2600)

    def test_endurance(self):
        self.assertAlmostEqual(
            calculate_endurance(self.flight), 6.25
        )

    def test_range(self):
        self.assertAlmostEqual(
            calculate_range(self.flight), 4687.5
        )

    def test_normal_status(self):
        self.assertEqual(
            assess_fuel_status(self.flight), "NORMAL"
        )

    def test_caution_status(self):
        self.flight.initial_fuel = 3500
        self.assertEqual(
            assess_fuel_status(self.flight), "CAUTION"
        )

    def test_critical_status(self):
        self.flight.initial_fuel = 3000
        self.assertEqual(
            assess_fuel_status(self.flight), "CRITICAL"
        )

    def test_exact_reserve_boundary(self):
        self.flight.initial_fuel = 3400
        self.assertEqual(
            assess_fuel_status(self.flight), "CAUTION"
        )

    def test_upper_caution_boundary(self):
        self.flight.initial_fuel = 3600
        self.assertEqual(
            assess_fuel_status(self.flight), "CAUTION"
        )

    def test_zero_fuel(self):
        self.flight.initial_fuel = 0
        used, remaining = calculate_fuel(self.flight)
        self.assertEqual(used, 2400)
        self.assertEqual(remaining, -2400)
        self.assertEqual(
            assess_fuel_status(self.flight), "CRITICAL"
        )

    def test_negative_fuel_rejected(self):
        self.flight.initial_fuel = -100
        with self.assertRaises(ValueError):
            calculate_fuel(self.flight)

    def test_zero_burn_rate_rejected(self):
        self.flight.burn_rate = 0
        with self.assertRaises(ValueError):
            calculate_endurance(self.flight)

    def test_negative_duration_rejected(self):
        self.flight.flight_duration = -2
        with self.assertRaises(ValueError):
            calculate_fuel(self.flight)

    def test_invalid_speed_rejected(self):
        self.flight.ground_speed = 0
        with self.assertRaises(ValueError):
            calculate_range(self.flight)

    def test_non_finite_value_rejected(self):
        self.flight.initial_fuel = float("nan")
        with self.assertRaises(ValueError):
            calculate_fuel(self.flight)

    def test_simulated_dataset(self):
        data_file = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "simulated_flights.csv"
        )

        flights = load_flights(data_file)

        self.assertEqual(len(flights), 100)
        self.assertEqual(
            len({flight.flight_id for flight in flights}),
            100
        )

        for flight in flights:
            flight.validate()
            status = assess_fuel_status(flight)
            self.assertIn(
                status, ("NORMAL", "CAUTION", "CRITICAL")
            )

    def test_invalid_csv_row_rejected(self):
        columns = [
            "flight_id", "initial_fuel", "burn_rate",
            "flight_duration", "ground_speed", "reserve_fuel"
        ]

        with tempfile.TemporaryDirectory() as folder:
            file_path = Path(folder) / "invalid.csv"

            with open(
                file_path, "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.writer(file)
                writer.writerow(columns)
                writer.writerow([
                    "BAD001", "invalid", 800, 3, 750, 1000
                ])

            with self.assertRaises(ValueError):
                load_flights(file_path)


if __name__ == "__main__":
    unittest.main()
