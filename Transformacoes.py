import tkinter as tk
import math

# Função do Algoritmo de Bresenham para desenhar uma linha com quadrados coloridos
def bresenham_line(x1, y1, x2, y2, canvas, color="red"):
    x1 = x1 + 11
    y1 = 11 - y1
    x2 = x2 + 11
    y2 = 11 - y2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        # Desenhar quadrado colorido no canvas (20x20 pixels para cada coordenada)
        canvas.create_rectangle(x1 * 20, y1 * 20, (x1 + 1) * 20, (y1 + 1) * 20, fill=color)
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Função para desenhar o polígono com os vértices especificados, usando Bresenham para as arestas
def draw_polygon(vertices, canvas, color="red"):
    canvas.delete("all")
    draw_grid(canvas)  # Redesenha a grade
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        bresenham_line(x1, y1, x2, y2, canvas, color)

# Função para aplicar rotação
def apply_rotation():
    try:
        angle = math.radians(float(entry_angle.get()))  # Converte o ângulo para radianos
        pivot_x = int(entry_pivot_x.get())
        pivot_y = int(entry_pivot_y.get())

        rotated_vertices = []
        for x, y in entry_polygon:
            translated_x = x - pivot_x
            translated_y = y - pivot_y

            rotated_x = translated_x * math.cos(angle) - translated_y * math.sin(angle)
            rotated_y = translated_x * math.sin(angle) + translated_y * math.cos(angle)

            final_x = rotated_x + pivot_x
            final_y = rotated_y + pivot_y
            rotated_vertices.append((final_x, final_y))

        draw_polygon(rotated_vertices, canvas, "red")
    except ValueError:
        pass

# Função para aplicar translação
def apply_translation():
    try:
        dx = int(entry_dx.get())
        dy = int(entry_dy.get())

        translated_vertices = [(x + dx, y + dy) for x, y in entry_polygon]
        draw_polygon(translated_vertices, canvas, "green")
    except ValueError:
        pass

# Função para aplicar escala
def apply_scale():
    try:
        sx = float(entry_scale_x.get())
        sy = float(entry_scale_y.get())
        scale_pivot_x = int(entry_pivot_scale_x.get())
        scale_pivot_y = int(entry_pivot_scale_y.get())

        scaled_vertices = []
        for x, y in entry_polygon:
            translated_x = x - scale_pivot_x
            translated_y = y - scale_pivot_y

            scaled_x = translated_x * sx
            scaled_y = translated_y * sy

            final_x = scaled_x + scale_pivot_x
            final_y = scaled_y + scale_pivot_y
            scaled_vertices.append((final_x, final_y))

        draw_polygon(scaled_vertices, canvas, "purple")
    except ValueError:
        pass

# Função para desenhar o polígono inicial
def draw_initial_polygon():
    draw_polygon(entry_polygon, canvas, "blue")

# Função para desenhar a grade e os eixos
def draw_grid(canvas):
    canvas.create_line(0, 220, 440, 220, fill="gray")  # Eixo X
    canvas.create_line(220, 0, 220, 440, fill="gray")  # Eixo Y
    for i in range(0, 440, 20):
        canvas.create_line(i, 0, i, 440, fill="lightgray")
        canvas.create_line(0, i, 440, i, fill="lightgray")

# Interface principal
root = tk.Tk()
root.title("Transformações de Polígono com Bresenham")

# Entrada para os pontos do polígono
tk.Label(root, text="Polígono (Pontos X,Y separados por ponto e vírgula):").grid(row=0, column=0)
entry_polygon = tk.Entry(root, width=50)
entry_polygon.grid(row=0, column=1)

# Botão para desenhar o polígono inicial
draw_polygon_button = tk.Button(root, text="Desenhar Polígono", command=draw_initial_polygon)
draw_polygon_button.grid(row=0, column=1, columnspan=2)

# Entradas para rotação
tk.Label(root, text="Rotação:").grid(row=1, column=0)
tk.Label(root, text="Ângulo:").grid(row=2, column=0)
entry_angle = tk.Entry(root)
entry_angle.grid(row=2, column=1)

tk.Label(root, text="Pivô X:").grid(row=2, column=2)
entry_pivot_x = tk.Entry(root)
entry_pivot_x.grid(row=2, column=3)

tk.Label(root, text="Pivô Y:").grid(row=3, column=2)
entry_pivot_y = tk.Entry(root)
entry_pivot_y.grid(row=3, column=3)

rotate_button = tk.Button(root, text="Rotacionar", command=apply_rotation)
rotate_button.grid(row=3, column=1)

# Entradas para translação
tk.Label(root, text="Translação:").grid(row=4, column=0)
tk.Label(root, text="dx:").grid(row=5, column=0)
entry_dx = tk.Entry(root)
entry_dx.grid(row=5, column=1)

tk.Label(root, text="dy:").grid(row=5, column=2)
entry_dy = tk.Entry(root)
entry_dy.grid(row=5, column=3)

translate_button = tk.Button(root, text="Transladar", command=apply_translation)
translate_button.grid(row=6, column=1)

# Entradas para escala
tk.Label(root, text="Escala:").grid(row=7, column=0)
tk.Label(root, text="sx:").grid(row=8, column=0)
entry_scale_x = tk.Entry(root)
entry_scale_x.grid(row=8, column=1)

tk.Label(root, text="sy:").grid(row=8, column=2)
entry_scale_y = tk.Entry(root)
entry_scale_y.grid(row=8, column=3)

tk.Label(root, text="Pivô Escala X:").grid(row=9, column=0)
entry_pivot_scale_x = tk.Entry(root)
entry_pivot_scale_x.grid(row=9, column=1)

tk.Label(root, text="Pivô Escala Y:").grid(row=9, column=2)
entry_pivot_scale_y = tk.Entry(root)
entry_pivot_scale_y.grid(row=9, column=3)

scale_button = tk.Button(root, text="Escalar", command=apply_scale)
scale_button.grid(row=10, column=1)

# Canvas para desenhar o polígono e as transformações
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=11, column=0, columnspan=4)

# Desenhar a grade e os eixos iniciais
draw_grid(canvas)

root.mainloop()