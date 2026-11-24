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

def plot_surface():
    """View the resulting surface of the fuzzy traffic light control system."""
    d = np.arange(0, fuzzy_system.DENSITY_MAX + 1, 3);
    w = np.arange(0, fuzzy_system.WAIT_MAX + 1, 6);
    D, W = np.meshgrid(d, w);
    G = np.zeros_like(D, dtype=float);

    for i in range(D.shape[0]):
        for j in range(D.shape[1]):
            G[i, j] = fuzzy_light.compute(D[i, j], W[i, j]);

    fig = plt.figure();
    ax = fig.add_subplot(111, projection='3d');
    ax.plot_surface(D, W, G, cmap='viridis');
    ax.set_xlabel('Traffic density (cars/min)');
    ax.set_ylabel('Waiting time (s)');
    ax.set_zlabel('Green Light Duration (s)');
    ax.set_title('Fuzzy traffic light control surface');
    plt.show();