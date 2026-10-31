
# Aircraft Fuel and Range Management (AFRM)

## Project Overview

AFRM is a Python-based prototype designed to demonstrate
aircraft fuel-management and flight-planning calculations.

The application processes simulated flight data, estimates
fuel consumption, remaining fuel, endurance and range,
and classifies predicted fuel status.

This is an educational prototype and is not intended
for operational aviation use.

## Development Environment

- Python 3.15.0
- Visual Studio Code
- Git and GitHub
- Windows
- Python virtual environment (venv)

The application uses Python's standard library only.
No external Python packages are required.

## Project Structure

AFRM-Prototype/
- afrm/
  - __init__.py
  - fuel_model.py
  - fuel_status.py
  - csv_handler.py
- data/
  - simulated_flights.csv
- tests/
  - test_afrm.py
- main.py
- performance.py
- README.md
- .gitignore

## Fuel Calculations

Fuel consumed = Burn rate × Flight duration

Remaining fuel = Initial fuel - Fuel consumed

Total endurance = Initial fuel / Burn rate

Theoretical range = Total endurance × Ground speed

Fuel is measured in kilograms, duration in hours,
ground speed in kilometres per hour and range
in kilometres.

## Fuel Status Classification

NORMAL:
Remaining fuel exceeds 120% of the required reserve.

CAUTION:
Remaining fuel is between 100% and 120% of
the required reserve, inclusive.

CRITICAL:
Remaining fuel is below the required reserve.

These thresholds are illustrative simulation criteria,
not certified aviation fuel requirements.

## Simulated Dataset and AI Disclosure

The dataset contains 100 synthetic flights.

AI assistance was used to generate the simulated
flight parameters and varied operating scenarios.

The dataset includes normal, caution, critical
and boundary conditions.

All values are synthetic and do not represent
verified aircraft operational data.

The dataset is retained in CSV format to support
repeatable testing and inspection.

## Running the Application

Create a virtual environment:

    py -m venv .venv

Run the application:

    .\.venv\Scripts\python.exe main.py

## Automated Testing

Run all tests:

    .\.venv\Scripts\python.exe -m unittest discover -s tests -v

The test suite covers fuel calculations, status
classification, threshold boundaries, input
validation and CSV processing.

## Performance Evaluation

Run the benchmark:

    .\.venv\Scripts\python.exe performance.py

The benchmark measures processing time across
100 repetitions and reports traced Python
memory allocations.

Results depend on the execution environment
and do not directly measure energy consumption.

## Design Decisions

Python was selected for its readability, testing
support and suitability for rapid prototyping.

The application separates data validation, fuel
calculations, status assessment and CSV processing
into individual modules.

This structure supports maintainability and
independent verification.

Using standard-library modules avoids unnecessary
third-party dependencies.

## Limitations

- Constant fuel consumption is assumed.
- Ground speed remains constant.
- Weather, altitude and aircraft mass changes
  are not modelled.
- Range and endurance are theoretical estimates
  that do not deduct reserve fuel.
- Negative predicted remaining fuel represents
  a modelled fuel shortfall, not physically
  available fuel.
- Fuel thresholds are simulation assumptions.
- Performance measurements do not demonstrate
  real-time or safety-critical suitability.

## Future Improvements

Potential improvements include variable fuel
consumption, reserve-aware range calculations,
additional aircraft parameters and more extensive
verification.

These changes should be justified against their
additional computational and maintenance costs.
