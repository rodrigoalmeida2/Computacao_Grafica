import tkinter as tk
import subprocess
import os


# Função para executar um script
def run_script(script_name):
    try:
        # Caminho absoluto do script (ajuste conforme necessário)
        script_path = os.path.join(os.getcwd(), script_name)
        # Executa o script
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar {script_name}: {e}")

# Criação da interface Tkinter
root = tk.Tk()
root.title("Executar Scripts do Projeto")

# Botões para executar os scripts
button_script1 = tk.Button(root, text="Bresennham", command=lambda: run_script('primitivas_grafica/Linha_Bresenham.py'))
button_script1.pack(pady=10)

button_script3 = tk.Button(root, text="Polilinha e Preenchimento Recursivo", command=lambda: run_script('primitivas_grafica/recursiva.py'))
button_script3.pack(pady=10)

button_script3 = tk.Button(root, text="Recorte", command=lambda: run_script('primitivas_grafica/recorte.py'))
button_script3.pack(pady=10)

button_script3 = tk.Button(root, text="Transformações", command=lambda: run_script('primitivas_grafica/Transformacoes.py'))
button_script3.pack(pady=10)

button_script3 = tk.Button(root, text="Projeções", command=lambda: run_script('primitivas_grafica/projecoes.py'))
button_script3.pack(pady=10)



# Iniciar a interface
root.mainloop()
