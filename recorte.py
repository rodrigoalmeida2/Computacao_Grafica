import tkinter as tk
from Bresenham import bresenham as bs

# Definindo a área de recorte (por exemplo, uma janela delimitada de 4x4 dentro do sistema de coordenadas 11x11)
CLIP_X_MIN = -4
CLIP_X_MAX = 4
CLIP_Y_MIN = -4
CLIP_Y_MAX = 4

# Função para calcular o código do ponto para o algoritmo de recorte Cohen-Sutherland
def compute_code(x, y):
    code = 0
    if x < CLIP_X_MIN:  # Esquerda da janela
        code |= 1
    elif x > CLIP_X_MAX:  # Direita da janela
        code |= 2
    if y < CLIP_Y_MIN:  # Abaixo da janela
        code |= 4
    elif y > CLIP_Y_MAX:  # Acima da janela
        code |= 8
    return code

# Algoritmo de recorte de linha de Cohen-Sutherland
def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)

    while True:
        if not (code1 | code2):  # Ambos os pontos estão dentro da janela
            return x1, y1, x2, y2
        elif code1 & code2:  # Ambos os pontos estão fora da janela
            return None  # Linha está completamente fora
        else:
            # Um dos pontos está fora da janela
            x, y = 0, 0
            code_out = code1 if code1 else code2

            # Verifica os limites e ajusta o ponto que está fora da janela
            if code_out & 8:  # Acima da janela
                x = x1 + (x2 - x1) * (CLIP_Y_MAX - y1) / (y2 - y1)
                y = CLIP_Y_MAX
            elif code_out & 4:  # Abaixo da janela
                x = x1 + (x2 - x1) * (CLIP_Y_MIN - y1) / (y2 - y1)
                y = CLIP_Y_MIN
            elif code_out & 2:  # Direita da janela
                y = y1 + (y2 - y1) * (CLIP_X_MAX - x1) / (x2 - x1)
                x = CLIP_X_MAX
            elif code_out & 1:  # Esquerda da janela
                y = y1 + (y2 - y1) * (CLIP_X_MIN - x1) / (x2 - x1)
                x = CLIP_X_MIN

            # Atualiza o ponto que estava fora
            if code_out == code1:
                x1, y1 = int(x), int(y)
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = int(x), int(y)
                code2 = compute_code(x2, y2)

# Função do Algoritmo de Bresenham para desenhar uma linha com recorte
def bresenham_line(x1, y1, x2, y2, canvas):
    clipped = cohen_sutherland_clip(x1, y1, x2, y2)
    if not clipped:
        return  # Não desenha se a linha está fora da janela

    x1, y1, x2, y2 = clipped

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        # Desenhar quadrado colorido no canvas (20x20 pixels para cada coordenada)
        canvas.create_rectangle((x1 + 11) * 20, (11 - y1) * 20, (x1 + 11 + 1) * 20, (11 - y1 + 1) * 20, fill="red")
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Função para desenhar a linha entre os pontos selecionados
def draw_line():
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        
        canvas.delete("all")  # Limpar o canvas
        bs.draw_grid(canvas)  # Desenhar sistema de coordenadas
        # Desenhar linha usando o algoritmo de Bresenham com recorte
        bresenham_line(x1, y1, x2, y2, canvas)
        draw_clip_area(canvas)  # Desenha a área de recorte
    except ValueError:
        pass  # Ignorar entradas inválidas

# Função para desenhar a área de recorte
def draw_clip_area(canvas):
    # Desenha um retângulo delimitando a área de recorte
    x_min_canvas = (CLIP_X_MIN + 11) * 20
    y_min_canvas = (11 - CLIP_Y_MAX) * 20
    x_max_canvas = (CLIP_X_MAX + 11) * 20
    y_max_canvas = (11 - CLIP_Y_MIN) * 20

    canvas.create_rectangle(x_min_canvas, y_min_canvas, x_max_canvas, y_max_canvas, outline="blue", width=2)

# Interface principal
root = tk.Tk()
root.title("Desenho de Linha com Recorte (Bresenham e Cohen-Sutherland)")

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
draw_clip_area(canvas)

root.mainloop()
