import tkinter as tk
from tkinter import Canvas
import numpy as np
from Bresenham import bresenham as bs

# Função para desenhar a curva de Bezier de grau 2 usando Bresenham
def draw_bezier_2():
    try:
        p0 = (int(entry_x0.get()), int(entry_y0.get()))
        p1 = (int(entry_x1.get()), int(entry_y1.get()))
        p2 = (int(entry_x2.get()), int(entry_y2.get()))
    except ValueError:
        pass  # Ignora entradas inválidas

    canvas.delete("all")
    bs.draw_grid(canvas)  # Redesenha a grade

    previous_point = None
    for t in np.linspace(0, 1, 100):
        # Fórmula da Bezier de grau 2: B(t) = (1-t)^2 * P0 + 2*(1-t)*t * P1 + t^2 * P2
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        x, y = int(round(x)), int(round(y))
        if previous_point:
            # Usa Bresenham para conectar os pontos da curva
            bs.bresenham_line(previous_point[0], previous_point[1], x, y, canvas)
        previous_point = (x, y)

# Função para desenhar a curva de Bezier de grau 3 usando Bresenham
def draw_bezier_3():
    try:
        p0 = (int(entry_x0.get()), int(entry_y0.get()))
        p1 = (int(entry_x1.get()), int(entry_y1.get()))
        p2 = (int(entry_x2.get()), int(entry_y2.get()))
        p3 = (int(entry_x3.get()), int(entry_y3.get()))
    except ValueError:
        pass  # Ignora entradas inválidas
    canvas.delete("all")
    bs.draw_grid(canvas)  # Redesenha a grade

    previous_point = None
    for t in np.linspace(0, 1, 100):
        # Fórmula da Bezier de grau 3: B(t) = (1-t)^3 * P0 + 3*(1-t)^2*t * P1 + 3*(1-t)*t^2 * P2 + t^3 * P3
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        x, y = int(round(x)), int(round(y))
        if previous_point:
            # Usa Bresenham para conectar os pontos da curva
            bs.bresenham_line(previous_point[0], previous_point[1], x, y, canvas)
        previous_point = (x, y)

# Interface principal
root = tk.Tk()
root.title("Curvas de Bezier de Grau 2 e 3 com Bresenham")

# Entradas para pontos de controle
tk.Label(root, text="Ponto P0 (x0, y0):").grid(row=0, column=0)
entry_x0 = tk.Entry(root)
entry_x0.grid(row=0, column=1)
entry_y0 = tk.Entry(root)
entry_y0.grid(row=0, column=2)

tk.Label(root, text="Ponto P1 (x1, y1):").grid(row=1, column=0)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=1, column=1)
entry_y1 = tk.Entry(root)
entry_y1.grid(row=1, column=2)

tk.Label(root, text="Ponto P2 (x2, y2):").grid(row=2, column=0)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=2, column=1)
entry_y2 = tk.Entry(root)
entry_y2.grid(row=2, column=2)

tk.Label(root, text="Ponto P3 (x3, y3) [Apenas para Bezier Grau 3]:").grid(row=3, column=0)
entry_x3 = tk.Entry(root)
entry_x3.grid(row=3, column=1)
entry_y3 = tk.Entry(root)
entry_y3.grid(row=3, column=2)

# Botões para desenhar curvas
button_curve_2 = tk.Button(root, text="Desenhar Bezier Grau 2", command=draw_bezier_2)
button_curve_2.grid(row=4, column=0, columnspan=3)

button_curve_3 = tk.Button(root, text="Desenhar Bezier Grau 3", command=draw_bezier_3)
button_curve_3.grid(row=5, column=0, columnspan=3)

# Canvas para desenhar a curva
canvas = Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=6, column=0, columnspan=3)

# Desenhar a grade inicial
bs.draw_grid(canvas)

root.mainloop()
