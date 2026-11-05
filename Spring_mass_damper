import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def mass_spring_damper(t, y, m, c, k, F_ext):
    """
    State space representation of the mass-spring-damper system.
    y[0] = position (x)
    y[1] = velocity (v)
    """
    x, v = y
    dxdt = v
    dvdt = (F_ext(t) - c * v - k * x) / m
    return [dxdt, dvdt]

# --- System Parameters ---
m = 1.0   # Mass (kg)
c = 0.5   # Damping coefficient (N·s/m)
k = 10.0  # Spring constant (N/m)

# Optional external force function F(t) (e.g., zero for free vibration, or a step/sinusoidal force)
F_ext = lambda t: 0.0  

# --- Initial Conditions & Time Span ---
x0 = 1.0   # Initial displacement (m)
v0 = 0.0   # Initial velocity (m/s)
y0 = [x0, v0]

t_start = 0.0
t_end = 15.0
t_eval = np.linspace(t_start, t_end, 1000)

# --- Solve ODE ---
sol = solve_ivp(
    fun=mass_spring_damper,
    t_span=(t_start, t_end),
    y0=y0,
    t_eval=t_eval,
    args=(m, c, k, F_ext)
)

# --- Plot Position vs. Time ---
plt.figure(figsize=(9, 5))
plt.plot(sol.t, sol.y[0], label=f'Position $x(t)$ ($m={m}, c={c}, k={k}$)', color='tab:blue', lw=2)
plt.title('Mass-Spring-Damper System Response', fontsize=12, fontweight='bold')
plt.xlabel('Time $t$ (s)', fontsize=11)
plt.ylabel('Displacement $x$ (m)', fontsize=11)
plt.axhline(0, color='gray', linestyle='--', alpha=0.7)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(frameon=True)
plt.tight_layout()
plt.show()
