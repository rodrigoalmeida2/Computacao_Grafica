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

# Projeção ortogonal: z é ignorado, projetamos no plano XY
def ortho_projection(vertices):
    projected = [(x, y) for x, y, z in vertices]
    return projected

# Projeção oblíqua: usando um ângulo típico de 45 graus para z
def oblique_projection(vertices, theta=45):
    theta = math.radians(theta)
    projected = [(x + z * math.cos(theta), y + z * math.sin(theta)) for x, y, z in vertices]
    return projected

# Projeção de perspectiva: assumindo uma distância do observador
def perspective_projection(vertices, d=5):
    projected = [(x / (1 + z / d), y / (1 + z / d)) for x, y, z in vertices]
    return projected

# Função para desenhar o objeto projetado no canvas
def draw_projected_object(vertices, edges, canvas, color="blue"):
    canvas.delete("all")
    draw_grid(canvas)
    
    for edge in edges:
        x1, y1 = vertices[edge[0]]
        x2, y2 = vertices[edge[1]]
        bresenham_line(round(x1), round(y1), round(x2), round(y2), canvas, color)

# Função para capturar as coordenadas e desenhar o polígono
def draw_polygon():
    try:
        # Capturar as coordenadas inseridas pelo usuário
        vertices_3d = []
        for i in range(0, len(vertex_entries), 3):
            x = int(vertex_entries[i].get())
            y = int(vertex_entries[i + 1].get())
            z = int(vertex_entries[i + 2].get())
            vertices_3d.append((x, y, z))
        
        # Definir arestas (conectando os vértices em sequência)
        edges = [(i, (i + 1) % len(vertices_3d)) for i in range(len(vertices_3d))]

        # Escolher a projeção
        projection_type = projection_var.get()
        if projection_type == "ortho":
            vertices_2d = ortho_projection(vertices_3d)
        elif projection_type == "oblique":
            vertices_2d = oblique_projection(vertices_3d)
        elif projection_type == "perspective":
            vertices_2d = perspective_projection(vertices_3d)

        # Desenhar o polígono projetado
        draw_projected_object(vertices_2d, edges, canvas)
    except ValueError:
        pass  # Ignorar entradas inválidas

# Função para desenhar a grade
def draw_grid(canvas):
    canvas.create_line(0, 220, 440, 220, fill="gray")  # Eixo X
    canvas.create_line(220, 0, 220, 440, fill="gray")  # Eixo Y
    for i in range(0, 440, 20):
        canvas.create_line(i, 0, i, 440, fill="lightgray")
        canvas.create_line(0, i, 440, i, fill="lightgray")

# Interface principal
root = tk.Tk()
root.title("Projeções 3D (Orto, Oblíqua, Perspectiva)")

# Seletor de projeção
projection_var = tk.StringVar(value="ortho")
tk.Radiobutton(root, text="Ortogonal", variable=projection_var, value="ortho").grid(row=0, column=0)
tk.Radiobutton(root, text="Oblíqua", variable=projection_var, value="oblique").grid(row=0, column=1)
tk.Radiobutton(root, text="Perspectiva", variable=projection_var, value="perspective").grid(row=0, column=2)

# Lista de entradas de vértices
vertex_entries = []
for i in range(5):  # Vamos começar com 5 vértices, você pode ajustar isso
    tk.Label(root, text=f"Vértice {i+1} (x, y, z):").grid(row=i+1, column=0)
    entry_x = tk.Entry(root, width=5)
    entry_y = tk.Entry(root, width=5)
    entry_z = tk.Entry(root, width=5)
    entry_x.grid(row=i+1, column=1)
    entry_y.grid(row=i+1, column=2)
    entry_z.grid(row=i+1, column=3)
    vertex_entries.extend([entry_x, entry_y, entry_z])

# Botão para desenhar o polígono
draw_button = tk.Button(root, text="Desenhar Polígono", command=draw_polygon)
draw_button.grid(row=6, column=1)

# Canvas para desenhar
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=7, column=0, columnspan=4)

# Desenhar a grade inicial
draw_grid(canvas)

root.mainloop()
