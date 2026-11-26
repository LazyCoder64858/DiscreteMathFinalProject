"""
## Input and output processing
Each user input is converted to a floating-point value and clipped to the limits of its universe
before it is evaluated. Density is restricted to 0 through 60 cars/min, while waiting time is
restricted to 0 through 120 seconds. The result is also constrained by the green-light
universe of 10 through 60 seconds. Clipping prevents values outside the modeled range from
producing invalid or undefined system output.

The resulting value represents a recommended green-light duration. It is a continuous estimate,
not a direct lookup result: overlapping membership functions, all applicable rules, and
aggregation determine the final duration. This makes the system useful for gradual changes in
traffic conditions, rather than only for exact categories.
"""

from plots import plot_memberships;
from fuzzy_system import FuzzyTrafficLight, DENSITY_MAX, WAIT_MAX;

# Get inputs
d = float(input("Traffic density (0-60 cars/min): "))
w = float(input("Waiting time (0-120 s): "))

if d > DENSITY_MAX:
	print("[WARNING] Traffic density is greater than 120, so it has been clamped to 120")

if d < 0:
	print("[WARNING] Traffic density is less than 0, so it has been clamped to 0")

if w > WAIT_MAX:
	print("[WARNING] Wait Time is greater than 60, so it has been clamped to 60")

if w < 0:
	print("[WARNING] Wait Time is less than 0, so it has been clamped to 0")

fuzzy_light = FuzzyTrafficLight()

# Print green light duration to 1dp
print(f"\nGreen light duration: {fuzzy_light.compute(d, w):.1f} seconds")

plot_memberships();
