import os

import matplotlib.pyplot as plt
import numpy as np


def mandelbrot(c, max_iteration):
    z = 0
    for n in range(max_iteration):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iteration


def generate_fractal(x_min, x_max, y_min, y_max, width, height, max_iteration):
    real = np.linspace(x_min, x_max, width)
    imaginary = np.linspace(y_min, y_max, height)
    fractal = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            fractal[i, j] = mandelbrot(real[j] + 1j * imaginary[i], max_iteration)
    return fractal


x_min, x_max, y_min, y_max = -2.0, 1.0, -1.5, 1.5

fractal = generate_fractal(
    x_min, x_max, y_min, y_max, width=960, height=900, max_iteration=100
)

plt.imsave(
    os.path.join("..", "output", "mandelbrot.png"),
    fractal,
    cmap="rainbow",
)
