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
        d["high"] = fuzz.trapmf(d.universe, [35, 50, 60, 60])

        w["short"] = fuzz.trapmf(w.universe, [0, 0, 20, 50])
        w["medium"] = fuzz.trimf(w.universe, [30, 60, 90])
        w["long"] = fuzz.trapmf(w.universe, [70, 100, 120, 120])

        g["short"] = fuzz.trapmf(g.universe, [10, 10, 15, 25])
        g["medium"] = fuzz.trimf(g.universe, [20, 35, 50])
        g["long"] = fuzz.trapmf(g.universe, [40, 50, 60, 60])

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