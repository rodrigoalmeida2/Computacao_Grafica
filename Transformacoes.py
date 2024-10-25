import tkinter as tk
import math
from Bresenham import bresenham as bs

# Função para desenhar o polígono com os vértices especificados, usando Bresenham para as arestas
def draw_polygon(vertices, canvas, color="blue"):
    canvas.delete("all")
    bs.draw_grid(canvas)  # Redesenha a grade
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        bs.bresenham_line(round(x1), round(y1), round(x2), round(y2), canvas, color)

# Função para capturar as coordenadas dos vértices fornecidos
def get_polygon_coordinates():
    try:
        coords = entry_polygon.get().split(';')  # Pega as coordenadas separadas por ";"
        vertices = []
        for coord in coords:
            x, y = map(int, coord.split(','))
            vertices.append((x, y))
        return vertices
    except ValueError:
        return []

# Função para aplicar rotação
def apply_rotation():
    try:
        angle = math.radians(float(entry_angle.get()))  # Converte o ângulo para radianos
        pivot_x = int(entry_pivot_x.get())
        pivot_y = int(entry_pivot_y.get())
        vertices = get_polygon_coordinates()

        rotated_vertices = []
        for x, y in vertices:
            # Transladar o ponto de pivô para a origem
            translated_x = x - pivot_x
            translated_y = y - pivot_y

            # Aplicar rotação
            rotated_x = translated_x * math.cos(angle) - translated_y * math.sin(angle)
            rotated_y = translated_x * math.sin(angle) + translated_y * math.cos(angle)

            # Voltar o ponto rotacionado para a posição original
            final_x = rotated_x + pivot_x
            final_y = rotated_y + pivot_y

            # Arredondar para evitar problemas de precisão e adicionar ao novo conjunto de vértices
            rotated_vertices.append((round(final_x), round(final_y)))

        draw_polygon(rotated_vertices, canvas, "red")
    except ValueError:
        pass

# Função para aplicar translação
def apply_translation():
    try:
        dx = int(entry_dx.get())
        dy = int(entry_dy.get())
        vertices = get_polygon_coordinates()

        translated_vertices = [(x + dx, y + dy) for x, y in vertices]
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
        vertices = get_polygon_coordinates()

        scaled_vertices = []
        for x, y in vertices:
            # Transladar o ponto de pivô para a origem
            translated_x = x - scale_pivot_x
            translated_y = y - scale_pivot_y

            # Aplicar escala
            scaled_x = translated_x * sx
            scaled_y = translated_y * sy

            # Voltar o ponto escalado para a posição original
            final_x = scaled_x + scale_pivot_x
            final_y = scaled_y + scale_pivot_y

            # Arredondar para garantir que caia em coordenadas inteiras
            scaled_vertices.append((round(final_x), round(final_y)))

        draw_polygon(scaled_vertices, canvas, "purple")
    except ValueError:
        pass

# Função para desenhar o polígono inicial
def draw_initial_polygon():
    vertices = get_polygon_coordinates()
    draw_polygon(vertices, canvas, "blue")

# Interface principal
root = tk.Tk()
root.title("Transformações de Polígono com Bresenham")

# Entrada de coordenadas do polígono
tk.Label(root, text="Polígono (x1,y1;x2,y2;...):").grid(row=0, column=0)
entry_polygon = tk.Entry(root)
entry_polygon.grid(row=0, column=1, columnspan=3)

# Botão para desenhar o polígono inicial
draw_polygon_button = tk.Button(root, text="Desenhar Polígono", command=draw_initial_polygon)
draw_polygon_button.grid(row=1, column=1, columnspan=2)

# Entradas para rotação
tk.Label(root, text="Rotação:").grid(row=2, column=0)
tk.Label(root, text="Ângulo:").grid(row=3, column=0)
entry_angle = tk.Entry(root)
entry_angle.grid(row=3, column=1)

tk.Label(root, text="Pivô X:").grid(row=3, column=2)
entry_pivot_x = tk.Entry(root)
entry_pivot_x.grid(row=3, column=3)

tk.Label(root, text="Pivô Y:").grid(row=4, column=2)
entry_pivot_y = tk.Entry(root)
entry_pivot_y.grid(row=4, column=3)

rotate_button = tk.Button(root, text="Rotacionar", command=apply_rotation)
rotate_button.grid(row=4, column=1)

# Entradas para translação
tk.Label(root, text="Translação:").grid(row=5, column=0)
tk.Label(root, text="dx:").grid(row=6, column=0)
entry_dx = tk.Entry(root)
entry_dx.grid(row=6, column=1)

tk.Label(root, text="dy:").grid(row=6, column=2)
entry_dy = tk.Entry(root)
entry_dy.grid(row=6, column=3)

translate_button = tk.Button(root, text="Transladar", command=apply_translation)
translate_button.grid(row=7, column=1)

# Entradas para escala
tk.Label(root, text="Escala:").grid(row=8, column=0)
tk.Label(root, text="sx:").grid(row=9, column=0)
entry_scale_x = tk.Entry(root)
entry_scale_x.grid(row=9, column=1)

tk.Label(root, text="sy:").grid(row=9, column=2)
entry_scale_y = tk.Entry(root)
entry_scale_y.grid(row=9, column=3)

tk.Label(root, text="Pivô Escala X:").grid(row=10, column=0)
entry_pivot_scale_x = tk.Entry(root)
entry_pivot_scale_x.grid(row=10, column=1)

tk.Label(root, text="Pivô Escala Y:").grid(row=10, column=2)
entry_pivot_scale_y = tk.Entry(root)
entry_pivot_scale_y.grid(row=10, column=3)

scale_button = tk.Button(root, text="Escalar", command=apply_scale)
scale_button.grid(row=11, column=1)

# Canvas para desenhar o polígono e as transformações
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=12, column=0, columnspan=4)

# Desenhar a grade e os eixos iniciais
bs.draw_grid(canvas)

root.mainloop()
