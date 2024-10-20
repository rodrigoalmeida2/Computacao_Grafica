import tkinter as tk

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

# Função para desenhar a polilinha
def draw_polyline():
    try:
        points_input = entry_points.get()  # Exemplo de entrada: "0,0; 5,3; -2,1"
        points = [(int(p.split(',')[0]) + 11, 11 - int(p.split(',')[1])) for p in points_input.split(';')]

        canvas.delete("all")  # Limpar o canvas
        draw_grid(canvas)

        # Rasterizar a polilinha ligando os pontos fornecidos
        for i in range(len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            bresenham(x0, y0, x1, y1, canvas)
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
root.title("Polilinha")

# Entrada para os pontos da polilinha
tk.Label(root, text="Pontos (X,Y) separados por ponto e vírgula (Ex: 0,0; 5,3; -2,1):").grid(row=0, column=0)
entry_points = tk.Entry(root, width=50)
entry_points.grid(row=0, column=1)

# Botão para desenhar a polilinha
draw_polyline_button = tk.Button(root, text="Desenhar Polilinha", command=draw_polyline)
draw_polyline_button.grid(row=1, column=0, columnspan=2)

# Canvas para o desenho
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=2, column=0, columnspan=2)

# Desenhar a grade inicial
draw_grid(canvas)

root.mainloop()
