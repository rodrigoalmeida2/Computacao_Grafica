import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageFilter

# Função para carregar a imagem
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global original_image
        original_image = Image.open(file_path)
        show_image(original_image)

# Função para exibir a imagem no canvas
def show_image(image):
    # Ajusta o tamanho da imagem para exibição
    resized_image = image.resize((300, 300))
    img_tk = ImageTk.PhotoImage(resized_image)
    canvas.image = img_tk  # Salva referência para evitar coleta de lixo
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

# Função para exibir imagem em RGB
def show_rgb():
    if original_image:
        show_image(original_image)

# Função para converter a imagem para tons de cinza
def show_gray():
    if original_image:
        gray_image = ImageOps.grayscale(original_image)
        show_image(gray_image)

# Função para converter a imagem para binária
def show_binary():
    if original_image:
        gray_image = ImageOps.grayscale(original_image)
        binary_image = gray_image.point(lambda p: 255 if p > 128 else 0)  # Binarização simples
        show_image(binary_image)


# Interface principal
root = tk.Tk()
root.title("Processamento de Imagens")

# Botão para carregar a imagem
load_button = tk.Button(root, text="Carregar Imagem", command=load_image)
load_button.grid(row=0, column=0, columnspan=2)

# Canvas para exibir a imagem
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=1, column=0, rowspan=5)

# Botões para as transformações
rgb_button = tk.Button(root, text="RGB", command=show_rgb)
rgb_button.grid(row=1, column=1)

gray_button = tk.Button(root, text="Tom de Cinza", command=show_gray)
gray_button.grid(row=2, column=1)

binary_button = tk.Button(root, text="Binária", command=show_binary)
binary_button.grid(row=3, column=1)

# Inicializa a variável da imagem
original_image = None

root.mainloop()
