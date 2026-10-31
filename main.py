
from afrm.fuel_model import (
    FlightData,
    calculate_fuel,
    calculate_endurance,
    calculate_range
)
from afrm.fuel_status import assess_fuel_status


def main():
    # Example simulated flight
    flight = FlightData(
        flight_id="AFRM001",
        initial_fuel=5000,
        burn_rate=800,
        flight_duration=3,
        ground_speed=750,
        reserve_fuel=1000
    )

    fuel_used, remaining_fuel = calculate_fuel(flight)
    endurance = calculate_endurance(flight)
    estimated_range = calculate_range(flight)
    status = assess_fuel_status(flight)

    print("Aircraft Fuel and Range Management")
    print("----------------------------------")
    print(f"Flight ID: {flight.flight_id}")
    print(f"Initial fuel: {flight.initial_fuel:.2f} kg")
    print(f"Fuel consumed: {fuel_used:.2f} kg")
    print(f"Remaining fuel: {remaining_fuel:.2f} kg")
    print(f"Total endurance: {endurance:.2f} hours")
    print(f"Theoretical range: {estimated_range:.2f} km")
    print(f"Fuel status: {status}")


if __name__ == "__main__":
    main()
