import cv2
import numpy as np
import matplotlib.pyplot as plt

def aplicar_filtro_media(img, kernel_size):
    rows, cols = img.shape
    output = np.zeros_like(img)

    offset = kernel_size // 2

    for i in range(offset, rows - offset):
        for j in range(offset, cols - offset):
            sum = 0
            for k in range(-offset, offset + 1):
                for l in range(-offset, offset + 1):
                    sum += img[i+k, j+l]
            output[i, j] = sum / (kernel_size * kernel_size)

    return output

def aplicar_filtro_mediana(img, kernel_size):
    rows, cols = img.shape
    output = np.zeros_like(img)

    offset = kernel_size // 2

    for i in range(offset, rows - offset):
        for j in range(offset, cols - offset):
            neighborhood = []
            for k in range(-offset, offset + 1):
                for l in range(-offset, offset + 1):
                    neighborhood.append(img[i+k, j+l])
            neighborhood.sort()
            output[i, j] = neighborhood[len(neighborhood) // 2]

    return output

def aplicar_filtro_gaussiano(img, kernel_size, sigma):
    # Criação do kernel gaussiano
    kernel = np.zeros((kernel_size, kernel_size))
    m, n = divmod(kernel_size, 2)
    y, x = np.ogrid[-m:m+1, -n:n+1]
    kernel = np.exp(-(x*x + y*y) / (2.0 * sigma*sigma))
    kernel = kernel / kernel.sum()

    # Aplicação do filtro
    return cv2.filter2D(img, -1, kernel)

# Carregar a imagem
img = cv2.imread('imagens_ruido\Ruido3.bmp', 0)

# Aplicar os filtros
img_media = aplicar_filtro_media(img, 5)
img_mediana = aplicar_filtro_mediana(img, 5)
img_gaussiana = aplicar_filtro_gaussiano(img, 5, 1)

# Mostrar as imagens
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(1, 4, 2), plt.imshow(img_media, cmap='gray'), plt.title('Média')
plt.subplot(1, 4, 3), plt.imshow(img_mediana, cmap='gray'), plt.title('Mediana')
plt.subplot(1, 4, 4), plt.imshow(img_gaussiana, cmap='gray'), plt.title('Gaussiana')
plt.show()