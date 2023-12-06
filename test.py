import customtkinter
import os
import tkinter as tk
from tkinter import font
from tkinter import filedialog
from PIL import Image, ImageTk  # Certifique-se de ter o módulo Pillow instalado (pip install Pillow)
import cv2 as cv
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")
app.title("SIP - Snake Image Processing")
path = os.path.abspath("logo.ico")
app.iconbitmap(path)

def openImage():
    # Abrir a caixa de diálogo para escolher o arquivo de imagem
    
    caminho_imagem = customtkinter.filedialog.askopenfilename(title="Escolher Imagem", filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

    # Verificar se o usuário escolheu um arquivo
    if caminho_imagem:
        global img # Variável global para armazenar a imagem
        # Atualizar a imagem exibida na interface gráfica
        imagem = customtkinter.Ctk.Image.open(caminho_imagem)
        imagem = imagem.resize((300, 300), Image.ANTIALIAS)  # Redimensionar a imagem conforme necessário
        imagem = ImageTk.PhotoImage(imagem)
        painel_imagem.config(image=imagem)
        painel_imagem.imagem = imagem
        label.config(text=f"Imagem selecionada: {os.path.basename(caminho_imagem)}")
        img = cv.imread(caminho_imagem)

# Função a ser chamada quando o botão for pressionado
def convolution():
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

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Convolução", command=convolution, font=customtkinter.CTkFont(size=13, weight="bold"))
button.place(relx=0.7, rely=0.8, anchor=customtkinter.CENTER)
button2 = customtkinter.CTkButton(master=app, text="Carregar Imagem", command=openImage, font=customtkinter.CTkFont(size=13, weight="bold"))
button2.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
button3 = customtkinter.CTkButton(master=app, text="Histograma", command=hist, font=customtkinter.CTkFont(size=13, weight="bold"))
button3.place(relx=0.3, rely=0.8, anchor=customtkinter.CENTER)

path = os.path.abspath("image.png")

iconCam = customtkinter.CTkImage(Image.open(os.path.join(path)), size=(50, 50))

imageIcon = customtkinter.CTkLabel(app, text="")
imageIcon.configure(image=iconCam)
imageIcon.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

painel_imagem = customtkinter.CTkLabel(app)

label = customtkinter.CTkLabel(app, text="Nenhuma imagem selecionada")
label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER);

rodape = customtkinter.CTkLabel(app, text="© 2023 SIP - Snake Image Processing", font=("Inter", 10), pady=10)
rodape.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()