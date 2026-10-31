
import statistics
import time
import tracemalloc
from pathlib import Path

from afrm.csv_handler import load_flights
from afrm.fuel_model import (
    calculate_fuel,
    calculate_endurance,
    calculate_range
)
from afrm.fuel_status import assess_fuel_status


def process_flights(flights):
    """Process every flight without printing results."""

    results = []

    for flight in flights:
        used, remaining = calculate_fuel(flight)

        results.append({
            "flight_id": flight.flight_id,
            "fuel_used": used,
            "remaining_fuel": remaining,
            "endurance": calculate_endurance(flight),
            "range": calculate_range(flight),
            "status": assess_fuel_status(flight)
        })

    return results


def main():
    data_file = (
        Path(__file__).resolve().parent
        / "data"
        / "simulated_flights.csv"
    )

    flights = load_flights(data_file)

    repetitions = 100
    timings = []

    # Warm-up run
    process_flights(flights)

    tracemalloc.start()

    for _ in range(repetitions):
        start = time.perf_counter()
        results = process_flights(flights)
        elapsed = time.perf_counter() - start

        timings.append(elapsed)

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("AFRM Performance Evaluation")
    print("---------------------------")
    print(f"Flights per run: {len(flights)}")
    print(f"Repetitions: {repetitions}")
    print(f"Total flight evaluations: {len(flights) * repetitions}")
    print(f"Average processing time: {statistics.mean(timings) * 1000:.4f} ms")
    print(f"Median processing time: {statistics.median(timings) * 1000:.4f} ms")
    print(f"Minimum processing time: {min(timings) * 1000:.4f} ms")
    print(f"Maximum processing time: {max(timings) * 1000:.4f} ms")
    print(f"Peak traced memory: {peak_memory / 1024:.2f} KiB")
    print(f"Current traced memory: {current_memory / 1024:.2f} KiB")
    print(f"Results in final run: {len(results)}")


if __name__ == "__main__":
    main()
