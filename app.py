import customtkinter
import os
from PIL import Image  # Certifique-se de ter o módulo Pillow instalado (pip install Pillow)
import cv2 as cv
import matplotlib.pyplot as plt

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")
app.title("SIP - Snake Image Processing")
path = os.path.abspath("./img/logo.ico")
app.iconbitmap(path)
  
def openImage():
    # Abrir a caixa de diálogo para escolher o arquivo de imagem
    
    caminho_imagem = customtkinter.filedialog.askopenfilename(title="Escolher Imagem", filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

    # Verificar se o usuário escolheu um arquivo
    if caminho_imagem:
        global img
        img = cv.imread(caminho_imagem)
        lab = customtkinter.CTkLabel(app, text="\t",  font=customtkinter.CTkFont(size=32))
        lab.place(relx=0.85, rely=0.2, anchor=customtkinter.CENTER)
       
        # Atualizar a imagem exibida na interface gráfica
        imagem = customtkinter.CTkImage(Image.open(caminho_imagem), size=(300, 300))
        painel_imagem.configure(image=imagem, text="")
        painel_imagem.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)

        label.configure(text=f"Imagem selecionada: {os.path.basename(caminho_imagem)}",text_color=("gray75"))
        label.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

def verifyFilter(imgConv):
    global menu # Variável global para armazenar o menu
   
    if menu.get() == "Sobel":
        imgSobel = cv.Sobel(imgConv, cv.CV_64F, 0, 1, ksize=3)
        cv.imshow("Imagem filtrada", imgSobel)
        cv.waitKey(0)
    elif menu.get() == "Galssiano":
        imgGaussian = cv.GaussianBlur(imgConv, (5,5), 0)
        cv.imshow("Imagem filtrada", imgGaussian)
        cv.waitKey(0)
    elif menu.get() == "MediaBlur":
        imgBlur = cv.blur(imgConv, (5,5))
        cv.imshow("Imagem filtrada", imgBlur)
        cv.waitKey(0)
    elif menu.get() == "Laplace":
        imgLaplace = cv.Laplacian(imgConv, cv.CV_64F)
        cv.imshow("Imagem filtrada", imgLaplace)
        cv.waitKey(0)
        
# Função a ser chamada quando o botão for pressionado
def convolution():
    try:
        global img # Variável global para armazenar a imagem
        global menu # Variável global para armazenar o menu
        imgConv = img

        menu = customtkinter.CTkOptionMenu(app, values=["Select", "Sobel", "Galssiano", "MediaBlur", "Laplace"], command= lambda value: verifyFilter(imgConv))
        menu.place(relx=0.85, rely=0.2, anchor=customtkinter.CENTER)
    except Exception as e:
        print(e)
        label.configure(text="Error, nenhuma imagem associada!",  text_color=("red"))


def hist():
    try:
        global img # Variável global para armazenar a imagem
        imgHist = img
        vals = imgHist.mean(axis=2).flatten()
        b, bins, patches = plt.hist(vals, 255)
        plt.xlim([0,255])
        plt.show()
        
        imgHist = cv.cvtColor(imgHist, cv.COLOR_BGR2GRAY)
        imgEqualize = cv.equalizeHist(imgHist)
        cv.imshow("Imagem equalizada", imgEqualize)
        cv.waitKey(0)

        valsEqualize = imgEqualize.mean(axis=1).flatten()
        b, bins, patches = plt.hist(valsEqualize, 255)
        plt.xlim([0,255])
        plt.show()

        lab = customtkinter.CTkLabel(app, text="\t",  font=customtkinter.CTkFont(size=32))
        lab.place(relx=0.9, rely=0.1, anchor=customtkinter.CENTER)
    except Exception as e:
        print(e)
        label.configure(text="Error, nenhuma imagem associada!",  text_color=("red"))

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Convolução", command=convolution, font=customtkinter.CTkFont(size=13, weight="bold"))
button.place(relx=0.7, rely=0.8, anchor=customtkinter.CENTER)
button2 = customtkinter.CTkButton(master=app, text="Carregar Imagem", command=openImage, font=customtkinter.CTkFont(size=13, weight="bold"))
button2.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
button3 = customtkinter.CTkButton(master=app, text="Histograma", command=hist, font=customtkinter.CTkFont(size=13, weight="bold"))
button3.place(relx=0.3, rely=0.8, anchor=customtkinter.CENTER)

path = os.path.abspath("./img/image.png")

iconCam = customtkinter.CTkImage(Image.open(os.path.join(path)), size=(50, 50))

imageIcon = customtkinter.CTkLabel(app, text="")
imageIcon.configure(image=iconCam)
imageIcon.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

painel_imagem = customtkinter.CTkLabel(app)

label = customtkinter.CTkLabel(app, text="Nenhuma imagem selecionada")
label.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

rodape = customtkinter.CTkLabel(app, text="© 2023 SIP - Snake Image Processing", font=("Inter", 10), pady=10)
rodape.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()