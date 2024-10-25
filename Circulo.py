import tkinter as tk
from Bresenham import bresenham as bs

# Algoritmo para desenhar um círculo usando o algoritmo de Midpoint Circle
def draw_circle(cx, cy, r, canvas):
    # Ajuste para o centro (cx, cy) considerando o sistema de coordenadas
    cx = cx + 11
    cy = 11 - cy

    x = 0
    y = r
    d = 1 - r

    draw_circle_points(cx, cy, x, y, canvas)

    while x < y:
        if d < 0:
            d = d + 2 * x + 3
        else:
            d = d + 2 * (x - y) + 5
            y -= 1
        x += 1
        draw_circle_points(cx, cy, x, y, canvas)

# Função auxiliar para desenhar os 8 pontos simétricos do círculo
def draw_circle_points(cx, cy, x, y, canvas):
    points = [
        (cx + x, cy + y), (cx - x, cy + y), (cx + x, cy - y), (cx - x, cy - y),
        (cx + y, cy + x), (cx - y, cy + x), (cx + y, cy - x), (cx - y, cy - x)
    ]
    for px, py in points:
        canvas.create_rectangle(px * 20, py * 20, (px + 1) * 20, (py + 1) * 20, fill="red", outline="black")

# Função para desenhar o círculo com base nos parâmetros da interface
def draw_circle_ui():
    try:
        cx = int(entry_cx.get())
        cy = int(entry_cy.get())
        r = int(entry_r.get())
        
        canvas.delete("all")  # Limpar o canvas
        bs.draw_grid(canvas)
        draw_circle(cx, cy, r, canvas)
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

# Botão para desenhar o círculo
draw_circle_button = tk.Button(root, text="Desenhar Círculo", command=draw_circle_ui)
draw_circle_button.grid(row=2, column=0, columnspan=2)

# Canvas para o desenho
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=3, column=0, columnspan=4)

# Desenhar a grade inicial
bs.draw_grid(canvas)

root.mainloop()
