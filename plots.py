"""
This module contains functions to plot the fuzzy membership functions and the resulting surface
of the fuzzy traffic light control system.

# density, waiting and green are fuzzy variable which are defined in fuzzy_system.py.
# FuzzyTrafficLight.compute() computes the green light duration based on the traffic density and 
  waiting time. This is also imported from fuzzy_system.py.

- density: Traffic density (cars/min)
- waiting: Waiting time (s)
- green: Green light duration (s)
"""

import numpy as np;
import matplotlib.pyplot as plt;
import fuzzy_system;

fuzzy_light = fuzzy_system.FuzzyTrafficLight();

def plot_memberships():
    """View the membership functions for each fuzzy variable."""
    fuzzy_light.density.view();
    fuzzy_light.waiting.view();
    fuzzy_light.green.view();
    plt.show();

