"""
This program uses solve_ivp to simulate the motion of a pendulum using differential equations.
"""


import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


g = 9.81  # Acceleration due to gravity (m/s^2)
L = 1.0  # Length of the pendulum (m)


def pendulum_ode(t, y):
  theta, omega = y
  dtheta_dt = omega
  domega_dt = -(g / L) * np.sin(theta)
  return [dtheta_dt, domega_dt]


# Set initial conditions and time span
theta_0 = np.radians(60) # Intital angle when pendulum is released
omega_0 = 0.0
y0 = [theta_0, omega_0]

t_span = (0, 10)  # Simulate from t = 0 to t = 10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Evaluation points

# Solve the ODE using solve_ivp
sol = solve_ivp(pendulum_ode, t_span, y0, t_eval=t_eval, method="RK45")

# Plot the results
plt.figure(figsize=(12, 5))

# Angle and Angular Velocity vs Time
plt.subplot(1, 2, 1)
plt.plot(sol.t, np.degrees(sol.y[0]), label=r"Angle ($\theta$)", color="b")
plt.plot(
    sol.t,
    sol.y[1],
    label=r"Angular Velocity ($\omega$)",
    color="r",
    linestyle="--",
)
plt.axhline(0, color="gray", linewidth=0.8, linestyle=":")
plt.title("Pendulum Motion Over Time")
plt.xlabel("Time ($s$)")
plt.ylabel("State")
plt.legend()
plt.grid(True)
