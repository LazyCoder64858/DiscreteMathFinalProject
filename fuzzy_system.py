"""
This module implements a fuzzy logic system to determine the optimal green light duration at a traffic
intersection based on traffic density and waiting time.

# Universe Definition
A universe is the full range of values a variable can take, stored as a NumPy array.

## Three universes will be created for our study:
	1. Traffic density (input): how congested the intersection is. Measured in cars/min
	2. Waiting time (input): how long cars have been waiting. Measured in seconds
	3. Green Light duration (output): how long the green light should stay on. Measured in seconds

In Ghana major arterial intersections in cities like Accra handle roughly 40,000 to 70,000+ vehicles per 
day (averaging 25 to 75+ vehicles per minute during peak periods). 
[citation](http://www.mlgrd.gov.gh/images/Ghana_Urban_Forum/er.pdf)

For our study, we will assume that:
	- The maximum traffic density is 60 cars/minute,
	- The maximum waiting time is 120 seconds,
	- The green light duration is between 10 and 60 seconds inclusive.

# Membership Functions
Membership functions are used to define fuzzy sets. They map the input values to a degree of membership.

## The membership functions for our fuzzy variables are defined as follows:
    - Traffic density:
        - Low: 0 to 25 cars/min
        - Medium: 15 to 45 cars/min
        - High: 35 to 60 cars/min
    - Waiting time:
        - Short: 0 to 50 seconds
        - Medium: 30 to 90 seconds
        - Long: 70 to 120 seconds
    - Green light duration:
        - Short: 10 to 25 seconds
        - Medium: 20 to 50 seconds
        - Long: 40 to 60 seconds

The membership functions use overlapping fuzzy shapes rather than strict numerical boundaries.
Trapezoidal functions are used for sets that remain fully true across a range, while triangular
functions represent a single preferred value. This overlap allows an input near a boundary to
belong partially to two sets. For example, a traffic density of 40 cars/min has membership in
both the low and medium sets, so it can influence rules associated with both categories.

## Fuzzy rule base
A fuzzy rule has the form:

    IF traffic density is A AND waiting time is B, THEN green light duration is C.

Nine rules compare the three fuzzy levels of each input. Low waiting time generally produces a
short green duration, while longer waiting time and higher traffic density produce longer green
durations. The complete rule table is:

  Rule base:  (density, waiting) -> green duration
                 waiting:  short    medium   long

  density: low             short    short    medium
           medium          short    medium   long
           high            medium   long     long

The AND operation combines the memberships of the two inputs using the minimum value. Rule
outputs are aggregated using the maximum value, and the centroid method defuzzifies the final
membership shape into one numerical green-light duration.
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

DENSITY_MAX = 60                
WAIT_MAX = 120                  
GREEN_MIN, GREEN_MAX = 10, 60   

# --------------------------------------------------------------------------
#   Rule base:  (density, waiting) -> green duration
#
#                  waiting:  short    medium   long
#   density: low             short    short    medium
#            medium          short    medium   long
#            high            medium   long     long
# --------------------------------------------------------------------------
RULE_TABLE = {
    ("low", "short"): "short",    ("low", "medium"): "short",    ("low", "long"): "medium",
    ("medium", "short"): "short", ("medium", "medium"): "medium", ("medium", "long"): "long",
    ("high", "short"): "medium",  ("high", "medium"): "long",    ("high", "long"): "long",
}
class FuzzyTrafficLight:
    def __init__(self):
        # Antecedents (inputs) and consequent (output)
        self.density = ctrl.Antecedent(np.arange(0, DENSITY_MAX + 1, 1), "density")
        self.waiting = ctrl.Antecedent(np.arange(0, WAIT_MAX + 1, 1), "waiting")
        self.green = ctrl.Consequent(np.arange(GREEN_MIN, GREEN_MAX + 1, 1), "green")  
        # Membership functions 
        d, w, g = self.density, self.waiting, self.green
        d["low"] = fuzz.trapmf(d.universe, [0, 0, 10, 25])
        d["medium"] = fuzz.trimf(d.universe, [15, 30, 45])
        d["high"] = fuzz.trapmf(d.universe, [35, 50, DENSITY_MAX, DENSITY_MAX])

        w["short"] = fuzz.trapmf(w.universe, [0, 0, 20, 50])
        w["medium"] = fuzz.trimf(w.universe, [30, 60, 90])
        w["long"] = fuzz.trapmf(w.universe, [70, 100, WAIT_MAX, WAIT_MAX])

        g["short"] = fuzz.trapmf(g.universe, [10, 10, 15, 25])
        g["medium"] = fuzz.trimf(g.universe, [20, 35, 50])
        g["long"] = fuzz.trapmf(g.universe, [40, 50, GREEN_MAX, GREEN_MAX])

        # Rules: AND = min, aggregation = max, defuzzification = centroid
        rules = [
            ctrl.Rule(d[dl] & w[wl], g[gl]) for (dl, wl), gl in RULE_TABLE.items()
        ]
        self.system = ctrl.ControlSystem(rules)
        self.sim = ctrl.ControlSystemSimulation(self.system)

    def compute(self, density, waiting):
        """Return green-light duration (s) for a given density (cars/min) and waiting time (s)."""
        self.sim.input["density"] = float(np.clip(density, 0, DENSITY_MAX))
        self.sim.input["waiting"] = float(np.clip(waiting, 0, WAIT_MAX))
        self.sim.compute()
        return float(self.sim.output["green"])