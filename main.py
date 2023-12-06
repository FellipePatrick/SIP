import os
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from PIL import Image, ImageTk  # Certifique-se de ter o módulo Pillow instalado (pip install Pillow)
import cv2 as cv
import matplotlib.pyplot as plt

def abrir_imagem():
    # Abrir a caixa de diálogo para escolher o arquivo de imagem
    caminho_imagem = filedialog.askopenfilename(title="Escolher Imagem", filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

    # Verificar se o usuário escolheu um arquivo
    if caminho_imagem:
        global img # Variável global para armazenar a imagem
        # Atualizar a imagem exibida na interface gráfica
        imagem = Image.open(caminho_imagem)
        imagem = imagem.resize((300, 300), Image.ANTIALIAS)  # Redimensionar a imagem conforme necessário
        imagem = ImageTk.PhotoImage(imagem)
        painel_imagem.config(image=imagem)
        painel_imagem.imagem = imagem
        label.config(text=f"Imagem selecionada: {os.path.basename(caminho_imagem)}")
        img = cv.imread(caminho_imagem)

# Função a ser chamada quando o botão for pressionado
def convolucao():
    label.config(text="Resultado da imagem filtrada")
    
    cv.imshow("Imagem filtrada", img)
    cv.waitKey(0)

def hist():
    label.config(text="Resultado da imagem equalizada")
    vals = img.mean(axis=2).flatten()
    # plot histogram with 255 bins
    b, bins, patches = plt.hist(vals, 255)
    plt.xlim([0,255])
    plt.show()

# Criar a janela principal
janela = tk.Tk()
janela.title("SIP - Snake Image Processing")
# Obter o caminho absoluto para o arquivo logo.ico
caminho_logo = os.path.abspath("logo.ico")

# Definir as dimensões da janela (largura x altura + posição x + posição y)
janela.geometry("800x700")

# Adicionar um ícone à janela
janela.iconbitmap(caminho_logo)

# Adicionar botões à janela com estilização
botao_conv = tk.Button(janela, text="Convolução da Imagem", command=convolucao)
# botao_conv.pack(side=tk.LEFT, padx=20)

botao_hist = tk.Button(janela, text="Histograma da Imagem", command=hist)
# botao_hist.pack(side=tk.LEFT, padx = 20)

# Adicionar um botão para abrir a caixa de diálogo de seleção de imagem
botao_abrir_imagem = tk.Button(janela, text="Abrir Imagem", command=abrir_imagem)
# botao_abrir_imagem.pack(side=tk.LEFT, padx=20)

# Adicionar um rótulo para exibir o nome da imagem selecionada
label = tk.Label(janela, text="Nenhuma imagem selecionada.")
# label.pack(side= tk.LEFT,pady=10, anchor=tk.NE, padx=2)

# Adicionar um espaço vazio para melhorar o layout
# tk.Label(janela, text="").pack()

# Adicionar um painel para exibir a imagem
painel_imagem = tk.Label(janela)
# painel_imagem.pack(side=tk.RIGHT, pady=20, anchor=tk.NE, padx=2)

# Adicionar um rodapé
rodape = tk.Label(janela, text="© 2023 SIP - Snake Image Processing", font=("Helvetica", 8), pady=10)
# rodape.pack(side=tk.BOTTOM)

botao_abrir_imagem.grid(row=0, column=0, padx=10, pady=10)
botao_conv.grid(row=1, column=0, padx=10, pady=10)
botao_hist.grid(row=2, column=0, columnspan=2, pady=10)
painel_imagem.grid(row=3, column=5, columnspan=2, pady=0,padx=100)

# Iniciar o loop principal da aplicação
janela.mainloop()
