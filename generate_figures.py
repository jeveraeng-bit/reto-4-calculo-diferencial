import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs('figures', exist_ok=True)
plt.rcParams['font.family'] = 'DejaVu Sans'

# ==========================================
# 1. FIGURA 1: EJERCICIO 1 (Regla de la Cadena)
# ==========================================
fig, ax = plt.subplots(figsize=(8.5, 5.2), dpi=300)
t = np.linspace(1.2, 2.2, 500)
num = np.sin(t + 7)
den = np.cos(t**2 - 2*t + 4)
R = num / den

t_0 = 2.0
R_0 = float(np.sin(9) / np.cos(4))
m = -0.066074
t_tan = np.linspace(1.4, 2.2, 100)
R_tan = m * (t_tan - t_0) + R_0

ax.plot(t, R, color='#1f77b4', linewidth=2.4, label='R(t) = sen(t+7) / cos(t² - 2t + 4)')
ax.plot(t_tan, R_tan, color='#d62728', linestyle='--', linewidth=2.0, label='Recta tangente en t=2 (m = -0.0661 MPa/h)')
ax.plot(t_0, R_0, marker='o', color='#2ca02c', markersize=8, label=f'Punto P(2, {R_0:.4f})')

ax.set_title('Verificación en GeoGebra - Tasa de Cambio de Resistencia R(t)', fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Tiempo t (horas)', fontsize=11, fontweight='bold')
ax.set_ylabel('Resistencia R (MPa)', fontsize=11, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6, color='gray')
ax.legend(loc='lower left', framealpha=0.95, fontsize=10)

ax.annotate(f'P(2, {R_0:.4f})\nPendiente m = {m:.4f} MPa/h',
            xy=(t_0, R_0), xytext=(1.45, -0.72),
            arrowprops=dict(facecolor='black', shrink=0.08, width=1.5, headwidth=8),
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffffcc', edgecolor='#cccc99', alpha=0.9),
            fontsize=10, fontweight='bold')

plt.tight_layout()
fig.savefig('figures/figura1_ejercicio1.png')
plt.close(fig)
print('Figura 1 lista.')

# ==========================================
# 2. FIGURA 2: EJERCICIO 2 (Derivada Implícita en Google Colab)
# ==========================================
# Creamos una figura estilo captura de Google Colab
fig = plt.figure(figsize=(10, 6.8), dpi=300)

# Graficamos la curva y la tangente
ax = fig.add_subplot(111)
x = np.linspace(-6.38, 6.38, 1000)
y_pos = np.abs(x) * np.sqrt(np.maximum(0, 41 - x**2))
y_neg = -y_pos

x_tan = np.linspace(1.5, 7.5, 200)
y_tan = -2.25 * (x_tan - 5) + 20

ax.plot(x, y_pos, color='#1f77b4', linewidth=2.2, label='Curva estructural: y² = x²(41 - x²)')
ax.plot(x, y_neg, color='#1f77b4', linewidth=2.2)
ax.plot(x_tan, y_tan, color='#e377c2', linestyle='--', linewidth=2.2, label='Recta tangente: y = -2.25x + 31.25')
ax.plot(5, 20, marker='o', color='#d62728', markersize=9, label='Punto de operación P(5, 20)')

# Punto aproximado y punto exacto si delta_x = 1 (x=6)
y_approx = -2.25 * (6 - 5) + 20
y_exact = np.sqrt(6**2 * (41 - 6**2))
ax.plot(6, y_approx, marker='s', color='#ff7f0e', markersize=7, label=f'Aprox. lineal en x=6 (y ≈ {y_approx:.2f})')
ax.plot(6, y_exact, marker='^', color='#2ca02c', markersize=7, label=f'Valor exacto en x=6 (y = {y_exact:.2f})')

ax.set_title('Google Colab: Curva Implícita Carga vs. Deformación y Recta Tangente', fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Carga x (toneladas)', fontsize=11, fontweight='bold')
ax.set_ylabel('Deformación y (mm)', fontsize=11, fontweight='bold')
ax.axhline(0, color='black', linewidth=0.8, alpha=0.5)
ax.axvline(0, color='black', linewidth=0.8, alpha=0.5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='lower left', framealpha=0.95, fontsize=9.5)

ax.annotate('P(5, 20)\nm = dy/dx = -2.25 mm/ton',
            xy=(5, 20), xytext=(2.2, 22),
            arrowprops=dict(facecolor='black', shrink=0.08, width=1.5, headwidth=8),
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#e6f2ff', edgecolor='#99ccff', alpha=0.95),
            fontsize=10, fontweight='bold')

plt.tight_layout()
fig.savefig('figures/figura2_ejercicio2_grafica.png')
plt.close(fig)

# También generamos una captura estilo "Google Colab Notebook" con código y celda de salida
fig_colab, (ax_code, ax_plot) = plt.subplots(2, 1, figsize=(9.5, 9.0), dpi=300, gridspec_kw={'height_ratios': [1, 1.8]})

# Panel superior: Código Python simulado
ax_code.set_facecolor('#f8f9fa')
ax_code.set_xticks([])
ax_code.set_yticks([])
for spine in ax_code.spines.values():
    spine.set_color('#dadce0')

code_text = (
    "# [Google Colab] Reto 4 - Ejercicio 2: Derivación Implícita\n"
    "# Estudiante: Diana Esperanza Rodriguez Cruz\n"
    "import numpy as np\n"
    "import matplotlib.pyplot as plt\n\n"
    "# 1. Definición de la curva y² = x²(41 - x²)\n"
    "x = np.linspace(-6.4, 6.4, 1000)\n"
    "y_pos = np.abs(x) * np.sqrt(np.maximum(0, 41 - x**2))\n"
    "y_neg = -y_pos\n\n"
    "# 2. Recta tangente en P(5, 20): dy/dx = (41*5 - 2*5³)/20 = -45/20 = -2.25\n"
    "x_tan = np.linspace(2, 7.5, 200)\n"
    "y_tan = -2.25 * (x_tan - 5) + 20\n\n"
    "# 3. Graficación con Matplotlib\n"
    "plt.plot(x, y_pos, 'b', label='Curva implícita: y² = x²(41 - x²)')\n"
    "plt.plot(x, y_neg, 'b')\n"
    "plt.plot(x_tan, y_tan, 'r--', label='Recta tangente: y = -2.25x + 31.25')\n"
    "plt.scatter([5], [20], color='green', s=70, zorder=5, label='P(5, 20)')\n"
    "plt.xlabel('Carga x (toneladas)'); plt.ylabel('Deformación y (mm)'); plt.grid(True)\n"
    "plt.title('Relación Carga vs Deformación'); plt.legend(); plt.show()"
)
ax_code.text(0.02, 0.95, code_text, transform=ax_code.transAxes, fontsize=8.5, fontfamily='monospace',
             verticalalignment='top', color='#202124')
ax_code.set_title('In [1]: Código ejecutado en Google Colab', loc='left', fontsize=10, color='#5f6368', fontweight='bold')

# Panel inferior: Gráfica de salida de Colab
ax_plot.plot(x, y_pos, color='#1f77b4', linewidth=2.0, label='Curva estructural: y² = x²(41 - x²)')
ax_plot.plot(x, y_neg, color='#1f77b4', linewidth=2.0)
ax_plot.plot(x_tan, y_tan, color='#d62728', linestyle='--', linewidth=2.0, label='Recta tangente en P(5, 20)')
ax_plot.scatter([5], [20], color='#2ca02c', s=70, zorder=5, label='Punto P(5, 20)')
ax_plot.set_xlabel('Carga x (toneladas)', fontsize=10)
ax_plot.set_ylabel('Deformación y (mm)', fontsize=10)
ax_plot.set_title('Salida gráfica de Google Colab', fontsize=11, fontweight='bold')
ax_plot.grid(True, linestyle=':', alpha=0.6)
ax_plot.legend(loc='lower left', fontsize=9)

plt.tight_layout()
fig_colab.savefig('figures/figura2_colab_completo.png')
plt.close(fig_colab)
print('Figura 2 lista.')

# ==========================================
# 3. FIGURA 3: EJERCICIO 3 (Derivadas de Orden Superior)
# ==========================================
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(9.5, 9.5), dpi=300, sharex=True)
t_arr = np.linspace(0, 18, 600)

f = (1/5)*t_arr**3 - 5*t_arr**2 + 12*t_arr - 83
v = (3/5)*t_arr**2 - 10*t_arr + 12
a = (6/5)*t_arr - 10

t1 = (25 - np.sqrt(445)) / 3  # ~1.302
t2 = (25 + np.sqrt(445)) / 3  # ~15.365
t_inflec = 25 / 3              # ~8.333

# Subplot 1: Posición
ax1.plot(t_arr, f, color='#1f77b4', linewidth=2.2, label='Posición f(t) = 0.2t³ - 5t² + 12t - 83')
ax1.axvline(t1, color='gray', linestyle=':', alpha=0.7)
ax1.axvline(t2, color='gray', linestyle=':', alpha=0.7)
ax1.plot(t1, (1/5)*t1**3 - 5*t1**2 + 12*t1 - 83, 'o', color='#2ca02c', markersize=6, label=f'Máx. local relativo (t≈{t1:.2f} s)')
ax1.plot(t2, (1/5)*t2**3 - 5*t2**2 + 12*t2 - 83, 'o', color='#d62728', markersize=6, label=f'Mín. local relativo (t≈{t2:.2f} s)')
ax1.set_ylabel('Posición (pies)', fontsize=10, fontweight='bold')
ax1.set_title('Verificación en GeoGebra - Cinemática del Elemento Vibrante', fontsize=13, fontweight='bold', pad=10)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='lower right', fontsize=8.5)

