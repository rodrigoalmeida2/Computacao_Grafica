import tkinter as tk
from Bresenham import bresenham as bs


# Algoritmo de Bresenham para desenhar linhas
def bresenham(x0, y0, x1, y1, canvas):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        canvas.create_rectangle(x0 * 20, y0 * 20, (x0 + 1) * 20, (y0 + 1) * 20, fill="red", outline="black")
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

# Função para desenhar o polígono usando bresenham
def draw_polygon():
    try:
        points_input = entry_polygon.get()  # Exemplo de entrada: "-5,0; 5,0; 3,3; 0,7; -3,3"
        points = [(int(p.split(',')[0]) + 11, 11 - int(p.split(',')[1])) for p in points_input.split(';')]

        canvas.delete("all")  # Limpar o canvas
        bs.draw_grid(canvas)

        # Desenhar as bordas do polígono
        for i in range(len(points)):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % len(points)]  # Para fechar o polígono
            bresenham(x0, y0, x1, y1, canvas)
    except ValueError:
        print("Entrada inválida! Verifique o formato dos pontos.")

def is_point_inside_polygon(x, y, points):
    """Verifica se um ponto está dentro do polígono usando o algoritmo de ponto de feixe."""
    n = len(points)
    inside = False

    p1x, p1y = points[0]
    for i in range(n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

# Preenche a área usando o algoritmo Flood Fill, somente se o ponto estiver dentro do polígono
def flood_fill(x, y, points):
    # Verifica se a coordenada inicial está dentro do polígono
    if not is_point_inside_polygon(x, y, points):
        return  # Não preenche se estiver fora do polígono

    pixel = canvas.find_overlapping(x * 20 + 10, y * 20 + 10, x * 20 + 11, y * 20 + 11)
    if pixel:
        return  # Não preenche fora do polígono ou onde já há preenchimento

    canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="blue")

    # Chama recursivamente para os vizinhos
    flood_fill(x + 1, y, points)
    flood_fill(x - 1, y, points)
    flood_fill(x, y + 1, points)
    flood_fill(x, y - 1, points)

# Função para iniciar o Flood Fill com ponto especificado
def apply_flood_fill():
    try:
        x, y = map(int, entry_point.get().split(','))
        x += 11
        y = 11 - y
        points_input = entry_polygon.get()
        points = [(int(p.split(',')[0]) + 11, 11 - int(p.split(',')[1])) for p in points_input.split(';')]
        flood_fill(x, y, points)
    except ValueError:
        print("Entrada inválida! Use o formato X,Y.")

# Varredura
def scanline_fill():
    try:
        points_input = entry_polygon.get()
        points = [(int(p.split(',')[0]) + 11, 11 - int(p.split(',')[1])) for p in points_input.split(';')]

        draw_polygon()  # Desenhar as bordas do polígono

        # Encontrar os limites vertical e horizontal
        min_y = min(y for _, y in points)
        max_y = max(y for _, y in points)

        # Preenchimento por varredura linha por linha
        for y in range(min_y + 1, max_y):  # Começar do min_y + 1 e ir até max_y - 1
            intersections = []
            for i in range(len(points)):
                x0, y0 = points[i]
                x1, y1 = points[(i + 1) % len(points)]

                if y0 == y1:  # Ignora linhas horizontais
                    continue
                if y0 < y1:
                    x0, y0, x1, y1 = x1, y1, x0, y0
                if y > min(y0, y1) and y < max(y0, y1):  # Verifica interseção
                    x_intersection = int(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
                    intersections.append(x_intersection)

            intersections.sort()
            for i in range(0, len(intersections), 2):
                if i + 1 < len(intersections):
                    x_start, x_end = intersections[i], intersections[i + 1]
                    for x in range(x_start + 1, x_end):  # Evita preencher a borda
                        canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="blue")

    except ValueError:
        print("Entrada inválida! Verifique o formato dos pontos.")

# Interface gráfica
root = tk.Tk()
root.title("Preenchimento de Polígonos")

# Entrada para os pontos do polígono
tk.Label(root, text="Polígono (Pontos X,Y separados por ponto e vírgula):").grid(row=0, column=0)
entry_polygon = tk.Entry(root, width=50)
entry_polygon.grid(row=0, column=1)

# Entrada para o ponto de preenchimento (Flood Fill)
tk.Label(root, text="Ponto para Flood Fill (X,Y):").grid(row=1, column=0)
entry_point = tk.Entry(root)
entry_point.grid(row=1, column=1)

# Botões para desenhar e preencher
draw_polygon_button = tk.Button(root, text="Desenhar Polígono", command=draw_polygon)
draw_polygon_button.grid(row=2, column=0, columnspan=2)

flood_fill_button = tk.Button(root, text="Aplicar Flood Fill", command=apply_flood_fill)
flood_fill_button.grid(row=3, column=0, columnspan=2)

scanline_fill_button = tk.Button(root, text="Preenchimento por Varredura", command=scanline_fill)
scanline_fill_button.grid(row=4, column=0, columnspan=2)

# Canvas para o desenho
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=5, column=0, columnspan=2)

# Desenhar a grade inicial
bs.draw_grid(canvas)

root.mainloop()
