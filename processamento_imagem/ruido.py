import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter

# Função para carregar a imagem
def load_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        global original_image
        original_image = Image.open(file_path)
        show_image(original_image)

# Função para exibir a imagem no canvas
def show_image(image):
    resized_image = image.resize((300, 300))
    img_tk = ImageTk.PhotoImage(resized_image)
    canvas.image = img_tk
    canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

# Filtros de remoção de ruído
# Mediana
def apply_median():
    if original_image:
        noise_free_image = original_image.filter(ImageFilter.MedianFilter(size=3))
        show_image(noise_free_image)

# Gaussiana
def apply_gaussian():
    if original_image:
        noise_free_image = original_image.filter(ImageFilter.GaussianBlur(radius=3))
        show_image(noise_free_image)

# Média
def MeanFilter():
    if original_image:
        noise_free_image = original_image.filter(ImageFilter.BoxBlur(radius=1))
        show_image(noise_free_image)


# Interface principal
root = tk.Tk()
root.title("Remoção de Ruído")

# Botão para carregar a imagem
load_button = tk.Button(root, text="Carregar Imagem", command=load_image)
load_button.grid(row=0, column=0, columnspan=2)

# Canvas para exibir a imagem
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.grid(row=1, column=0, rowspan=5)

# Botões para aplicar filtros
median_button = tk.Button(root, text="Mediana", command=apply_median)
median_button.grid(row=3, column=1)

gaussian_button = tk.Button(root, text="Gaussiana", command=apply_gaussian)
gaussian_button.grid(row=4, column=1)

mean_button = tk.Button(root, text="média", command=MeanFilter)
mean_button.grid(row=2, column=1)

# Inicializa a variável da imagem
original_image = None

root.mainloop()