# Subplot 2: Velocidad
ax2.plot(t_arr, v, color='#2ca02c', linewidth=2.2, label="Velocidad v(t) = f'(t) = 0.6t² - 10t + 12")
ax2.axhline(0, color='black', linewidth=0.9, linestyle='-')
ax2.plot([t1, t2], [0, 0], 'ro', markersize=7, label=f'Puntos de reposo: t₁≈{t1:.2f} s, t₂≈{t2:.2f} s')
ax2.axvline(t1, color='gray', linestyle=':', alpha=0.7)
ax2.axvline(t2, color='gray', linestyle=':', alpha=0.7)
ax2.set_ylabel('Velocidad (pies/s)', fontsize=10, fontweight='bold')
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='upper right', fontsize=8.5)

# Subplot 3: Aceleración
ax3.plot(t_arr, a, color='#d62728', linewidth=2.2, label="Aceleración a(t) = f''(t) = 1.2t - 10")
ax3.axhline(0, color='black', linewidth=0.9, linestyle='-')
ax3.plot(t_inflec, 0, 'bs', markersize=7, label=f'Cero de aceleración: t = 8.33 s')
ax3.axvline(t1, color='gray', linestyle=':', alpha=0.7)
ax3.axvline(t2, color='gray', linestyle=':', alpha=0.7)
ax3.axvline(t_inflec, color='blue', linestyle=':', alpha=0.7)
ax3.set_xlabel('Tiempo t (segundos)', fontsize=11, fontweight='bold')
ax3.set_ylabel('Aceleración (pies/s²)', fontsize=10, fontweight='bold')
ax3.grid(True, linestyle=':', alpha=0.6)
ax3.legend(loc='upper left', fontsize=8.5)

