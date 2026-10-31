
from pathlib import Path

from afrm.csv_handler import load_flights
from afrm.fuel_model import (
    calculate_fuel,
    calculate_endurance,
    calculate_range
)
from afrm.fuel_status import assess_fuel_status


def main():
    print("Aircraft Fuel and Range Management")
    print("----------------------------------")

    data_file = (
        Path(__file__).resolve().parent
        / "data"
        / "simulated_flights.csv"
    )

    try:
        flights = load_flights(data_file)
    except (OSError, ValueError) as error:
        print(f"Unable to load flight data: {error}")
        return

    status_counts = {
        "NORMAL": 0,
        "CAUTION": 0,
        "CRITICAL": 0
    }

    for flight in flights:
        fuel_used, remaining_fuel = calculate_fuel(flight)
        endurance = calculate_endurance(flight)
        estimated_range = calculate_range(flight)
        status = assess_fuel_status(flight)

        status_counts[status] += 1

        print(f"\nFlight: {flight.flight_id}")
        print(f"Fuel consumed: {fuel_used:.2f} kg")
        print(f"Remaining fuel: {remaining_fuel:.2f} kg")
        print(f"Total endurance: {endurance:.2f} hours")
        print(f"Theoretical range: {estimated_range:.2f} km")
        print(f"Fuel status: {status}")

    print("\n========== FLIGHT SUMMARY ==========")
    print(f"Total flights: {len(flights)}")
    print(f"Normal: {status_counts['NORMAL']}")
    print(f"Caution: {status_counts['CAUTION']}")
    print(f"Critical: {status_counts['CRITICAL']}")


if __name__ == "__main__":
    main()
