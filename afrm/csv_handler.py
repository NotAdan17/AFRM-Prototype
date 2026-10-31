
import csv

from afrm.fuel_model import FlightData


def load_flights(file_path):
    """Read and validate simulated flights from a CSV file."""

    flights = []

    required_columns = [
        "flight_id",
        "initial_fuel",
        "burn_rate",
        "flight_duration",
        "ground_speed",
        "reserve_fuel"
    ]

    with open(file_path, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty")

        if not all(
            column in reader.fieldnames
            for column in required_columns
        ):
            raise ValueError("CSV file has missing columns")

        for row_number, row in enumerate(reader, start=2):
            try:
                flight = FlightData(
                    flight_id=row["flight_id"],
                    initial_fuel=float(row["initial_fuel"]),
                    burn_rate=float(row["burn_rate"]),
                    flight_duration=float(row["flight_duration"]),
                    ground_speed=float(row["ground_speed"]),
                    reserve_fuel=float(row["reserve_fuel"])
                )

                flight.validate()
                flights.append(flight)

            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(
                    f"Invalid flight data on row {row_number}: {error}"
                ) from error

    return flights
