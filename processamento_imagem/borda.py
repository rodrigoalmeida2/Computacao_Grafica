import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2

# Função para carregar a imagem
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global original_image, original_image_cv
        original_image = Image.open(file_path)
        original_image_cv = cv2.cvtColor(np.array(original_image), cv2.COLOR_RGB2GRAY)  # Converte para tons de cinza
        show_image(original_image)

# Função para exibir a imagem no canvas
def show_image(image):
    # Ajusta o tamanho da imagem para exibição
    resized_image = image.resize((300, 300))
    img_tk = ImageTk.PhotoImage(resized_image)
    canvas.image = img_tk  # Salva referência para evitar coleta de lixo
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

# Função para aplicar o filtro Sobel
def apply_sobel():
    if original_image_cv is not None:
        # Aplica filtro Sobel para detecção de bordas
        sobel_x = cv2.Sobel(original_image_cv, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(original_image_cv, cv2.CV_64F, 0, 1, ksize=3)
        sobel = cv2.magnitude(sobel_x, sobel_y)
        sobel = np.uint8(np.clip(sobel * 0.25, 0, 255))  # Ajuste de intensidade
        sobel_image = Image.fromarray(sobel)
        show_image(sobel_image)

# Função para aplicar o filtro Prewitt
def apply_prewitt():
    if original_image_cv is not None:
        # Aplica o filtro Prewitt para detecção de bordas
        kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
        kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)

        prewitt_x = cv2.filter2D(original_image_cv, cv2.CV_64F, kernelx)
        prewitt_y = cv2.filter2D(original_image_cv, cv2.CV_64F, kernely)
        
        prewitt = cv2.magnitude(prewitt_x, prewitt_y)
        prewitt = np.uint8(np.clip(prewitt * 0.25, 0, 255))  # Ajuste de intensidade
        prewitt_image = Image.fromarray(prewitt)
        show_image(prewitt_image)

# Função para aplicar o filtro Canny
def apply_canny():
    if original_image_cv is not None:
        # Aplica o filtro Canny para detecção de bordas
        canny = cv2.Canny(original_image_cv, 100, 200)
        canny_image = Image.fromarray(canny)
        show_image(canny_image)

# Interface principal
root = tk.Tk()
root.title("Destaque de Bordas em Imagens")

# Botão para carregar a imagem
load_button = tk.Button(root, text="Carregar Imagem", command=load_image)
load_button.grid(row=0, column=0, columnspan=2)

# Canvas para exibir a imagem
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=1, column=0, rowspan=3)

# Botões para as transformações
sobel_button = tk.Button(root, text="Filtro Sobel", command=apply_sobel)
sobel_button.grid(row=1, column=1)

prewitt_button = tk.Button(root, text="Filtro Prewitt", command=apply_prewitt)
prewitt_button.grid(row=2, column=1)

canny_button = tk.Button(root, text="Filtro Canny", command=apply_canny)
canny_button.grid(row=3, column=1)

# Inicializa a variável da imagem
original_image = None
original_image_cv = None

root.mainloop()