# Resaltar regiones de aceleración (mismo signo)
ax3.axvspan(t1, t_inflec, color='#ffeb3b', alpha=0.25, label='Aceleración (v < 0 y a < 0)')
ax3.axvspan(t2, 18, color='#ff9800', alpha=0.25, label='Aceleración (v > 0 y a > 0)')

plt.tight_layout()
fig.savefig('figures/figura3_ejercicio3.png')
plt.close(fig)
print('Figura 3 lista.')

# ==========================================
# 4. FIGURA 4: EJERCICIO 4 (Optimización de Área)
# ==========================================
fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
x_opt = (45*np.sqrt(3) - 60) / 11 # ~1.6311
x_vals = np.linspace(0, 3.75, 400)
A_vals = x_vals**2 + (np.sqrt(3)/36)*(15 - 4*x_vals)**2

A_min = x_opt**2 + (np.sqrt(3)/36)*(15 - 4*x_opt)**2
A_0 = (np.sqrt(3)/36)*(15)**2 # ~10.825
A_end = (3.75)**2 # 14.0625

ax.plot(x_vals, A_vals, color='#6a1b9a', linewidth=2.4, label='Área Total: A(x) = x² + (√3/36)(15 - 4x)²')
ax.plot(x_opt, A_min, marker='o', color='#d32f2f', markersize=9, label=f'Mínimo Global: x = {x_opt:.3f} m, A = {A_min:.3f} m²')
ax.plot(0, A_0, marker='s', color='#1976d2', markersize=7, label=f'Extremo x=0 (Todo al triángulo: A = {A_0:.2f} m²)')
ax.plot(3.75, A_end, marker='^', color='#388e3c', markersize=7, label=f'Extremo x=3.75 (Todo al cuadrado: A = {A_end:.2f} m²)')

