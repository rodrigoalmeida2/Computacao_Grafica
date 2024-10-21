import tkinter as tk

# Códigos de região para Cohen-Sutherland
INSIDE = 0  # 0000
LEFT = 1    # 0001
RIGHT = 2   # 0010
BOTTOM = 4  # 0100
TOP = 8     # 1000

# Definindo a área de recorte (janela)
x_min, y_min = 2, 2  # Canto inferior esquerdo da janela de recorte
x_max, y_max = 8, 8  # Canto superior direito da janela de recorte

# Função para calcular o código de região (outcode) de um ponto
def compute_outcode(x, y):
    code = INSIDE
    if x < x_min:  # à esquerda da janela
        code |= LEFT
    elif x > x_max:  # à direita da janela
        code |= RIGHT
    if y < y_min:  # abaixo da janela
        code |= BOTTOM
    elif y > y_max:  # acima da janela
        code |= TOP
    return code

# Função para recortar a linha usando o algoritmo de Cohen-Sutherland
def cohen_sutherland_line_clip(x0, y0, x1, y1):
    outcode0 = compute_outcode(x0, y0)
    outcode1 = compute_outcode(x1, y1)
    accept = False

    while True:
        if outcode0 == 0 and outcode1 == 0:  # Ambos os pontos dentro da janela
            accept = True
            break
        elif outcode0 & outcode1 != 0:  # Ambos os pontos estão fora e na mesma região
            break
        else:
            # Pelo menos um ponto está fora, então encontramos a interseção
            outcode_out = outcode0 if outcode0 != 0 else outcode1
            x, y = 0, 0

            # Caso de interseção no topo ou embaixo
            if outcode_out & TOP:  # Ponto acima da janela
                if y1 != y0:
                    x = x0 + (x1 - x0) * (y_max - y0) / (y1 - y0)
                y = y_max
            elif outcode_out & BOTTOM:  # Ponto abaixo da janela
                if y1 != y0:
                    x = x0 + (x1 - x0) * (y_min - y0) / (y1 - y0)
                y = y_min
            # Caso de interseção à direita ou esquerda
            elif outcode_out & RIGHT:  # Ponto à direita da janela
                if x1 != x0:
                    y = y0 + (y1 - y0) * (x_max - x0) / (x1 - x0)
                x = x_max
            elif outcode_out & LEFT:  # Ponto à esquerda da janela
                if x1 != x0:
                    y = y0 + (y1 - y0) * (x_min - x0) / (x1 - x0)
                x = x_min

            # Atualiza o ponto fora para a nova interseção e recalcula o código de região
            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_outcode(x0, y0)
            else:
                x1, y1 = x, y
                outcode1 = compute_outcode(x1, y1)

    if accept:
        # Desenha a linha recortada (somente a parte dentro da janela)
        bresenham_line(x0, y0, x1, y1)

# Função para desenhar uma linha usando o algoritmo de Bresenham
def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        # Desenhar o ponto
        canvas.create_rectangle(x0 * 20, y0 * 20, (x0 + 1) * 20, (y0 + 1) * 20, fill="green", outline="green")
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

# Função para desenhar o retângulo da área de recorte (janela)
def draw_clip_window():
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, outline="red")

# Função para inicializar a interface gráfica
def initialize():
    global canvas
    window = tk.Tk()
    window.title("Recorte de Linha - Cohen-Sutherland")
    
    canvas = tk.Canvas(window, width=440, height=440)
    canvas.pack()

    # Desenhar a área de recorte
    draw_clip_window()

    # Exemplo de linha a ser recortada
    cohen_sutherland_line_clip(-5, -5, 10, 10)  # Uma linha fora da área de recorte

    window.mainloop()

# Executar o programa
initialize()
