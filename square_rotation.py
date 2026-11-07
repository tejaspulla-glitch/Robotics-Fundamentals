"""This program asks for an input of degrees to rotate a square by and the number of rotations, then outputs a square rotated by that angle for that many rotations"""

import numpy as np
import matplotlib.pyplot as plt

#Function inputs an angle in degrees and converts it to a transformation matrix
def rotation_matrix(angle_deg):
    theta = np.radians(angle_deg)
    s, c = np.sin(theta), np.cos(theta)
    return np.array([[c, -s],
                     [s,  c]])

#Function rotates square by the transformation matrix
def rotate_shape(shape_vertices, angle_deg):
    R = rotation_matrix(angle_deg)
    return (R @ shape_vertices.T).T

def main():
    angle = int(input("Angle to rotate shape by:"))
    square_vertices = np.array([
        [-1, -1],
        [ 1, -1],
        [ 1,  1],
        [-1,  1],
        [-1, -1],
    ])
    rotations = int(input("Number of rotations:"))
    for i in range(rotations):
        new_square = rotate_shape(square_vertices, angle)
        plt.figure()
        plt.plot(square_vertices[:, 0], square_vertices[:, 1], label="original")
        plt.plot(new_square[:, 0], new_square[:, 1], label=f"rotated {angle}°")
        plt.axis("equal")
        plt.grid(True)
        plt.legend()
        plt.show()
        angle = angle + 15



main()
