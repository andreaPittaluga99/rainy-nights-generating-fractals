import os

import matplotlib.pyplot as plt
import numpy as np


def julia(z, c, max_iteration):
    for n in range(max_iteration):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iteration


def generate_fractal(x_min, x_max, y_min, y_max, width, height, max_iteration, c):
    real = np.linspace(x_min, x_max, width)
    imaginary = np.linspace(y_min, y_max, height)

    fractal = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            z = real[j] + 1j * imaginary[i]
            fractal[i, j] = julia(z, c, max_iteration)

    return fractal


c = -0.5125 + 0.5213j

x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5

fractal = generate_fractal(
    x_min, x_max, y_min, y_max, width=960, height=900, max_iteration=150, c=c
)

plt.imsave(
    os.path.join("..", "output", "julia.png"),
    fractal,
    cmap="spring",
)
