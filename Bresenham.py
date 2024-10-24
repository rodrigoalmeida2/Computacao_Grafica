import tkinter as tk

class bresenham:
    # Função do Algoritmo de Bresenham para desenhar uma linha com quadrados coloridos
    def bresenham_line(x1, y1, x2, y2, canvas):
        # Conversão para as coordenadas do canvas (considera 11 x 11 quadrantes com centro em (0, 0))
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
            canvas.create_rectangle(x1 * 20, y1 * 20, (x1 + 1) * 20, (y1 + 1) * 20, fill="red")
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x1 += sx
            if e2 < dx:
                err += dx
                y1 += sy

bs = bresenham
# Função para desenhar a linha entre os pontos selecionados
def draw_line():
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        
        canvas.delete("all")  # Limpar o canvas
        # Desenhar sistema de coordenadas
        draw_grid(canvas)
        # Desenhar linha usando o algoritmo de Bresenham
        bs.bresenham_line(x1, y1, x2, y2, canvas)
    except ValueError:
        pass  # Ignorar entradas inválidas

# Função para desenhar o sistema de coordenadas
def draw_grid(canvas):
    # Desenhar eixo x e y
    canvas.create_line(0, 220, 440, 220, fill="gray")  # Eixo X
    canvas.create_line(220, 0, 220, 440, fill="gray")  # Eixo Y
    # Desenhar linhas de grade
    for i in range(0, 440, 20):
        canvas.create_line(i, 0, i, 440, fill="lightgray")
        canvas.create_line(0, i, 440, i, fill="lightgray")

# Interface principal
root = tk.Tk()
root.title("Desenho de Linha com Bresenham (Quadrados Coloridos)")

# Entrada de coordenadas
tk.Label(root, text="x1:").grid(row=0, column=0)
entry_x1 = tk.Entry(root)
entry_x1.grid(row=0, column=1)

tk.Label(root, text="y1:").grid(row=0, column=2)
entry_y1 = tk.Entry(root)
entry_y1.grid(row=0, column=3)

tk.Label(root, text="x2:").grid(row=1, column=0)
entry_x2 = tk.Entry(root)
entry_x2.grid(row=1, column=1)

tk.Label(root, text="y2:").grid(row=1, column=2)
entry_y2 = tk.Entry(root)
entry_y2.grid(row=1, column=3)

# Botão para desenhar a linha
draw_button = tk.Button(root, text="Desenhar Linha", command=draw_line)
draw_button.grid(row=2, column=1, columnspan=2)

# Canvas para desenhar o sistema de coordenadas e a linha
canvas = tk.Canvas(root, width=440, height=440, bg="white")
canvas.grid(row=3, column=0, columnspan=4)

# Desenhar a grade e os eixos iniciais
draw_grid(canvas)

root.mainloop()

