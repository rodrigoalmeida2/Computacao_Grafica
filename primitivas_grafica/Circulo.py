import tkinter as tk
from Bresenham import bresenham as bs

# Algoritmo para desenhar um círculo usando o algoritmo de Midpoint Circle
def draw_circle():
    try:
        cx = int(entry_cx.get())
        cy = int(entry_cy.get())
        r = int(entry_r.get())
        
        canvas.delete("all")  # Limpar o canvas
        bs.draw_grid(canvas)
    except ValueError:
        pass  # Ignorar entradas inválidas
    # Ajuste para o centro (cx, cy) considerando o sistema de coordenadas
    cx = cx + 11
    cy = 11 - cy

    x = 0
    y = r
    d = 1 - r

    draw_circle_points(cx, cy, x, y)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1
        x += 1
        draw_circle_points(cx, cy, x, y)

# Função auxiliar para desenhar os 8 pontos simétricos do círculo
def draw_circle_points(cx, cy, x, y):
    points = [
        (cx + x, cy + y), (cx - x, cy + y), (cx + x, cy - y), (cx - x, cy - y),
        (cx + y, cy + x), (cx - y, cy + x), (cx + y, cy - x), (cx - y, cy - x)
    ]
    for px, py in points:
        canvas.create_rectangle(px * 20, py * 20, (px + 1) * 20, (py + 1) * 20, fill="red")

# Algoritmo para desenhar uma elipse usando o algoritmo de Midpoint Ellipse
def draw_ellipse(cx, cy, rx, ry):
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
        draw_ellipse_points(cx, cy, x, y)
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
        draw_ellipse_points(cx, cy, x, y)
        y -= 1
        py -= tworx2
        if p > 0:
            p += rx2 - py
        else:
            x += 1
            px += twory2
            p += rx2 - py + px

# Função auxiliar para desenhar os 4 pontos simétricos da elipse
def draw_ellipse_points(cx, cy, x, y):
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
        bs.draw_grid(canvas)
        draw_ellipse(cx, cy, rx, ry)
    except ValueError:
        pass  # Ignorar entradas inválidas

# Interface gráfica
root = tk.Tk()
root.title("Desenho de Círculo")

# Entradas para o círculo
tk.Label(root, text="Centro X:").grid(row=0, column=0)
entry_cx = tk.Entry(root)
entry_cx.grid(row=0, column=1)

tk.Label(root, text="Centro Y:").grid(row=0, column=2)
entry_cy = tk.Entry(root)
entry_cy.grid(row=0, column=3)

tk.Label(root, text="Raio:").grid(row=1, column=0)
entry_r = tk.Entry(root)
entry_r.grid(row=1, column=1)

# Entradas para a elipse
tk.Label(root, text="Raio X:").grid(row=2, column=0)
entry_rx = tk.Entry(root)
entry_rx.grid(row=2, column=1)

tk.Label(root, text="Raio Y:").grid(row=2, column=2)
entry_ry = tk.Entry(root)
entry_ry.grid(row=2, column=3)

# Botão para desenhar a elipse
draw_ellipse_button = tk.Button(root, text="Desenhar Elipse", command=draw_ellipse_ui)
draw_ellipse_button.grid(row=3, column=0, columnspan=2)

# Botão para desenhar o círculo
draw_circle_button = tk.Button(root, text="Desenhar Círculo", command=draw_circle)
draw_circle_button.grid(row=3, column=2, columnspan=2)


# Canvas para o desenho
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=4, column=0, columnspan=4)

# Desenhar a grade inicial
bs.draw_grid(canvas)

root.mainloop()
