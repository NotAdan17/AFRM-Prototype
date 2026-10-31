
from afrm.fuel_model import calculate_fuel


def assess_fuel_status(flight):
    """Assess predicted fuel against the required reserve."""

    _, remaining_fuel = calculate_fuel(flight)

    if remaining_fuel < 0:
        return "CRITICAL"

    if remaining_fuel < flight.reserve_fuel:
        return "CRITICAL"

    if remaining_fuel <= flight.reserve_fuel * 1.2:
        return "CAUTION"

    return "NORMAL"
