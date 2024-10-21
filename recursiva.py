import tkinter as tk

# Algoritmo de Bresenham para desenhar linhas
def bresenham(x0, y0, x1, y1, canvas):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        canvas.create_rectangle(x0 * 20, y0 * 20, (x0 + 1) * 20, (y0 + 1) * 20, fill="red")
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
        draw_grid(canvas)

        # Desenhar as bordas do polígono
        for i in range(len(points)):
            x0, y0 = points[i]
            x1, y1 = points[(i + 1) % len(points)]  # Para fechar o polígono
            bresenham(x0, y0, x1, y1, canvas)
    except ValueError:
        pass  # Ignorar entradas inválidas

# Função para preenchimento recursivo (Flood Fill)
def flood_fill(x, y, canvas):
    # Converte para coordenadas da grade
    pixel = canvas.find_overlapping(x * 20 + 10, y * 20 + 10, x * 20 + 11, y * 20 + 11)
    if pixel:
        return  # Não preenche fora do polígono ou onde já há preenchimento

    canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="blue")

    # Chama recursivamente para os vizinhos
    flood_fill(x + 1, y, canvas)
    flood_fill(x - 1, y, canvas)
    flood_fill(x, y + 1, canvas)
    flood_fill(x, y - 1, canvas)

# Função para preencher o polígono com flood fill
def apply_flood_fill():
    try:
        x, y = map(int, entry_point.get().split(','))
        x += 11
        y = 11 - y
        flood_fill(x, y, canvas)
    except ValueError:
        pass

# Função para preencher o polígono com algoritmo de varredura (Scanline)
def scanline_fill():
    try:
        points_input = entry_polygon.get()  # Exemplo de entrada: "-5,0; 5,0; 3,3; 0,7; -3,3"
        points = [(int(p.split(',')[0]) + 11, 11 - int(p.split(',')[1])) for p in points_input.split(';')]

        # Desenha o polígono
        draw_polygon()

        # Encontrar o limite superior e inferior do polígono
        min_y = min(y for _, y in points)
        max_y = max(y for _, y in points)

        # Preenchimento por varredura linha por linha
        for y in range(min_y, max_y + 1):
            intersections = []
            for i in range(len(points)):
                x0, y0 = points[i]
                x1, y1 = points[(i + 1) % len(points)]

                # Verifica se a linha de varredura cruza a aresta
                if y0 == y1:  # Ignora linhas horizontais
                    continue
                if y0 < y1:
                    x0, y0, x1, y1 = x1, y1, x0, y0  # Garante que estamos subindo na varredura
                if y > min(y0, y1) and y <= max(y0, y1):  # A linha de varredura cruza essa aresta
                    # Calcula o ponto de interseção
                    x_intersection = int(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
                    intersections.append(x_intersection)

            # Ordena as interseções e preenche os pixels entre pares de interseções
            intersections.sort()
            for i in range(0, len(intersections), 2):
                if i + 1 < len(intersections):
                    x_start, x_end = intersections[i], intersections[i + 1]
                    for x in range(x_start, x_end + 1):
                        canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green")

    except ValueError:
        pass  # Ignora entradas inválidas


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
draw_grid(canvas)

root.mainloop()
#-4,-4; 4,-4; 4,4; -4,4; -4,-4
