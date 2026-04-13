# Robotica-Lab1

> **ICI 4150 – Robótica y Sistemas Autónomos 2026-01**
> Laboratorio 1: Simulación de un robot móvil diferencial en Webots

---

## Descripción

Este laboratorio simula el comportamiento cinemático de un robot móvil diferencial (e-puck) en Webots. Se implementaron dos modos de operación:

- **Control manual**: el usuario conduce el robot en tiempo real desde el teclado.
- **Secuencias automáticas**: el robot ejecuta una serie de trayectorias predefinidas (línea recta, curva, giro en sitio, círculo, cuadrado).

El objetivo es comprender cómo las velocidades individuales de cada rueda determinan el movimiento del robot, aplicando el modelo cinemático diferencial.

---

## Cómo ejecutar la simulación

### 1. Clonar el repositorio

```bash
git clone https://github.com/sebacruz1/Robotica-Lab1
```

### 2. Abrir el mundo en Webots

1. Abrir Webots.
2. Ir a File -> Open World.
3. Seleccionar `worlds/Lab1.wbt`.

El mundo contiene dos instancias del robot e-puck:

| Robot           | Controlador                    | Descripción                         |
| --------------- | ------------------------------ | ----------------------------------- |
| `e-puck_manual` | `controlador_robot_manual`     | Control en tiempo real por teclado  |
| `e-puck tests`  | `controlador_test_automaticos` | Secuencias automáticas predefinidas |

> **Nota:** El robot controlado manualmente (`e-puck_manual`) tiene sus LEDs encendidos, lo que permite identificarlo visualmente dentro de la simulación.

### 3. Ejecutar la simulación

Presiona el botón **Play** (▶) en Webots.

---

## Control Manual

El robot `e-puck_manual` responde a las siguientes teclas:

| Tecla   | Acción                         |
| ------- | ------------------------------ |
| `↑`     | Aumenta velocidad lineal       |
| `↓`     | Disminuye velocidad lineal     |
| `←`     | Gira a la izquierda (ajusta ω) |
| `→`     | Gira a la derecha (ajusta ω)   |
| `SPACE` | Freno completo (v = 0, ω = 0)  |

Las velocidades de rueda se calculan como:

```python
left_speed  = linear - angular
right_speed = linear + angular
```

---

## Secuencias Automáticas

El robot `e-puck tests` ejecuta los siguientes experimentos en orden:

| Experimento       | Condición                         | Resultado esperado     |
| ----------------- | --------------------------------- | ---------------------- |
| Línea recta       | `vr == vl`                        | Avance sin desvío      |
| Trayectoria curva | `vr ≠ vl`                         | Arco de circunferencia |
| Giro en sitio     | `vr == -vl`                       | Rotación sobre el eje  |
| Círculo           | `vr` y `vl` constantes desiguales | Círculo cerrado        |
| Cuadrado          | Alternancia recto/giro 90°        | Figura cuadrada        |

Para cada secuencia se reporta en consola:

```
v = X.XX m/s   ω = X.XX rad/s
```

> **Nota:** Los mensajes de consola correspondientes a las secuencias automáticas se muestran en **color rojo**, lo que permite distinguirlos fácilmente de otros mensajes del sistema.

---

## Resultados
<img width="1411" height="1001" alt="image" src="https://github.com/user-attachments/assets/60172b08-61d7-4f05-bfda-d6f8de63c859" />

### Observaciones

- Cuando `vr = vl`, el robot avanza en línea recta sin rotación (`ω = 0`).
- Cuando `vr ≠ vl`, la trayectoria curva hacia la rueda más lenta.
- Cuando `vr = -vl`, el robot rota en su propio eje (`v = 0`).
- Para dibujar un círculo, se mantienen velocidades constantes y distintas entre ruedas.

---

## Preguntas de Análisis

1. **¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?**
   El robot avanza en línea recta. La velocidad angular `ω` es cero porque la diferencia `vr - vl = 0`.

2. **¿Cómo cambia la trayectoria cuando las velocidades son diferentes?**
   El robot describe una curva. El radio de curvatura es inversamente proporcional a la diferencia de velocidades.

3. **¿Qué ocurre cuando una rueda gira en sentido opuesto?**
   El robot rota sobre su propio eje. La velocidad lineal `v` es cero.

4. **¿Qué tipo de movimiento permite dibujar un círculo?**
   Velocidades constantes y distintas en ambas ruedas (`vr ≠ vl`, mismo signo), lo que produce una trayectoria circular continua de radio `R = L/2 · (vr + vl)/(vr - vl)`.

---

## Equipo

| Rol            | Responsabilidad                | Autor                  |
| -------------- | ------------------------------ | ---------------------- |
| Programador    | Implementación del controlador | Sebastián Cruz         |
| Experimentador | Ejecución de pruebas           | Maximiliano Bustamante |
| Analista       | Interpretación de resultados   | Ignacio Ávila          |
| Documentador   | Redacción del informe y README | Joaquín Fuenzalida     |
| Integrador     | Coordinación del equipo        | Sebastián Cruz         |

---

## Licencia

Proyecto académico – ICI 4150, PUCV, 2026.
