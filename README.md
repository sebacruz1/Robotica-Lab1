# Robotica-Lab1

Este repositorio contiene la implementación de un controlador básico para un robot móvil diferencial utilizando el simulador **Webots**. El proyecto permite gestionar el movimiento del robot en tiempo real mediante comandos de teclado.

---

# Contenido
1. [Descripción del Laboratorio](#1-descripción-del-laboratorio)
2. [Instrucciones de Ejecución](#2-instrucciones-de-ejecución)
3. [Resultados Obtenidos](#3-resultados-obtenidos)

---

## 1. Descripción del Laboratorio
[cite_start]El objetivo principal es comprender y aplicar la cinemática de un robot diferencial[cite: 1]. [cite_start]El movimiento se controla ajustando las velocidades de los motores izquierdo y derecho basándose en la entrada del usuario capturada por el teclado[cite: 1].

### Lógica de Movimiento
[cite_start]De acuerdo a las reglas de navegación establecidas para este modelo[cite: 1]:
* [cite_start]**Avance recto:** Ambas ruedas giran a la misma velocidad ($V_i = V_d$)[cite: 1].
* [cite_start]**Giro a la izquierda:** La rueda derecha tiene una velocidad mayor que la izquierda ($V_d > V_i$)[cite: 1].
* [cite_start]**Giro a la derecha:** La rueda izquierda tiene una velocidad mayor que la derecha ($V_i > V_d$)[cite: 1].
* [cite_start]**Rotación sobre su propio eje:** Las ruedas giran en direcciones opuestas[cite: 1].
* [cite_start]**Trayectoria circular:** Se recomienda una relación de velocidad donde una rueda sea el doble de la otra[cite: 1].

## 2. Instrucciones de Ejecución

### Requisitos
* [cite_start]Simulador **Webots** instalado[cite: 1].
* [cite_start]Python 3.x configurado como intérprete en el simulador[cite: 1].

### Pasos para Simular
1. Clone este repositorio en su máquina local.
2. Abra el archivo de mundo en Webots.
3. [cite_start]Asegúrese de que el robot tenga asignado el script `controlador_robot.py`[cite: 1].
4. Inicie la simulación presionando el botón **Play**.
5. [cite_start]Haga clic en la ventana 3D de Webots y utilice las **flechas del teclado** para mover el robot[cite: 1]:
    * [cite_start]**↑ / ↓**: Control de velocidad lineal (adelante/atrás)[cite: 1].
    * [cite_start]**← / →**: Control de velocidad angular (giros)[cite: 1].

## 3. Resultados Obtenidos
[cite_start]El controlador procesa las entradas para calcular las velocidades de cada motor, limitándolas a un máximo de $\pm 5.0$ para mantener la estabilidad[cite: 1].

| Comando | Acción | Impacto en Velocidad |
| :--- | :--- | :--- |
| **Flecha Arriba** | Adelante | [cite_start]`linear` +5.0 [cite: 1] |
| **Flecha Abajo** | Atrás | [cite_start]`linear` -5.0 [cite: 1] |
| **Flecha Izquierda** | Giro Izq. | [cite_start]`angular` +2.0 [cite: 1] |
| **Flecha Derecha** | Giro Der. | [cite_start]`angular` -2.0 [cite: 1] |

### Preguntas de análisis

1. ¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?
- Velocidades iguales: avanza en línea recta

2. ¿Cómo cambia la trayectoria cuando las velocidades son diferentes?  
- Velocidad derecha mayor: gira en circulos hacia su izquierda
- Velocidad izquierda mayor: gira en circulos hacia su derecha

3. ¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?
- Ruedas en direcciones distintas: gira en su propio eje

4. ¿Qué tipo de movimiento permite dibujar un círculo?
- Para dibujar un circulo hay que dejar una rueda con una mayor velocidad (? el doble del otro ?
