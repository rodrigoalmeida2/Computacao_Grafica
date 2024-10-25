
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
    
    # Função para desenhar o sistema de coordenadas
    def draw_grid(canvas):
        # Desenhar eixo x e y
        canvas.create_line(0, 220, 440, 220, fill="gray")  # Eixo X
        canvas.create_line(220, 0, 220, 440, fill="gray")  # Eixo Y
        # Desenhar linhas de grade
        for i in range(0, 440, 20):
            canvas.create_line(i, 0, i, 440, fill="lightgray")
            canvas.create_line(0, i, 440, i, fill="lightgray")

