"""
This program uses the previous falling ball simulation and improves upon it using the euler method to produce better results
"""

import matplotlib.pyplot as plt
import numpy as np

mass = 1.0  # kg
g = 9.81  # m/s^2 (gravity)
t_start = 0.0  # s
t_end = 10.0  # s
dt = 0.1  # time step in seconds

t = np.arange(t_start, t_end + dt, dt)

y = np.zeros_like(t)  # height (position)
v = np.zeros_like(t)  # velocity

y[0] = 200.0  # starting height in meters
v[0] = 0.0  # initial velocity in m/s

# Euler integration loop
for i in range(0, len(t) - 1):
  # Net force: gravity acting downwards (-mg)
  f_net = -mass * g

  # Forward Euler updates using eulers method
  v[i + 1] = v[i] + (f_net / mass) * dt
  y[i + 1] = y[i] + v[i] * dt

  # Stop if the ball hits the ground
  if y[i + 1] <= 0:
    y[i + 1] = 0.0
    v[i + 1] = 0.0

plt.figure(figsize=(8, 5))
plt.plot(t[: len(y)], y[: len(y)], marker='o', label='Height (m)')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Falling Ball Simulation via Euler Integration')
plt.grid(True)
plt.legend()
plt.show()
