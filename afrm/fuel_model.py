
from dataclasses import dataclass
import math


@dataclass
class FlightData:
    """Stores the fuel and flight parameters for one flight."""

    flight_id: str
    initial_fuel: float       # kg
    burn_rate: float          # kg per hour
    flight_duration: float    # hours
    ground_speed: float       # km per hour
    reserve_fuel: float       # kg

    def validate(self):
        """Check that the flight parameters are valid."""

        if not self.flight_id.strip():
            raise ValueError("Flight ID cannot be empty")

        values = [
            self.initial_fuel,
            self.burn_rate,
            self.flight_duration,
            self.ground_speed,
            self.reserve_fuel
        ]

        if any(
            not isinstance(value, (int, float))
            or isinstance(value, bool)
            or not math.isfinite(value)
            for value in values
        ):
            raise ValueError("Fuel and flight values must be finite numbers")

        if self.initial_fuel < 0:
            raise ValueError("Initial fuel cannot be negative")

        if self.burn_rate <= 0:
            raise ValueError("Burn rate must be greater than zero")

        if self.flight_duration < 0:
            raise ValueError("Flight duration cannot be negative")

        if self.ground_speed <= 0:
            raise ValueError("Ground speed must be greater than zero")

        if self.reserve_fuel < 0:
            raise ValueError("Reserve fuel cannot be negative")


def calculate_fuel(flight):
    """Calculate fuel consumption and predicted remaining fuel."""

    flight.validate()

    fuel_used = flight.burn_rate * flight.flight_duration
    remaining_fuel = flight.initial_fuel - fuel_used

    return fuel_used, remaining_fuel


def calculate_endurance(flight):
    """Calculate total endurance from initial fuel."""

    flight.validate()
    return flight.initial_fuel / flight.burn_rate


def calculate_range(flight):
    """Calculate theoretical range using constant ground speed."""

    flight.validate()
    endurance = calculate_endurance(flight)

    return endurance * flight.ground_speed