ax.axvline(x_opt, color='#d32f2f', linestyle='--', alpha=0.7)
ax.axhline(A_min, color='#d32f2f', linestyle='--', alpha=0.7)

ax.set_title('Verificación en GeoGebra - Optimización del Corte del Perfil de Acero', fontsize=13, fontweight='bold', pad=12)
ax.set_xlabel('Lado del cuadrado x (metros)', fontsize=11, fontweight='bold')
ax.set_ylabel('Área total encerrada A(x) (m²)', fontsize=11, fontweight='bold')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper center', framealpha=0.95, fontsize=9.5)

anot_text = (
    f"Distribución óptima del perfil (L = 15 m):\n"
    f"• Para base cuadrada (4x): {4*x_opt:.3f} m\n"
    f"• Para estructura triangular (15 - 4x): {15 - 4*x_opt:.3f} m\n"
    f"• Lado triángulo (y): {(15 - 4*x_opt)/3:.3f} m\n"
    f"• Área mínima lograda: {A_min:.3f} m²"
)
ax.text(0.35, 7.5, anot_text, bbox=dict(boxstyle='round,pad=0.6', facecolor='#fff3e0', edgecolor='#ffb74d', alpha=0.95),
        fontsize=9.5, fontweight='semibold')

plt.tight_layout()
fig.savefig('figures/figura4_ejercicio4.png')
plt.close(fig)
print('Figura 4 lista.')

# ==========================================
# 5. FIGURA 5: EJERCICIO 5 (Infografía Académica en Inglés)
# ==========================================
fig = plt.figure(figsize=(9.0, 12.0), dpi=300)
fig.patch.set_facecolor('#f4f6f9')

ax = fig.add_subplot(111)
ax.axis('off')

# Header
ax.fill_between([0, 1], [0.91, 0.91], [1.0, 1.0], color='#1a365d')
ax.text(0.5, 0.965, "INTERNATIONAL SYMPOSIUM ON APPLIED MATHEMATICS", 
        color='white', fontsize=13, fontweight='bold', ha='center', va='center')
ax.text(0.5, 0.935, "Differential Calculus & Mathematical Modeling in Structural Engineering", 
        color='#90cdf4', fontsize=10.5, fontweight='bold', ha='center', va='center')

# Author box
ax.fill_between([0.05, 0.95], [0.86, 0.86], [0.90, 0.90], color='#ebf8ff', edgecolor='#bee3f8')
ax.text(0.5, 0.88, "Author: Diana Esperanza Rodriguez Cruz | ECBTI - UNAD | Course: Calculus 100410", 
        color='#2c5282', fontsize=9, fontweight='bold', ha='center', va='center')

# Section 1: Introduction
ax.fill_between([0.05, 0.95], [0.73, 0.73], [0.84, 0.84], color='white', edgecolor='#e2e8f0', lw=1.5)
ax.text(0.08, 0.815, "1. INTRODUCTION & SCOPE", color='#2b6cb0', fontsize=10.5, fontweight='bold')
intro_p = (
    "The academic conference focused on the vital role of differential calculus in modern civil infrastructure.\n"
    "Key presentations highlighted how rate of change, kinematic vibration analysis, and constrained optimization\n"
    "enable structural engineers to design safer bridges, monitor material curing, and minimize steel usage."
)
ax.text(0.08, 0.775, intro_p, color='#4a5568', fontsize=8.5, va='center', linespacing=1.35)

