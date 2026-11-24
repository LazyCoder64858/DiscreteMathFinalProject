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

from plots import plot_memberships, plot_surface
from fuzzy_system import FuzzyTrafficLight;

# Get inputs
d = float(input("Traffic density (0-60 cars/min): "))
w = float(input("Waiting time (0-120 s): "))

fuzzy_light = FuzzyTrafficLight()

# Print green light duration to 1dp
print(f"Green light duration: {fuzzy_light.compute(d, w):.1f} seconds")

plot_memberships();
plot_surface();