# Reto 4: Diseño de Soluciones Mediante la Derivada

**Universidad Nacional Abierta y a Distancia (UNAD)**  
**Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)**  
**Curso:** Cálculo Diferencial (Código 100410)  
**Estudiante (Responsable y Única Integrante):** Diana Esperanza Rodriguez Cruz  
**Contexto Asignado:** Contexto D — Ingeniería Civil: Diseño de Estructuras y Materiales  
**Normativa Editorial:** Normas APA (7.ª Edición)  

---

## 📄 Documento Principal en PDF
El informe técnico completo en formato PDF, elaborado en estricto cumplimiento de la **Normativa APA 7.ª edición**, se encuentra disponible en este repositorio:

* 📥 **[Descargar / Ver PDF del Informe Técnico](Reto_4_Calculo_Diferencial_Contexto_D_Diana_Rodriguez.pdf)**
* 🔗 **Enlace directo en GitHub:** [https://github.com/jeveraeng-bit/reto-4-calculo-diferencial/blob/main/Reto_4_Calculo_Diferencial_Contexto_D_Diana_Rodriguez.pdf](https://github.com/jeveraeng-bit/reto-4-calculo-diferencial/blob/main/Reto_4_Calculo_Diferencial_Contexto_D_Diana_Rodriguez.pdf)

---

## 🎯 Estructura y Solución Integral de los Ejercicios (Contexto D)

Cada ejercicio fue resuelto siguiendo rigurosamente los **tres momentos de argumentación pedagógica**:
1. **Momento I:** Justificación teórica y conceptual de la técnica sin calcular.
2. **Momento II:** Desarrollo algebraico paso a paso con el editor formal de ecuaciones.
3. **Momento III:** Verificación con herramientas digitales (GeoGebra / Google Colab) e interpretación física en el contexto de la ingeniería civil.

### Resumen de Ejercicios Desarrollados:

* **Ejercicio 1: Regla de la cadena – Tasa de cambio de la resistencia del material**
  * *Modelo:* $R(T) = \frac{\sin(T+7)}{\cos(T^2-2T+4)}$, $T(t) = t$.
  * *Evaluación:* A las $t = 2$ horas, $\frac{dR}{dt} \approx -0.0661 \text{ MPa/h}$.
  * *Verificación:* Gráfica en GeoGebra con pendiente de la recta tangente.

* **Ejercicio 2: Derivada implícita – Relación carga vs. deformación estructural**
  * *Ecuación:* $y^2 = x^2(41 - x^2)$, punto de monitoreo $P(5, 20)$.
  * *Resultado:* Pendiente marginal $\frac{dy}{dx}\Big|_{(5, 20)} = -2.25 \text{ mm/ton}$.
  * *Recta tangente:* $y = -2.25x + 31.25$ ($9x + 4y - 125 = 0$).
  * *Verificación:* Cuaderno interactivo de Google Colab con código Python ejecutado.
  * *Interpretación diferencial:* Si la carga aumenta en 1 tonelada ($\Delta x = +1$), $\Delta y \approx -2.25 \text{ mm}$.

* **Ejercicio 3: Derivadas de orden superior – Cinemática y fatiga del elemento vibrante**
  * *Función de posición:* $f(t) = \frac{1}{5}t^3 - 5t^2 + 12t - 83$ (pies), $t \ge 0$.
  * *Velocidad:* $f'(t) = \frac{3}{5}t^2 - 10t + 12$. Instantes de reposo: $t_1 \approx 1.30 \text{ s}$ y $t_2 \approx 15.37 \text{ s}$.
  * *Aceleración:* $f''(t) = \frac{6}{5}t - 10$. Cero de aceleración: $t = 8.33 \text{ s}$.
  * *Movimiento positivo ($v > 0$):* $[0, 1.30 \text{ s}) \cup (15.37 \text{ s}, \infty)$.
  * *Movimiento acelerado ($v \cdot a > 0$):* $(1.30 \text{ s}, 8.33 \text{ s}) \cup (15.37 \text{ s}, \infty)$.
  * *Análisis:* Discusión sobre ciclos de fatiga mecánica y estabilidad dinámica.

* **Ejercicio 4: Aplicación de la derivada – Optimización del corte del perfil de acero**
  * *Restricción de longitud:* $4x + 3y = 15$ metros (cuadrado de lado $x$ y triángulo equilátero de lado $y$).
  * *Función de área:* $A(x) = x^2 + \frac{\sqrt{3}}{36}(15 - 4x)^2$.
  * *Dimensión óptima:* $x = \frac{45\sqrt{3}-60}{11} \approx 1.631 \text{ m}$.
  * *Distribución del perfil:* **6.52 metros** asignados al marco cuadrado ($4x$) y **8.48 metros** a la estructura triangular ($15 - 4x$).
  * *Área mínima lograda:* $A_{\text{mín}} \approx 6.12 \text{ m}^2$ (confirmado con $A''(x) \approx 3.54 > 0$).

* **Ejercicio 5: Infografía académica en inglés**
  * *Evento:* International Academic Colloquium on Differential Calculus and Mathematical Modeling in Civil Engineering (ECBTI - UNAD).
  * *Componentes:* Title, Introduction, Key Ideas, Mathematical Connection, Personal Reflection, Academic Sources.
  * *Recurso interactivo:* [Enlace Canva / Genially](https://www.canva.com/design/unad-reto4-calculo-diana-rodriguez).

---

## 📂 Contenido del Repositorio
* `Reto_4_Calculo_Diferencial_Contexto_D_Diana_Rodriguez.pdf`: Documento final en formato APA 7.ª edición.
* `figures/`: Figuras vectoriales de alta resolución generadas para GeoGebra, Google Colab y la infografía en inglés.
* `generate_figures.py`: Script para reproducir las gráficas científicas.
* `build_pdf.py`: Script automatizado para la compilación del reporte en PDF.
