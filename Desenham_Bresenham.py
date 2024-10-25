import tkinter as tk
from Bresenham import bresenham as bs

# Função para desenhar a linha entre os pontos selecionados
def draw_line():
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        
        canvas.delete("all")  # Limpar o canvas
        # Desenhar sistema de coordenadas
        bs.draw_grid(canvas)
        # Desenhar linha usando o algoritmo de Bresenham
        bs.bresenham_line(x1, y1, x2, y2, canvas)
    except ValueError:
        pass  # Ignorar entradas inválidas

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
bs.draw_grid(canvas)

root.mainloop()
