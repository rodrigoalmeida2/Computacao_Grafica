import tkinter as tk

# Algoritmo para desenhar uma elipse usando o algoritmo de Midpoint Ellipse
def draw_ellipse(cx, cy, rx, ry, canvas):
    # Ajuste para o centro (cx, cy) no sistema de coordenadas
    cx = cx + 11
    cy = 11 - cy

    x = 0
    y = ry
    rx2 = rx * rx
    ry2 = ry * ry
    tworx2 = 2 * rx2
    twory2 = 2 * ry2
    px = 0
    py = tworx2 * y

    # Região 1
    p = round(ry2 - (rx2 * ry) + (0.25 * rx2))
    while px < py:
        draw_ellipse_points(cx, cy, x, y, canvas)
        x += 1
        px += twory2
        if p < 0:
            p += ry2 + px
        else:
            y -= 1
            py -= tworx2
            p += ry2 + px - py

    # Região 2
    p = round(ry2 * (x + 0.5) ** 2 + rx2 * (y - 1) ** 2 - rx2 * ry2)
    while y > 0:
        draw_ellipse_points(cx, cy, x, y, canvas)
        y -= 1
        py -= tworx2
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += twory2
            p += rx2 - py + px

# Função auxiliar para desenhar os 4 pontos simétricos da elipse
def draw_ellipse_points(cx, cy, x, y, canvas):
    points = [
        (cx + x, cy + y), (cx - x, cy + y), (cx + x, cy - y), (cx - x, cy - y)
    ]
    for px, py in points:
        canvas.create_rectangle(px * 20, py * 20, (px + 1) * 20, (py + 1) * 20, fill="blue", outline="black")

# Função para desenhar a elipse com base nos parâmetros da interface
def draw_ellipse_ui():
    try:
        cx = int(entry_cx.get())
        cy = int(entry_cy.get())
        rx = int(entry_rx.get())
        ry = int(entry_ry.get())
        
        canvas.delete("all")  # Limpar o canvas
        draw_grid(canvas)
        draw_ellipse(cx, cy, rx, ry, canvas)
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
root.title("Desenho de Elipse")

# Entradas para a elipse
tk.Label(root, text="Centro X:").grid(row=0, column=0)
entry_cx = tk.Entry(root)
entry_cx.grid(row=0, column=1)

tk.Label(root, text="Centro Y:").grid(row=0, column=2)
entry_cy = tk.Entry(root)
entry_cy.grid(row=0, column=3)

tk.Label(root, text="Raio X:").grid(row=1, column=0)
entry_rx = tk.Entry(root)
entry_rx.grid(row=1, column=1)

tk.Label(root, text="Raio Y:").grid(row=1, column=2)
entry_ry = tk.Entry(root)
entry_ry.grid(row=1, column=3)

# Botão para desenhar a elipse
draw_ellipse_button = tk.Button(root, text="Desenhar Elipse", command=draw_ellipse_ui)
draw_ellipse_button.grid(row=2, column=0, columnspan=2)

# Canvas para o desenho
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=3, column=0, columnspan=4)

# Desenhar a grade inicial
draw_grid(canvas)

root.mainloop()
