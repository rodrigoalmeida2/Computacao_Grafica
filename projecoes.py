import tkinter as tk
import math
from Bresenham import bresenham as bs

# Função para desenhar o polígono com os vértices especificados, usando Bresenham para as arestas
def draw_polygon(vertices, canvas, color="blue"):
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        bs.bresenham_line(round(x1), round(y1), round(x2), round(y2), canvas, color)

# Função para capturar as coordenadas dos vértices fornecidos (em 3D)
def get_polygon_coordinates_3d():
    try:
        coords = entry_polygon.get().split(';')  # Pega as coordenadas separadas por ";"
        vertices = []
        for coord in coords:
            x, y, z = map(int, coord.split(','))
            vertices.append((x, y, z))
        return vertices
    except ValueError:
        return []

# Projeção Ortogonal: descarta a coordenada z
def orthogonal_projection(vertices):
    projected_vertices = [(x, y) for x, y, z in vertices]
    return projected_vertices

# Projeção Oblíqua: inclui uma distorção proporcional ao valor de z
def oblique_projection(vertices, alpha=45, l=0.5):
    angle_radians = math.radians(alpha)
    projected_vertices = [(x + l * z * math.cos(angle_radians), y + l * z * math.sin(angle_radians)) for x, y, z in vertices]
    return projected_vertices

# Projeção em Perspectiva: aplica a redução baseada na profundidade (z)
def perspective_projection(vertices, d=500):
    projected_vertices = [(x * d / (d + z), y * d / (d + z)) for x, y, z in vertices]
    return projected_vertices

# Função para desenhar a projeção ortogonal
def draw_orthogonal():
    canvas.delete("all")  # Limpar o canvas
    draw_grid(canvas)  # Redesenha a grade
    vertices = get_polygon_coordinates_3d()
    ortho_vertices = orthogonal_projection(vertices)
    draw_polygon(ortho_vertices, canvas, "blue")

# Função para desenhar a projeção oblíqua
def draw_oblique():
    canvas.delete("all")  # Limpar o canvas
    draw_grid(canvas)  # Redesenha a grade
    vertices = get_polygon_coordinates_3d()
    oblique_vertices = oblique_projection(vertices)
    draw_polygon(oblique_vertices, canvas, "green")

# Função para desenhar a projeção em perspectiva
def draw_perspective():
    canvas.delete("all")  # Limpar o canvas
    draw_grid(canvas)  # Redesenha a grade
    vertices = get_polygon_coordinates_3d()
    perspective_vertices = perspective_projection(vertices)
    draw_polygon(perspective_vertices, canvas, "red")

# Função para desenhar a grade e os eixos
def draw_grid(canvas):
    canvas.create_line(0, 220, 440, 220, fill="gray")  # Eixo X
    canvas.create_line(220, 0, 220, 440, fill="gray")  # Eixo Y
    for i in range(0, 440, 20):
        canvas.create_line(i, 0, i, 440, fill="lightgray")
        canvas.create_line(0, i, 440, i, fill="lightgray")

# Interface principal
root = tk.Tk()
root.title("Projeções 3D com Bresenham")

# Entrada de coordenadas do polígono (x, y, z)
tk.Label(root, text="Polígono (x,y,z;x,y,z;...):").grid(row=0, column=0)
entry_polygon = tk.Entry(root)
entry_polygon.grid(row=0, column=1, columnspan=3)

# Botão para desenhar projeção ortogonal
ortho_button = tk.Button(root, text="Projeção Ortogonal", command=draw_orthogonal)
ortho_button.grid(row=1, column=0)

# Botão para desenhar projeção oblíqua
oblique_button = tk.Button(root, text="Projeção Oblíqua", command=draw_oblique)
oblique_button.grid(row=1, column=1)

# Botão para desenhar projeção em perspectiva
perspective_button = tk.Button(root, text="Projeção Perspectiva", command=draw_perspective)
perspective_button.grid(row=1, column=2)

# Canvas para desenhar o polígono e as transformações
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=2, column=0, columnspan=4)

# Desenhar a grade e os eixos iniciais
draw_grid(canvas)

root.mainloop()
