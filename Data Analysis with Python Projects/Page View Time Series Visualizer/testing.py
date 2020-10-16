import matplotlib
import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

fig, ax = plt.subplots()
ax.bar(labels, men_means)
ax.bar(labels, women_means)
plt.show()