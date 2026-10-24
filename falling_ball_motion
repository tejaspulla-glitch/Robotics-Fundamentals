import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

g = 9.81      # gravity
m = 0.145     # mass of ball
rho = 1.225   # air density
Cd = 0.47     # drag coefficient
r = 0.037     # radius of ball
A = np.pi * r**2
k = 0.5 * rho * Cd * A

def falling_ball(t, state):
    position, velocity = state
    dvel_dt = -g - (k / m) * velocity * np.abs(velocity)
    return [velocity, dvel_dt]

def hit_ground(t, state):
    return state[0]          # event triggers when height = 0
hit_ground.terminal = True
hit_ground.direction = -1    # only when moving downward

sol = integrate.solve_ivp(
    falling_ball, (0, 10), [1, 1],
    t_eval=np.linspace(0, 10, 500),
    events=hit_ground,
)

height, velocity = sol.y

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(sol.t, height)
ax1.set_ylabel("Height (m)")
ax2.plot(sol.t, velocity)
ax2.set_ylabel("Velocity (m/s)")
ax2.set_xlabel("Time (s)")
plt.show()
