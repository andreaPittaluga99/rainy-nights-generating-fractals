import os

import matplotlib.pyplot as plt
import numpy as np


def barnsley(number_of_iterations):
    x = np.zeros(number_of_iterations)
    y = np.zeros(number_of_iterations)

    random = np.random.random(number_of_iterations)
    start_x, start_y = 0.0, 0.0

    for i in range(number_of_iterations):
        if random[i] < 0.01:
            new_x = 0
            new_y = 0.16 * start_y
        elif random[i] < 0.86:
            new_x = start_x * 0.85 + 0.04 * start_y
            new_y = start_x * -0.04 + start_y * 0.85 + 1.6
        elif random[i] < 0.93:
            new_x = start_x * 0.2 - start_y * 0.26
            new_y = start_x * 0.23 + start_y * 0.22 + 1.6
        else:
            new_x = start_x * -0.15 + start_y * 0.28
            new_y = start_x * 0.26 + start_y * 0.24 + 0.44

        start_x, start_y = new_x, new_y
        x[i] = start_x
        y[i] = start_y

    return x, y


x, y = barnsley(number_of_iterations=500000)

plt.figure(figsize=(8, 12), facecolor="black")
plt.scatter(x, y, s=0.05, color="forestgreen")
plt.axis("off")

plt.savefig(
    os.path.join("..", "output", "barnsley_fern.png"),
    dpi=300,
    bbox_inches="tight",
    pad_inches=0,
)
