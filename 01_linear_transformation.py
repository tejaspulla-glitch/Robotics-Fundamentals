"""Project 1: visualizing a linear transformation.

Two input vectors are multiplied by a 2x2 matrix A. The original vectors are
drawn in red and the transformed vectors in blue, so you can see what A does.
"""

import numpy as np
import matplotlib.pyplot as plt


def input_vectors():
    """Two input vectors, each given as [x, y]."""
    v1 = np.array([3, 2])
    v2 = np.array([-5, 3])
    return v1, v2


def transformation_matrix():
    """Flips and doubles x (-2), and stretches y by 5."""
    return np.array([[-2, 0],
                     [0, 5]])


def output_vectors(A, v1, v2):
    """Apply the matrix A to both vectors."""
    return A @ v1, A @ v2


def draw_vectors(ax, vectors, color, label):
    """Draw each vector as an arrow starting at the origin."""
    for n, v in enumerate(vectors):
        ax.quiver(0, 0, v[0], v[1],
                  angles="xy", scale_units="xy", scale=1,
                  color=color, label=label if n == 0 else None)


def main():
    v1, v2 = input_vectors()
    A = transformation_matrix()
    Av1, Av2 = output_vectors(A, v1, v2)

    fig, ax = plt.subplots()
    draw_vectors(ax, [v1, v2], "red", "input vectors")
    draw_vectors(ax, [Av1, Av2], "blue", "after transformation (A @ v)")

    limit = max(abs(np.concatenate([v1, v2, Av1, Av2]))) + 2
    ax.set_xlim(-limit, limit)
    ax.set_ylim(-limit, limit)
    ax.set_aspect("equal")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.axvline(0, color="black", linewidth=0.5)
    ax.grid(True, alpha=0.3)
    ax.set_title("Linear transformation of two vectors")
    ax.legend(loc="lower right")
    return fig


if __name__ == "__main__":
    main()
    plt.show()