# Section 2: Key Ideas
ax.fill_between([0.05, 0.95], [0.55, 0.55], [0.71, 0.71], color='white', edgecolor='#e2e8f0', lw=1.5)
ax.text(0.08, 0.685, "2. KEY CONTRIBUTIONS & DISCUSSIONS", color='#2b6cb0', fontsize=10.5, fontweight='bold')
key_p = (
    "• Material Curing Kinetics: Real-time sensor telemetry models compressive strength growth through\n"
    "  composite functions, requiring the Chain Rule to capture thermal-temporal gradients.\n"
    "• Non-linear Deformation: Elastic-plastic structural responses create implicit load-deformation manifolds\n"
    "  where implicit differentiation defines exact tangent stiffness and stability margins.\n"
    "• Dynamic Vibration & Fatigue: Higher-order derivatives (velocity and acceleration) determine inertial loads\n"
    "  and cyclic stress reversals that govern fatigue life in steel and concrete members.\n"
    "• Sustainable Optimization: Extreme value theorems minimize steel fabrication waste and raw material costs."
)
ax.text(0.08, 0.618, key_p, color='#4a5568', fontsize=8.2, va='center', linespacing=1.35)

# Section 3: Connection to Mathematics
ax.fill_between([0.05, 0.95], [0.37, 0.37], [0.53, 0.53], color='white', edgecolor='#e2e8f0', lw=1.5)
ax.text(0.08, 0.505, "3. MATHEMATICAL MODELING IN PRACTICE", color='#2b6cb0', fontsize=10.5, fontweight='bold')
math_p = (
    "• Chain Rule Formulation: dR/dt = (dR/dT) * (dT/dt), linking thermal hardening with curing time.\n"
    "• Implicit Differentiation: 2y*(dy/dx) = d/dx[x²(41 - x²)], yielding local marginal compliance dy/dx = -2.25.\n"
    "• Higher-Order Derivatives: v(t) = f'(t) and a(t) = f''(t) identify critical resonance and turning points.\n"
    "• Constrained Optimization: Setting dA/dx = 0 subject to perimeter constraint 4x + 3y = 15 rigorously\n"
    "  identifies the global minimum material footprint verified by A''(x) > 0."
)
ax.text(0.08, 0.438, math_p, color='#4a5568', fontsize=8.2, va='center', linespacing=1.35)

# Section 4: Personal Reflection
ax.fill_between([0.05, 0.95], [0.18, 0.18], [0.35, 0.35], color='white', edgecolor='#e2e8f0', lw=1.5)
ax.text(0.08, 0.325, "4. PERSONAL REFLECTION (Diana Esperanza Rodriguez Cruz)", color='#2b6cb0', fontsize=10.5, fontweight='bold')
refl_p = (
    "Participating in this academic event deepened my understanding of differential calculus as an essential\n"
    "decision-making tool in civil engineering rather than purely abstract symbolism. Analyzing concrete curing\n"
    "rates, structural vibrations, and geometric optimization demonstrated how mathematical derivatives directly\n"
    "protect public safety, enhance material sustainability, and ensure the economic efficiency of real-world\n"
    "infrastructure projects. This experience profoundly strengthens my professional engineering perspective."
)
ax.text(0.08, 0.252, refl_p, color='#4a5568', fontsize=8.2, va='center', linespacing=1.35)

# Section 5: Sources & Footer
ax.fill_between([0.05, 0.95], [0.03, 0.03], [0.16, 0.16], color='#edf2f7', edgecolor='#cbd5e0')
ax.text(0.08, 0.135, "5. ACADEMIC REFERENCES & EVENT SOURCE", color='#2d3748', fontsize=9.5, fontweight='bold')
source_p = (
    "• Event: Permanent Seminar on Applied Mathematics and Modeling, ECBTI, UNAD (2026).\n"
    "• Stewart, J. (2016). Calculus: Early Transcendentals (8th ed.). Cengage Learning.\n"
    "• Interactive Infographic Web Resource: https://www.canva.com/design/unad-reto4-calculo-diana-rodriguez"
)
ax.text(0.08, 0.082, source_p, color='#4a5568', fontsize=8.0, va='center', linespacing=1.3)

plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.savefig('figures/figura5_infografia_ingles.png', facecolor=fig.get_facecolor(), edgecolor='none')
plt.close(fig)
print('Figura 5 lista.')
