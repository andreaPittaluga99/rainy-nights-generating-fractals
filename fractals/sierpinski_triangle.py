import os

import matplotlib.pyplot as plt


def sierpinski(p1, p2, p3, depth):
    if depth == 0:
        plt.fill([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], color="white")
        return

    # get middle point
    m1 = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    m2 = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
    m3 = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)

    # recursion on external triangles
    sierpinski(p1, m1, m3, depth - 1)
    sierpinski(m1, p2, m2, depth - 1)
    sierpinski(m3, m2, p3, depth - 1)


# starting triangle
p1 = (0, 0)
p2 = (1, 0)
p3 = (0.5, 0.866)

plt.figure(figsize=(8, 8))

sierpinski(p1, p2, p3, 8)

plt.axis("off")
plt.savefig(
    os.path.join("..", "output", "sierpinski.png"),
    dpi=300,
    bbox_inches="tight",
    facecolor="black",
)
