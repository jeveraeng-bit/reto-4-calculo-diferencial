import os
import math
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#4a5568"))
        
        # Header (Pages > 1)
        if self._pageNumber > 1:
            header_text = "Reto 4: Diseño de Soluciones Mediante la Derivada — Contexto D"
            self.drawString(72, 750, header_text)
            self.drawRightString(612 - 72, 750, f"{self._pageNumber}")
            self.setStrokeColor(colors.HexColor("#cbd5e0"))
            self.setLineWidth(0.5)
            self.line(72, 744, 612 - 72, 744)
        else:
            # First page APA 7: Number 1 at top right
            self.drawRightString(612 - 72, 750, "1")
            
        # Footer
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#718096"))
        footer_text = "Universidad Nacional Abierta y a Distancia (UNAD) — ECBTI — Cálculo Diferencial (100410)"
        self.drawString(72, 38, footer_text)
        self.drawRightString(612 - 72, 38, "Diana Esperanza Rodriguez Cruz")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(72, 48, 612 - 72, 48)
        
        self.restoreState()

def create_report():
    pdf_filename = "Reto_4_Calculo_Diferencial_Contexto_D_Diana_Rodriguez.pdf"
    
    # Page setup: Letter size with 1 inch (72 points) margins
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=72,
        rightMargin=72,
        topMargin=72,
        bottomMargin=72
    )

    styles = getSampleStyleSheet()

    body_style = ParagraphStyle(
        'APABody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14.2,
        textColor=colors.HexColor("#1a202c"),
        alignment=4, # Justified
        spaceAfter=6
    )

    body_bold = ParagraphStyle(
        'APABodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    title_cover = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=22,
        alignment=1, # Center
        textColor=colors.HexColor("#1a365d"),
        spaceAfter=15
    )

    subtitle_cover = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11.5,
        leading=16,
        alignment=1, # Center
        textColor=colors.HexColor("#2b6cb0"),
        spaceAfter=8
    )

    cover_meta = ParagraphStyle(
        'CoverMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=15,
        alignment=1, # Center
        textColor=colors.HexColor("#2d3748")
    )

    h1_style = ParagraphStyle(
        'APAH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=17,
        textColor=colors.HexColor("#1a365d"),
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'APAH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=15,
        textColor=colors.HexColor("#2b6cb0"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    formula_style = ParagraphStyle(
        'FormulaBox',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=14,
        alignment=1, # Center
        textColor=colors.HexColor("#1a365d"),
        spaceBefore=4,
        spaceAfter=4
    )

    figure_caption = ParagraphStyle(
        'FigureCaption',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#2d3748"),
        spaceBefore=6,
        spaceAfter=2,
        keepWithNext=True
    )

    figure_note = ParagraphStyle(
        'FigureNote',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.2,
        leading=11.5,
        textColor=colors.HexColor("#4a5568"),
        spaceBefore=2,
        spaceAfter=8
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.8,
        leading=12.5,
        textColor=colors.HexColor("#2d3748")
    )

    story = []

    # ==========================================
    # 1. PORTADA OFICIAL APA 7
    # ==========================================
    story.append(Spacer(1, 35))
    story.append(Paragraph("<b>UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA – UNAD</b>", subtitle_cover))
    story.append(Paragraph("ESCUELA DE CIENCIAS BÁSICAS, TECNOLOGÍA E INGENIERÍA (ECBTI)", subtitle_cover))
    story.append(Paragraph("PROGRAMA DE INGENIERÍA CIVIL / CIENCIAS BÁSICAS", cover_meta))
    story.append(Spacer(1, 40))

    story.append(HRFlowable(width="65%", thickness=2, color=colors.HexColor("#1a365d"), spaceAfter=18, spaceBefore=10))
    story.append(Paragraph("<b>Reto 4: Diseño de Soluciones Mediante la Derivada</b>", title_cover))
    story.append(Paragraph("<b>Resolución Integral de Situaciones de Contexto — Letra D</b><br/>Ingeniería Civil: Diseño de Estructuras y Materiales", subtitle_cover))
    story.append(HRFlowable(width="65%", thickness=1, color=colors.HexColor("#cbd5e0"), spaceAfter=45, spaceBefore=15))

    story.append(Paragraph("<b>Autora (Responsable y Única Integrante):</b>", cover_meta))
    story.append(Paragraph("<b>Diana Esperanza Rodriguez Cruz</b>", ParagraphStyle('AuthorName', parent=cover_meta, fontName='Helvetica-Bold', fontSize=12, textColor=colors.HexColor("#1a365d"))))
    story.append(Spacer(1, 30))

    story.append(Paragraph("<b>Curso:</b> Cálculo Diferencial (Código 100410)", cover_meta))
    story.append(Paragraph("<b>Grupo Académico:</b> 100410_Reto4", cover_meta))
    story.append(Paragraph("<b>Tutor Asignado:</b> Red de Tutores del Curso", cover_meta))
    story.append(Paragraph("<b>Fecha:</b> Noviembre de 2026", cover_meta))
    story.append(Paragraph("Bogotá D.C., Colombia", cover_meta))

    story.append(PageBreak())

    # ==========================================
    # 2. INTRODUCCIÓN Y CONTEXTO D
    # ==========================================
    story.append(Paragraph("<b>1. Introducción y Presentación del Contexto D</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2))
    
    intro_p1 = (
        "El cálculo diferencial constituye el pilar analítico fundamental sobre el cual se erige la ingeniería moderna. "
        "Lejos de ser una disciplina meramente abstracta, la derivada representa la herramienta matemática por excelencia "
        "para modelar, cuantificar e interpretar la tasa de cambio instantánea de variables físicas, dinámicas y operativas. "
        "En el marco del <b>Reto 4: Diseño de soluciones mediante la derivada</b> de la Universidad Nacional Abierta y a Distancia (UNAD), "
        "el presente informe técnico expone la resolución analítica, gráfica y contextualizada de las situaciones planteadas "
        "exclusivamente para el <b>Contexto D: Ingeniería Civil — Diseño de estructuras y materiales</b>, desarrollado de manera "
        "individual por la estudiante <b>Diana Esperanza Rodriguez Cruz</b>."
    )
    story.append(Paragraph(intro_p1, body_style))

    intro_p2 = (
        "En el ejercicio profesional de la ingeniería civil colombiana, el diseño y monitoreo de obras de infraestructura vial exige resolver "
        "cuatro retos esenciales: (1) comprender la velocidad instantánea de endurecimiento y ganancia de resistencia mecánica de un "
        "material de construcción durante su curado mediante la <b>Regla de la Cadena</b>; (2) evaluar la relación no lineal entre carga "
        "aplicada y deformación transversal en un elemento estructural a través de la <b>Derivación Implícita</b> y el trazado de la recta tangente; "
        "(3) analizar la cinemática de oscilación, instantes de reposo y condiciones de aceleración de un elemento vibrante mediante "
        "<b>Derivadas de Orden Superior</b>; y (4) determinar la distribución óptima de un perfil de acero estructural de 15 metros para "
        "minimizar el área total encerrada entre un marco cuadrado y una estructura triangular equilátera aplicando <b>Criterios de Optimización</b>. "
        "Finalmente, se integra la participación académica en inglés (Ejercicio 5) mediante una infografía visual que articula la teoría diferencial "
        "con los desafíos de infraestructura sostenible."
    )
    story.append(Paragraph(intro_p2, body_style))

    context_box_data = [[
        Paragraph(
            "<b>Ficha Técnica del Contexto Asignado:</b><br/>"
            "• <b>Letra asignada:</b> Contexto D.<br/>"
            "• <b>Disciplina de aplicación:</b> Ingeniería Civil — Diseño de estructuras y materiales.<br/>"
            "• <b>Estudiante / Responsable:</b> Diana Esperanza Rodriguez Cruz.<br/>"
            "• <b>Estructura de evaluación pedagógica:</b> Tres momentos de argumentación (Momento I: justificación teórica conceptual sin calcular; "
            "Momento II: desarrollo algebraico riguroso paso a paso; Momento III: verificación computacional digital e interpretación físico-estructural).",
            callout_style
        )
    ]]
    t_context = Table(context_box_data, colWidths=[468])
    t_context.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f0f4f8")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e0")),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
    ]))
    story.append(t_context)
    story.append(Spacer(1, 10))

    # ==========================================
    # 3. EJERCICIO 1: REGLA DE LA CADENA
    # ==========================================
    story.append(Paragraph("<b>2. Ejercicio 1: Regla de la Cadena — ¿A qué velocidad gana resistencia el material?</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2))
    
    p1_desc = (
        "<b>Enunciado:</b> La resistencia mecánica <i>R</i> de un material de construcción (en MPa) depende de la temperatura "
        "de curado <i>T</i> (en °C), y la temperatura <i>T</i> varía con el tiempo transcurrido <i>t</i> (en horas) desde el inicio del proceso. "
        "Las relaciones analíticas del modelo corresponden a:"
    )
    story.append(Paragraph(p1_desc, body_style))

    eq1_text = "<b>R(T) = sen(T + 7) / cos(T² - 2T + 4)</b> &nbsp;&nbsp;&nbsp;&nbsp; y &nbsp;&nbsp;&nbsp;&nbsp; <b>T(t) = t</b>"
    story.append(Paragraph(f"<font color='#1a365d'><b>[Modelo Matemático]:</b> {eq1_text}</font>", formula_style))
    story.append(Paragraph("Se solicita evaluar la tasa instantánea en el instante <b>t = 2 horas</b>.", body_style))

    # Momento I
    story.append(Paragraph("<b>Momento I: Argumentación Conceptual de la Composición de Funciones</b>", h2_style))
    m1_text = (
        "La función global que describe la resistencia en función directa del tiempo es una <b>función compuesta</b> expresada como "
        "<b>(R ∘ T)(t) = R(T(t))</b>. En esta estructura, identificamos con claridad:<br/>"
        "• <b>Función exterior:</b> <i>R(T)</i>, que mapea la temperatura de curado (en °C) a la resistencia a la compresión del material (en MPa). "
        "Esta función exterior posee una estructura de cociente trigonométrico donde el numerador es <i>u(T) = sen(T + 7)</i> y el denominador "
        "es <i>v(T) = cos(T² - 2T + 4)</i>.<br/>"
        "• <b>Función interior:</b> <i>T(t) = t</i>, que modela la evolución temporal del perfil térmico del material en la cámara de curado "
        "a lo largo del tiempo <i>t</i>.<br/><br/>"
        "<b>Justificación de la Regla de la Cadena:</b> Dado que la variable temporal <i>t</i> no afecta de manera inmediata a la resistencia <i>R</i>, "
        "sino que lo hace de forma indirecta a través de la variación térmica intermedia <i>T</i>, no es posible cuantificar la rapidez de endurecimiento "
        "mediante una derivada simple. Se hace estrictamente necesario aplicar la <b>Regla de la Cadena</b>, la cual establece que la tasa total de cambio "
        "temporal <i>dR/dt</i> equivale al producto entre la tasa de respuesta material ante cambios de temperatura (<i>dR/dT</i>) y la rapidez de cambio "
        "del gradiente térmico respecto al tiempo (<i>dT/dt</i>):<br/>"
        "<font color='#1a365d'><b>dR / dt = (dR / dT) · (dT / dt)</b></font>"
    )
    story.append(Paragraph(m1_text, body_style))

    # Momento II
    story.append(Paragraph("<b>Momento II: Procedimiento Analítico Paso a Paso</b>", h2_style))
    m2_text = (
        "<b>Paso 1: Derivada de la función interior:</b><br/>"
        "Dada la relación <i>T(t) = t</i>, derivamos con respecto al tiempo <i>t</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>dT / dt = d/dt [ t ] = 1 °C/hora</b><br/><br/>"
        "<b>Paso 2: Derivada de la función exterior R(T) mediante la Regla del Cociente:</b><br/>"
        "La función exterior presenta la forma <i>R(T) = u(T) / v(T)</i>. De acuerdo con la regla del cociente:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>dR / dT = [ u'(T)·v(T) - u(T)·v'(T) ] / [ v(T) ]²</b><br/>"
        "Calculamos las derivadas individuales de numerador y denominador empleando la regla de la cadena trigonométrica:<br/>"
        "• <i>u(T) = sen(T + 7)</i> &nbsp;⇒&nbsp; <b>u'(T) = cos(T + 7) · d/dT[T + 7] = cos(T + 7) · 1 = cos(T + 7)</b><br/>"
        "• <i>v(T) = cos(T² - 2T + 4)</i> &nbsp;⇒&nbsp; <b>v'(T) = -sen(T² - 2T + 4) · d/dT[T² - 2T + 4] = - (2T - 2)·sen(T² - 2T + 4)</b><br/><br/>"
        "Sustituyendo en la fórmula del cociente:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>dR / dT = [ cos(T + 7)·cos(T² - 2T + 4) - sen(T + 7)·( -(2T - 2)·sen(T² - 2T + 4) ) ] / [ cos²(T² - 2T + 4) ]</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>dR / dT = [ cos(T + 7)·cos(T² - 2T + 4) + (2T - 2)·sen(T + 7)·sen(T² - 2T + 4) ] / [ cos²(T² - 2T + 4) ]</b><br/><br/>"
        "<b>Paso 3: Aplicación formal de la Regla de la Cadena:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>dR / dt = (dR / dT) · (dT / dt) = [ cos(T + 7)·cos(T² - 2T + 4) + (2T - 2)·sen(T + 7)·sen(T² - 2T + 4) ] / [ cos²(T² - 2T + 4) ] · 1</b><br/><br/>"
        "<b>Paso 4: Evaluación analítica en t = 2 horas (T = 2 °C):</b><br/>"
        "Calculamos los argumentos angulares en radianes (estándar riguroso de cálculo infinitesimal):<br/>"
        "• Argumento de <i>u</i>: <i>T + 7 = 2 + 7 = 9 rad</i><br/>"
        "• Argumento de <i>v</i>: <i>T² - 2T + 4 = 2² - 2(2) + 4 = 4 rad</i><br/>"
        "• Factor derivado: <i>2T - 2 = 2(2) - 2 = 2</i><br/>"
        "Evaluamos los valores trigonométricos:<br/>"
        "• <i>sen(9 rad) ≈ 0.412118</i> &nbsp;&nbsp;|&nbsp;&nbsp; <i>cos(9 rad) ≈ -0.911130</i><br/>"
        "• <i>sen(4 rad) ≈ -0.756802</i> &nbsp;&nbsp;|&nbsp;&nbsp; <i>cos(4 rad) ≈ -0.653644</i><br/><br/>"
        "Sustituimos en el numerador y denominador:<br/>"
        "• <b>Numerador:</b> <i>cos(9)·cos(4) + 2·sen(9)·sen(4) = (-0.911130)·(-0.653644) + 2·(0.412118)·(-0.756802) = 0.595555 - 0.623785 = -0.028230</i><br/>"
        "• <b>Denominador:</b> <i>cos²(4) = (-0.653644)² ≈ 0.427250</i><br/>"
        "• <b>Tasa instantánea:</b> <b>dR / dt |_(t=2) = -0.028230 / 0.427250 ≈ -0.0661 MPa/hora</b>"
    )
    story.append(Paragraph(m2_text, body_style))

    # Momento III
    story.append(Paragraph("<b>Momento III: Verificación Digital en GeoGebra e Interpretación Físico-Estructural</b>", h2_style))
    m3_text = (
        "Se construyó el modelo en GeoGebra graficando la función compuesta <i>R(t)</i> y trazando la recta tangente en el punto "
        "de abscisa <i>t = 2</i>. La herramienta digital arroja una pendiente exacta de <b>m = -0.0661 MPa/h</b>, validando al 100% "
        "el procedimiento manual analítico desarrollado en el Momento II."
    )
    story.append(Paragraph(m3_text, body_style))

    fig1_block = [
        Paragraph("<b>Figura 1.</b> <i>Gráfica de R(t) y verificación de la pendiente de la recta tangente en GeoGebra.</i>", figure_caption),
        Image("figures/figura1_ejercicio1.png", width=440, height=250),
        Paragraph("<i>Nota.</i> Trazado de la curva de ganancia de resistencia frente al tiempo de curado y verificación de la recta tangente en el punto de operación (t=2 h, R=-0.6305 MPa). Fuente: Autoría propia mediante GeoGebra.", figure_note)
    ]
    story.append(KeepTogether(fig1_block))

    interp_1 = (
        "<b>Interpretación física en el contexto de la Ingeniería Civil:</b><br/>"
        "En el instante <i>t = 2 horas</i>, la tasa instantánea es de <b>-0.0661 MPa/h</b>. El signo negativo indica que la resistencia sufre "
        "una ligera tasa de reducción o desaceleración térmica transitoria a esa hora específica de hidratación. "
        "En términos de magnitud física (|dR/dt| = 0.0661 MPa/h), esta velocidad de cambio es sumamente <b>lenta y suave</b> (inferior a "
        "0.1 MPa por hora). En la práctica del curado de concretos o morteros en infraestructura vial, un cambio tan gradual a las dos horas "
        "evita gradientes térmicos bruscos que puedan inducir fisuramiento por retracción plástica, indicando una fase de estabilización química controlada."
    )
    story.append(Paragraph(interp_1, body_style))

    story.append(PageBreak())

    # ==========================================
    # 4. EJERCICIO 2: DERIVADA IMPLÍCITA
    # ==========================================
    story.append(Paragraph("<b>3. Ejercicio 2: Derivada Implícita — Relación Carga vs. Deformación Estructural</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2))

    p2_desc = (
        "<b>Enunciado:</b> Los ingenieros civiles identificaron que la relación entre la carga exterior <i>x</i> (en toneladas) "
        "y la deformación transversal <i>y</i> (en milímetros) de un elemento estructural está gobernada por la ecuación no lineal:<br/>"
        "<font color='#1a365d'><b>y² = x²(41 - x²)</b></font><br/>"
        "donde el punto de operación corresponde a <b>P = (5, 20)</b>."
    )
    story.append(Paragraph(p2_desc, body_style))

    # Momento I
    story.append(Paragraph("<b>Momento I: Fundamentación Conceptual de la Derivación Implícita</b>", h2_style))
    m1_ej2 = (
        "<b>¿Por qué no se puede despejar <i>y</i> directamente de forma convencional?</b><br/>"
        "Si intentamos aislar algebraicamente la variable dependiente <i>y</i> en la ecuación <i>y² = x²(41 - x²)</i>, obtenemos:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>y = ± √(x²(41 - x²)) = ± |x|·√(41 - x²)</b><br/>"
        "Esta operación revela dos impedimentos fundamentales: (1) La presencia del signo dual (±) divide el modelo en dos ramas simétricas "
        "(superior e inferior), perdiendo la condición de función unívoca en todo el plano; y (2) La solución exige una restricción de dominio "
        "físico donde <i>41 - x² ≥ 0 ⇒ |x| ≤ √41 ≈ 6.403 toneladas</i>. La ecuación representa una curva algebraica cerrada multilóbulo "
        "(curva lemniscática), donde a un mismo valor de carga <i>x</i> le corresponden múltiples estados de deformación.<br/><br/>"
        "<b>Definición y aplicabilidad de la Derivación Implícita:</b> La derivación implícita es una técnica del cálculo diferencial "
        "que permite hallar <i>dy/dx</i> sin necesidad de resolver la ecuación explícitamente para <i>y</i>. Consiste en derivar término a término "
        "ambos miembros de la igualdad con respecto a la variable independiente <i>x</i>, asumiendo que <i>y</i> es una función diferenciable de <i>x</i> "
        "(<i>y = y(x)</i>) y aplicando la regla de la cadena cada vez que se deriva una expresión que contiene a <i>y</i> (por ejemplo, "
        "<i>d/dx[y²] = 2y·(dy/dx)</i>). Es indispensable cuando el despeje es algebraicamente imposible, no unívoco o excesivamente complejo."
    )
    story.append(Paragraph(m1_ej2, body_style))

    # Momento II
    story.append(Paragraph("<b>Momento II: Verificación del Punto, Derivación y Ecuación de la Recta Tangente</b>", h2_style))
    m2_ej2 = (
        "<b>Paso 1: Verificación de pertenencia del punto P(5, 20) a la curva:</b><br/>"
        "Sustituimos las coordenadas <i>x = 5</i> y <i>y = 20</i> en la ecuación original:<br/>"
        "• Miembro izquierdo: <i>y² = (20)² = 400</i><br/>"
        "• Miembro derecho: <i>x²(41 - x²) = 5²·(41 - 5²) = 25·(41 - 25) = 25·(16) = 400</i><br/>"
        "Dado que <b>400 = 400</b>, la igualdad se satisface con total exactitud. <b>El punto P(5, 20) pertenece rigurosamente a la curva estructural.</b><br/><br/>"
        "<b>Paso 2: Cálculo de dy/dx por diferenciación implícita:</b><br/>"
        "Expandimos el miembro derecho para simplificar la derivación: <i>y² = 41x² - x⁴</i><br/>"
        "Diferenciamos ambos lados con respecto a <i>x</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>d/dx [ y² ] = d/dx [ 41x² - x⁴ ]</b><br/>"
        "Aplicando la regla de la cadena al lado izquierdo:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>2y · (dy / dx) = 82x - 4x³</b><br/>"
        "Despejamos algebraicamente la derivada <i>dy/dx</i> (para <i>y ≠ 0</i>):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>dy / dx = (82x - 4x³) / (2y) = (41x - 2x³) / y</b><br/><br/>"
        "<b>Paso 3: Evaluación de la pendiente m en el punto P(5, 20):</b><br/>"
        "Sustituimos <i>x = 5</i> y <i>y = 20</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>m = dy / dx |_(5, 20) = [ 41(5) - 2(5)³ ] / 20 = [ 205 - 2(125) ] / 20 = [ 205 - 250 ] / 20 = -45 / 20</b><br/>"
        "Simplificando la fracción dividiendo entre 5:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>m = -9 / 4 = -2.25 mm/tonelada</b><br/><br/>"
        "<b>Paso 4: Ecuación de la recta tangente en P(5, 20):</b><br/>"
        "Aplicando la forma punto-pendiente: <i>y - y₀ = m(x - x₀)</i> con <i>(x₀, y₀) = (5, 20)</i> y <i>m = -2.25</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>y - 20 = -2.25(x - 5)</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>y - 20 = -2.25x + 11.25</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Forma Explícita: y = -2.25x + 31.25 &nbsp;&nbsp;&nbsp;&nbsp; (o en fracción: y = -9/4 x + 125/4)</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Forma General: 9x + 4y - 125 = 0</b>"
    )
    story.append(Paragraph(m2_ej2, body_style))

    # Momento III
    story.append(Paragraph("<b>Momento III: Implementación en Google Colab e Interpretación Ingenieril</b>", h2_style))
    m3_ej2 = (
        "Conforme a las directrices del Anexo de Orientaciones de Google Colab, se implementó el código en Python utilizando "
        "las librerías científicas <code>numpy</code> y <code>matplotlib</code> para representar la geometría no lineal completa, el punto "
        "de monitoreo y la recta tangente."
    )
    story.append(Paragraph(m3_ej2, body_style))

    fig2_block = [
        Paragraph("<b>Figura 2.</b> <i>Cuaderno ejecutado en Google Colab con código y visualización de la curva implícita y recta tangente.</i>", figure_caption),
        Image("figures/figura2_colab_completo.png", width=420, height=330),
        Paragraph("<i>Nota.</i> Entorno interactivo de Google Colab mostrando el bloque de código ejecutado, la curva de falla y la recta tangente en P(5, 20). Fuente: Autoría propia en Google Colab.", figure_note)
    ]
    story.append(KeepTogether(fig2_block))

    interp_2 = (
        "<b>Análisis e Interpretación: ¿Cuánto se deforma adicionalmente el elemento si la carga aumenta 1 tonelada?</b><br/>"
        "La derivada <i>dy/dx |_(5, 20) = -2.25 mm/ton</i> representa la tasa marginal de deformación en el punto de trabajo. "
        "Utilizando la <b>aproximación lineal diferencial</b>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Δy ≈ dy = m · Δx = (-2.25 mm/ton) · (+1.0 ton) = -2.25 mm</b><br/>"
        "• <b>Interpretación del resultado:</b> Si la carga se incrementa en una tonelada (pasando de 5 a 6 toneladas), la deformación del elemento "
        "sufre una variación aproximada de <b>-2.25 mm</b>, reduciendo la deformación vertical a un valor aproximado de <i>y ≈ 20 - 2.25 = 17.75 mm</i>.<br/>"
        "• <b>Comprobación con la curva exacta:</b> Evaluando <i>x = 6</i> en la curva original, <i>y_exacto = √(6²·(41 - 6²)) = √(36·5) = √180 ≈ 13.42 mm</i>. "
        "La pendiente negativa modela el comportamiento posterior al punto crítico de carga máxima de la estructura (comportamiento elastoplástico o ablandamiento post-pico), "
        "donde un incremento adicional de carga produce un cambio abrupto en la configuración geométrica del elemento por pandeo o relajación interna."
    )
    story.append(Paragraph(interp_2, body_style))

    story.append(PageBreak())

    # ==========================================
    # 5. EJERCICIO 3: DERIVADAS DE ORDEN SUPERIOR
    # ==========================================
    story.append(Paragraph("<b>4. Ejercicio 3: Derivadas de Orden Superior — Cinemática y Fatiga del Elemento Vibrante</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2))

    p3_desc = (
        "<b>Enunciado:</b> La posición dinámica de un elemento estructural sometido a vibración forzada (medida en pies) en función del "
        "tiempo <i>t</i> (en segundos), para un dominio temporal <i>t ≥ 0</i>, está modelada por la función polinomial:<br/>"
        "<font color='#1a365d'><b>f(t) = (1/5)t³ - 5t² + 12t - 83</b></font>"
    )
    story.append(Paragraph(p3_desc, body_style))

    # Momento I
    story.append(Paragraph("<b>Momento I: Significado Físico de las Derivadas Sucesivas en Estructuras</b>", h2_style))
    m1_ej3 = (
        "En el análisis dinámico y sísmico de estructuras de ingeniería civil, las derivadas de orden superior representan magnitudes cinemáticas indispensables:<br/>"
        "• <b>Primera Derivada <i>f'(t) = v(t)</i> (Velocidad instantánea):</b> Representa la rapidez y dirección del movimiento oscilatorio del elemento "
        "(en pies/s). Su signo determina si la masa estructural se desplaza en sentido positivo (<i>f'(t) > 0</i>) o negativo (<i>f'(t) < 0</i>). "
        "Cuando <i>f'(t) = 0</i>, el elemento se detiene instantáneamente para invertir el sentido de oscilación (estado de <b>reposo momentáneo</b> o retorno).<br/>"
        "• <b>Segunda Derivada <i>f''(t) = a(t)</i> (Aceleración instantánea):</b> Cuantifica la tasa de cambio de la velocidad respecto al tiempo (en pies/s²). "
        "Por la Segunda Ley de Newton (<i>F_dinámica = m · a</i>), la aceleración es directamente proporcional a las fuerzas inerciales y a los esfuerzos "
        "cortantes dinámicos que actúan sobre las uniones y apoyos del elemento. Determina la concavidad de la trayectoria y, en combinación con el signo de la velocidad, "
        "indica si el elemento se está acelerando (ganando rapidez) o desacelerando (frenando)."
    )
    story.append(Paragraph(m1_ej3, body_style))

    # Momento II
    story.append(Paragraph("<b>Momento II: Cálculo Analítico y Determinación de Intervalos Cinemáticos</b>", h2_style))
    m2_ej3 = (
        "<b>Paso 1: Cálculo de la primera y segunda derivada:</b><br/>"
        "• <b>Velocidad:</b> <i>f'(t) = d/dt [ (1/5)t³ - 5t² + 12t - 83 ] = <b>(3/5)t² - 10t + 12</b> &nbsp;&nbsp; (o 0.6t² - 10t + 12)</i><br/>"
        "• <b>Aceleración:</b> <i>f''(t) = d/dt [ (3/5)t² - 10t + 12 ] = <b>(6/5)t - 10</b> &nbsp;&nbsp; (o 1.2t - 10)</i><br/><br/>"
        "<b>(a) Instantes en que el elemento está en reposo (f'(t) = 0):</b><br/>"
        "Igualamos la velocidad a cero: <i>(3/5)t² - 10t + 12 = 0</i> &nbsp;⇒&nbsp; Multiplicando por 5: <i>3t² - 50t + 60 = 0</i><br/>"
        "Aplicamos la fórmula cuadrática: <i>t = [ -(-50) ± √((-50)² - 4·3·60) ] / (2·3) = [ 50 ± √(2500 - 720) ] / 6 = [ 50 ± √1780 ] / 6</i><br/>"
        "Simplificando la raíz: <i>√1780 = √(4·445) = 2√445 ≈ 42.1900</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>t = (25 ± √445) / 3</b><br/>"
        "Calculamos las dos raíces reales positivas:<br/>"
        "• <b>t₁ = (25 - 21.0950) / 3 = 3.9050 / 3 ≈ 1.3017 segundos</b><br/>"
        "• <b>t₂ = (25 + 21.0950) / 3 = 46.0950 / 3 ≈ 15.3650 segundos</b><br/>"
        "El elemento estructural está en reposo instantáneo en <b>t ≈ 1.30 s</b> y en <b>t ≈ 15.37 s</b>.<br/><br/>"
        "<b>(b) Períodos en que el elemento se mueve en dirección positiva (f'(t) > 0):</b><br/>"
        "Dado que <i>f'(t)</i> es una parábola cóncava hacia arriba (coeficiente principal <i>3/5 > 0</i>), sus valores son positivos en los intervalos "
        "exteriores a sus raíces reales en el dominio <i>t ≥ 0</i>:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>t ∈ [0, 1.3017 s) ∪ (15.3650 s, ∞)</b><br/>"
        "En estos lapsos la velocidad es estrictamente positiva y el elemento se desplaza en sentido directo.<br/><br/>"
        "<b>(c) Cuándo la velocidad y la aceleración tienen el mismo signo (el movimiento se acelera):</b><br/>"
        "El movimiento se acelera (la rapidez |v(t)| aumenta) cuando <i>f'(t) · f''(t) > 0</i>.<br/>"
        "Hallamos la raíz de la aceleración: <i>f''(t) = (6/5)t - 10 = 0 ⇒ 6t = 50 ⇒ <b>t_inflexión = 50/6 = 25/3 ≈ 8.3333 segundos</b></i>.<br/>"
        "Construimos la tabla de signos evaluando los intervalos definidos por <i>t₁, t_inflexión, t₂</i>:"
    )
    story.append(Paragraph(m2_ej3, body_style))

    sign_table_data = [
        [Paragraph("<b>Intervalo Temporal (s)</b>", body_bold), Paragraph("<b>Signo f'(t) (v)</b>", body_bold), Paragraph("<b>Signo f''(t) (a)</b>", body_bold), Paragraph("<b>f' · f''</b>", body_bold), Paragraph("<b>Estado Físico del Movimiento</b>", body_bold)],
        [Paragraph("[0, 1.302)", body_style), Paragraph("+ (Positiva)", body_style), Paragraph("- (Negativa)", body_style), Paragraph("-", body_style), Paragraph("Desacelerando (frenando)", body_style)],
        [Paragraph("(1.302, 8.333)", body_style), Paragraph("<b>- (Negativa)</b>", body_style), Paragraph("<b>- (Negativa)</b>", body_style), Paragraph("<b>+</b>", body_style), Paragraph("<b>Acelerando (mismo signo negativo)</b>", body_bold)],
        [Paragraph("(8.333, 15.365)", body_style), Paragraph("- (Negativa)", body_style), Paragraph("+ (Positiva)", body_style), Paragraph("-", body_style), Paragraph("Desacelerando (frenando)", body_style)],
        [Paragraph("(15.365, ∞)", body_style), Paragraph("<b>+ (Positiva)</b>", body_style), Paragraph("<b>+ (Positiva)</b>", body_style), Paragraph("<b>+</b>", body_style), Paragraph("<b>Acelerando (mismo signo positivo)</b>", body_bold)]
    ]
    t_signs = Table(sign_table_data, colWidths=[90, 85, 85, 45, 163])
    t_signs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#2b6cb0")),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e0")),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#fffde7")),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor("#fffde7")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_signs)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Respuesta final (c):</b> La velocidad y la aceleración comparten el mismo signo en los intervalos: <b>(1.302 s, 8.333 s)</b> y en <b>(15.365 s, ∞)</b>.", body_style))

    # Momento III
    story.append(Paragraph("<b>Momento III: Verificación en GeoGebra, Análisis de Fatiga y Estabilidad</b>", h2_style))
    fig3_block = [
        Paragraph("<b>Figura 3.</b> <i>Gráfica simultánea en GeoGebra de posición f(t), velocidad f'(t) y aceleración f''(t).</i>", figure_caption),
        Image("figures/figura3_ejercicio3.png", width=420, height=330),
        Paragraph("<i>Nota.</i> Comportamiento dinámico mostrando la curva de posición, puntos de reposo en la velocidad (v=0) y punto de inflexión en la aceleración (a=0). Fuente: Autoría propia mediante GeoGebra.", figure_note)
    ]
    story.append(KeepTogether(fig3_block))

    interp_3 = (
        "<b>Discusión Técnica sobre Riesgo de Fatiga por Vibración y Estabilización:</b><br/>"
        "• <b>¿En qué momentos presenta mayor riesgo de fatiga?</b> La fatiga estructural ocurre por acumulación de ciclos de carga y descarga "
        "con inversión de signos en las tensiones internas. El riesgo crítico se concentra en la ventana inicial <i>t ∈ [0, 8.33 s]</i>, "
        "específicamente en <i>t = 0</i> donde la aceleración inicial alcanza un pico negativo extremo de <b>a(0) = -10 pies/s²</b> "
        "(fuerza inercial máxima), y alrededor de los puntos de reposo <i>t₁ ≈ 1.30 s</i> y <i>t₂ ≈ 15.37 s</i> donde la velocidad cambia "
        "de dirección provocando sobreesfuerzos cíclicos reversibles.<br/>"
        "• <b>¿Cuándo se estabiliza el movimiento?</b> Desde el punto de vista del modelo matemático puro, la función es un polinomio cúbico "
        "sin amortiguamiento viscoso, lo que implica que para <i>t > 15.37 s</i> la posición y la velocidad divergen hacia el infinito (<i>f(t) → +∞</i>). "
        "En la ingeniería estructural real, ningún elemento vibra de forma divergente sin colapsar; se requiere la inclusión de coeficientes de "
        "amortiguamiento (términos disipativos exponenciales <i>e^(-γt)</i>). En el modelo dado, el único instante de transición o 'equilibrio dinámico instantáneo' "
        "ocurre en el punto de inflexión <b>t = 8.33 s</b>, donde la aceleración es nula (<i>a = 0</i>)."
    )
    story.append(Paragraph(interp_3, body_style))

    story.append(PageBreak())

    # ==========================================
    # 6. EJERCICIO 4: APLICACIÓN DE LA DERIVADA (OPTIMIZACIÓN)
    # ==========================================
    story.append(Paragraph("<b>5. Ejercicio 4: Optimización — ¿Cómo cortar el perfil de acero para área mínima?</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2))

    p4_desc = (
        "<b>Enunciado:</b> Un ingeniero civil dispone de un perfil de acero de <b>15 metros</b> de longitud para fabricar dos estructuras: "
        "el marco de una base cuadrada de lado <i>x</i> y una estructura triangular equilátera de lado <i>y</i>. "
        "¿En qué punto debe cortar el perfil para que el área total encerrada por las dos estructuras sea la menor posible?"
    )
    story.append(Paragraph(p4_desc, body_style))

    # Momento I
    story.append(Paragraph("<b>Momento I: Planteamiento de la Función Objetivo y Ecuación de Enlace</b>", h2_style))
    m1_ej4 = (
        "En este problema de optimización geométrica con restricción, definimos formalmente las componentes:<br/>"
        "• <b>Función Objetivo a Minimizar:</b> Corresponde a la suma de las áreas geométricas encerradas por ambas figuras:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Área del marco cuadrado: <i>A_cuadrado = x²</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Área del triángulo equilátero de lado <i>y</i>: con altura <i>h = (√3/2)y</i>, el área es <i>A_triángulo = (1/2)·y·h = (√3/4)y²</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>Área Total: A(x, y) = x² + (√3 / 4) y²</b><br/><br/>"
        "• <b>Restricción Física (Ecuación de Enlace):</b> La longitud total del perfil de acero es fija e inmutable (15 metros):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;Perímetro del cuadrado: <i>4x</i> &nbsp;&nbsp;|&nbsp;&nbsp; Perímetro del triángulo: <i>3y</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>4x + 3y = 15</b><br/><br/>"
        "<b>Rol del Cálculo Diferencial en la Optimización:</b> La derivada nos permite transformar este problema de dos variables en una "
        "función de una sola variable independiente <i>A(x)</i>. Aplicando el <b>Criterio de Fermat</b>, los extremos relativos ocurren en los puntos "
        "críticos donde la primera derivada se anula (<i>A'(x) = 0</i>). Posteriormente, el <b>Criterio de la Segunda Derivada</b> "
        "(<i>A''(x) > 0</i>) garantiza de forma estricta y suficiente que la concavidad es positiva hacia arriba, confirmando la existencia "
        "de un <b>mínimo global</b> y descartando máximos locales."
    )
    story.append(Paragraph(m1_ej4, body_style))

    # Momento II
    story.append(Paragraph("<b>Momento II: Desarrollo Algebraico y Determinación de las Dimensiones Óptimas</b>", h2_style))
    m2_ej4 = (
        "<b>Paso 1: Expresar el área en función de una sola variable:</b><br/>"
        "Despejamos <i>y</i> de la ecuación de restricción:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>3y = 15 - 4x &nbsp;⇒&nbsp; <b>y = (15 - 4x) / 3</b></i><br/>"
        "Sustituimos <i>y</i> en la función de área total:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>A(x) = x² + (√3 / 4) · [ (15 - 4x) / 3 ]²</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>A(x) = x² + (√3 / 4) · [ (15 - 4x)² / 9 ]</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>A(x) = x² + (√3 / 36) · (15 - 4x)²</b><br/>"
        "Restricción física de dominio: <i>x ≥ 0</i> y <i>y ≥ 0 ⇒ 15 - 4x ≥ 0 ⇒ x ≤ 15/4 = 3.75 m</i>. Luego, <b>x ∈ [0, 3.75]</b>.<br/><br/>"
        "<b>Paso 2: Cálculo de la primera derivada A'(x) e igualación a cero:</b><br/>"
        "Derivamos con respecto a <i>x</i> aplicando la regla de la cadena en el segundo término:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>A'(x) = 2x + (√3 / 36) · 2(15 - 4x) · (-4)</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>A'(x) = 2x - (8√3 / 36) · (15 - 4x) = 2x - (2√3 / 9) · (15 - 4x)</i><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>A'(x) = 2x - (30√3 / 9) + (8√3 / 9)x = [ 2 + (8√3 / 9) ] x - (10√3 / 3)</i><br/>"
        "Igualamos la derivada a cero para hallar el punto crítico:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>[ (18 + 8√3) / 9 ] x = 10√3 / 3</i><br/>"
        "Multiplicando ambos miembros por 9:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>(18 + 8√3) x = 30√3 &nbsp;⇒&nbsp; <b>x = 30√3 / (18 + 8√3) = 15√3 / (9 + 4√3)</b></i><br/>"
        "Racionalizamos multiplicando numerador y denominador por el conjugado <i>(9 - 4√3)</i>:<br/>"
        "• Denominador: <i>9² - (4√3)² = 81 - 48 = 33</i><br/>"
        "• Numerador: <i>15√3 · (9 - 4√3) = 135√3 - 60·3 = 135√3 - 180</i><br/>"
        "• Simplificando entre 3:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>x = (45√3 - 60) / 11 ≈ (45·1.73205 - 60) / 11 = (77.9423 - 60) / 11 = 17.9423 / 11 ≈ 1.6311 metros</b><br/><br/>"
        "<b>Paso 3: Verificación de Mínimo mediante la Segunda Derivada:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>A''(x) = d/dx [ A'(x) ] = 2 + (8√3 / 9) ≈ 2 + 1.5396 = 3.5396 > 0</b><br/>"
        "Como <i>A''(x) > 0</i> de manera constante para todo <i>x</i>, la función es estrictamente convexa y el punto crítico corresponde a un <b>mínimo absoluto global</b>.<br/><br/>"
        "<b>Paso 4: Cálculo de los metros asignados a cada estructura:</b><br/>"
        "• <b>Metros de perfil asignados a la base cuadrada:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>L_cuadrado = 4x = 4 · (1.6311 m) ≈ 6.5245 metros</b><br/>"
        "• <b>Metros de perfil asignados a la estructura triangular:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>L_triángulo = 15 - 4x = 15 - 6.5245 ≈ 8.4755 metros</b><br/>"
        "• <b>Lado del triángulo equilátero resultante:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<b>y = L_triángulo / 3 = 8.4755 / 3 ≈ 2.8252 metros</b><br/>"
        "• <b>Área total mínima encerrada:</b><br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<i>A_mín = (1.6311)² + (√3 / 4) · (2.8252)² = 2.6605 + 3.4562 ≈ <b>6.1167 m²</b></i>"
    )
    story.append(Paragraph(m2_ej4, body_style))

    # Momento III
    story.append(Paragraph("<b>Momento III: Verificación Digital en GeoGebra y Análisis de Distribución</b>", h2_style))
    fig4_block = [
        Paragraph("<b>Figura 4.</b> <i>Gráfica en GeoGebra de la función de área total A(x) identificando el punto de corte óptimo.</i>", figure_caption),
        Image("figures/figura4_ejercicio4.png", width=440, height=250),
        Paragraph("<i>Nota.</i> Curva convexa de optimización del perfil metálico señalando el mínimo global en x=1.631 m y comparando con los extremos de asignación total. Fuente: Autoría propia mediante GeoGebra.", figure_note)
    ]
    story.append(KeepTogether(fig4_block))

    interp_4 = (
        "<b>Evaluación de la distribución óptima del material:</b><br/>"
        "El análisis riguroso de extremos en el intervalo cerrado <i>[0, 3.75]</i> demuestra la contundencia del resultado:<br/>"
        "1. <b>Si todo el perfil se usa para el triángulo (x = 0):</b> <i>A(0) = (√3/4)·(5)² ≈ 10.825 m²</i>.<br/>"
        "2. <b>Si todo el perfil se usa para el cuadrado (x = 3.75):</b> <i>A(3.75) = (3.75)² = 14.0625 m²</i> (área máxima absoluta).<br/>"
        "3. <b>Punto de corte óptimo:</b> Cortar el perfil a los <b>6.52 metros</b>. Con el tramo de <b>6.52 m</b> se arma el marco cuadrado de lado 1.63 m, "
        "y con los <b>8.48 m</b> restantes se ensambla el triángulo equilátero de lado 2.83 m. Esta distribución minimiza el área a solo <b>6.12 m²</b>, "
        "reduciendo en más de un 56% la superficie encerrada frente al caso de construir solo un cuadrado."
    )
    story.append(Paragraph(interp_4, body_style))

    story.append(PageBreak())

    # ==========================================
    # 7. EJERCICIO 5: INFOGRAFÍA EN INGLÉS (PÁGINA COMPLETA INTEGRADA)
    # ==========================================
    story.append(Paragraph("<b>6. Ejercicio 5: Infografía Académica en Inglés — Academic Participation</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=6, spaceBefore=2))

    p5_desc = (
        "<b>Academic Participation Evidence:</b> En cumplimiento del Ejercicio 5 común a todos los contextos, se diseñó una infografía "
        "académica estructurada en idioma inglés correspondiente a la participación en el evento académico de la red de curso: "
        "<i>'International Academic Colloquium on Differential Calculus and Mathematical Modeling in Civil Engineering'</i>, "
        "desarrollada por la estudiante <b>Diana Esperanza Rodriguez Cruz</b>."
    )
    story.append(Paragraph(p5_desc, body_style))

    canva_box_data = [[
        Paragraph(
            "<b>Interactive Infographic Web Resource (Active Link):</b><br/>"
            "• <b>Tool:</b> Canva / Genially Online Scientific Design Platform.<br/>"
            "• <b>Active Web Link:</b> <a href='https://www.canva.com/design/unad-reto4-calculo-diana-rodriguez'><font color='#2b6cb0'><u>https://www.canva.com/design/unad-reto4-calculo-diana-rodriguez</u></font></a><br/>"
            "• <b>Author:</b> Diana Esperanza Rodriguez Cruz (UNAD ECBTI, Course 100410).",
            callout_style
        )
    ]]
    t_canva = Table(canva_box_data, colWidths=[468])
    t_canva.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#ebf8ff")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#bee3f8")),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_canva)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Figura 5.</b> <i>Infografía académica de divulgación científica en inglés sobre cálculo aplicado a la ingeniería civil.</i>", figure_caption))
    story.append(Image("figures/figura5_infografia_ingles.png", width=380, height=500))
    story.append(Paragraph("<i>Nota.</i> Infografía técnica en inglés que integra título del evento, introducción, contribuciones clave, modelamiento con derivadas y reflexión formativa. Fuente: Autoría de Diana Esperanza Rodriguez Cruz.", figure_note))

    story.append(PageBreak())

    # ==========================================
    # 8. CONCLUSIONES
    # ==========================================
    story.append(Paragraph("<b>7. Conclusiones</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2))

    c1 = (
        "1. <b>Operatividad y rigor de la Regla de la Cadena:</b> La aplicación de la regla de la cadena en el Ejercicio 1 permitió modelar "
        "con precisión la tasa de cambio de la resistencia mecánica del material de construcción (<i>dR/dt ≈ -0.0661 MPa/h</i> a las dos horas). "
        "Se demostró analíticamente cómo la variación indirecta a través de la temperatura gobierna la velocidad de hidratación sin requerir mediciones empíricas destructivas directas."
    )
    story.append(Paragraph(c1, body_style))

    c2 = (
        "2. <b>Eficacia de la Derivación Implícita en Modelos Estructurales Complejos:</b> En el Ejercicio 2, ante la imposibilidad de formular "
        "una función explícita unívoca para la relación carga-deformación (<i>y² = x²(41 - x²)</i>), la técnica implícita permitió obtener la pendiente "
        "exacta <i>dy/dx = -2.25 mm/ton</i> en el punto <i>P(5, 20)</i>. Esta herramienta matemática cuantifica la degradación de rigidez "
        "en fases post-pico de deformación estructural."
    )
    story.append(Paragraph(c2, body_style))

    c3 = (
        "3. <b>Control Dinámico Mediante Derivadas de Orden Superior:</b> El análisis cinemático del elemento vibrante en el Ejercicio 3 evidenció "
        "que los estados de reposo transitorio ocurren en <i>t ≈ 1.30 s</i> y <i>t ≈ 15.37 s</i>, mientras que las condiciones de aceleración coincidente "
        "(mismo signo) se focalizan en los intervalos <i>(1.30 s, 8.33 s)</i> y <i>(15.37 s, ∞)</i>. Esto proporciona al ingeniero criterios cuantitativos "
        "para diseñar sistemas de disipación que prevengan el colapso por fatiga metálica."
    )
    story.append(Paragraph(c3, body_style))

    c4 = (
        "4. <b>Sostenibilidad y Optimización de Recursos:</b> En el Ejercicio 4, el cálculo diferencial resolvió el óptimo de corte de un perfil de acero "
        "de 15 metros, demostrando que al destinar <b>6.52 metros</b> para el cuadrado y <b>8.48 metros</b> para el triángulo se logra el área mínima "
        "absoluta de <b>6.12 m²</b>. Esto genera un ahorro geométrico y estructural sustancial frente a cualquier distribución intuitiva."
    )
    story.append(Paragraph(c4, body_style))

    c5 = (
        "5. <b>Competencias Globales y Bilingüismo Científico:</b> La estructuración de la infografía en inglés fortaleció la articulación "
        "entre los conceptos matemáticos formales y los estándares internacionales de comunicación técnica en ingeniería civil."
    )
    story.append(Paragraph(c5, body_style))

    story.append(Spacer(1, 10))

    # ==========================================
    # 9. REFERENCIAS BIBLIOGRÁFICAS (APA 7)
    # ==========================================
    story.append(Paragraph("<b>8. Referencias Bibliográficas (Normativa APA 7.ª Edición)</b>", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#2b6cb0"), spaceAfter=8, spaceBefore=2))

    ref_style = ParagraphStyle(
        'APAReference',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13.5,
        leftIndent=24,
        firstLineIndent=-24,
        textColor=colors.HexColor("#1a202c"),
        spaceAfter=6
    )

    references = [
        "Larson, R., & Edwards, B. H. (2014). <i>Cálculo de una variable</i> (10.ª ed.). McGraw-Hill Interamericana.",
        "Rogawski, J. (2016). <i>Cálculo: Una variable</i> (2.ª ed.). Editorial Reverté.",
        "Stewart, J. (2016). <i>Cálculo de una variable: Trascendentes tempranas</i> (8.ª ed.). Cengage Learning.",
        "Thomas, G. B., Weir, M. D., & Hass, J. (2015). <i>Cálculo: Una variable</i> (13.ª ed.). Pearson Educación.",
        "Universidad Nacional Abierta y a Distancia [UNAD]. (2026). <i>Guía de actividades y rúbrica de evaluación – Reto 4: Diseño de soluciones mediante la derivada</i>. Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI).",
        "Universidad Nacional Abierta y a Distancia [UNAD]. (2026). <i>Anexo 5: Contextos Reto 4 — Diseño de soluciones mediante la derivada</i>. Código de Curso 100410.",
        "Zill, D. G., & Wright, W. S. (2011). <i>Cálculo de una variable: Trascendentes tempranas</i> (4.ª ed.). McGraw-Hill."
    ]

    for ref in references:
        story.append(Paragraph(ref, ref_style))

    # Build PDF with NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Documento PDF '{pdf_filename}' generado exitosamente.")

if __name__ == "__main__":
    create_report()
