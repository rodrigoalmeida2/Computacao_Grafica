import tkinter as tk

# Função para calcular um ponto da curva de Bézier de grau 3 (Cúbica)
def bezier3(t, p0, p1, p2, p3):
    x = (1 - t)**3 * p0[0] + 3 * (1 - t)**2 * t * p1[0] + 3 * (1 - t) * t**2 * p2[0] + t**3 * p3[0]
    y = (1 - t)**3 * p0[1] + 3 * (1 - t)**2 * t * p1[1] + 3 * (1 - t) * t**2 * p2[1] + t**3 * p3[1]
    return round(x), round(y)

# Algoritmo de Bresenham para desenhar linhas
def bresenham(x0, y0, x1, y1, canvas):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        canvas.create_rectangle(x0 * 20, y0 * 20, (x0 + 1) * 20, (y0 + 1) * 20, fill="blue", outline="black")
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

# Função para desenhar a curva de Bézier de grau 3
def draw_bezier3():
    try:
        x0 = int(entry_x0.get()) + 11
        y0 = 11 - int(entry_y0.get())
        x1 = int(entry_x1.get()) + 11
        y1 = 11 - int(entry_y1.get())
        x2 = int(entry_x2.get()) + 11
        y2 = 11 - int(entry_y2.get())
        x3 = int(entry_x3.get()) + 11
        y3 = 11 - int(entry_y3.get())

        canvas.delete("all")  # Limpar o canvas
        draw_grid(canvas)

        # Rasterizar a curva de Bézier
        prev_x, prev_y = x0, y0
        for t in range(101):
            t = t / 100
            x, y = bezier3(t, (x0, y0), (x1, y1), (x2, y2), (x3, y3))
            bresenham(prev_x, prev_y, x, y, canvas)
            prev_x, prev_y = x, y
    except ValueError:
        pass  # Ignorar entradas inválidas

# Função para desenhar a grade e os eixos de coordenadas
def draw_grid(canvas):
    # Eixo x e y
    canvas.create_line(0, 220, 440, 220, fill="gray")  # Eixo X
    canvas.create_line(220, 0, 220, 440, fill="gray")  # Eixo Y
    # Linhas da grade
    for i in range(0, 440, 20):
        canvas.create_line(i, 0, i, 440, fill="lightgray")
        canvas.create_line(0, i, 440, i, fill="lightgray")

# Interface gráfica
root = tk.Tk()
root.title("Curva de Bézier Grau 3")

# Entradas para os pontos de controle da Bézier
tk.Label(root, text="Ponto Inicial X0:").grid(row=0, column=0)
entry_x0 = tk.Entry(root)
entry_x0.grid(row=0, column=1)

tk.Label(root, text="Ponto Inicial Y0:").grid(row=0, column=2)
entry_y0 = tk.Entry(root)
entry_y0.grid(row=0, column=3)

tk.Label(root, text="Ponto Controle X1:").grid(row=1, column=0)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=1, column=1)

tk.Label(root, text="Ponto Controle Y1:").grid(row=1, column=2)
entry_y1 = tk.Entry(root)
entry_y1.grid(row=1, column=3)

tk.Label(root, text="Ponto Controle X2:").grid(row=2, column=0)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=2, column=1)

tk.Label(root, text="Ponto Controle Y2:").grid(row=2, column=2)
entry_y2 = tk.Entry(root)
entry_y2.grid(row=2, column=3)

tk.Label(root, text="Ponto Final X3:").grid(row=3, column=0)
entry_x3 = tk.Entry(root)
entry_x3.grid(row=3, column=1)

tk.Label(root, text="Ponto Final Y3:").grid(row=3, column=2)
entry_y3 = tk.Entry(root)
entry_y3.grid(row=3, column=3)

# Botão para desenhar a curva Bézier de grau 3
draw_bezier3_button = tk.Button(root, text="Desenhar Bézier Grau 3", command=draw_bezier3)
draw_bezier3_button.grid(row=4, column=0, columnspan=2)

# Canvas para o desenho
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=5, column=0, columnspan=4)

# Desenhar a grade inicial
draw_grid(canvas)

root.mainloop()
