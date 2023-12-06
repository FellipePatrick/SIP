import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")
app.title("SIP - Snake Image Processing")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Convolução", command=button_function, font=customtkinter.CTkFont(size=13, weight="bold"))
button.place(relx=0.7, rely=0.8, anchor=customtkinter.CENTER)
button2 = customtkinter.CTkButton(master=app, text="Carregar Imagem", command=button_function, font=customtkinter.CTkFont(size=13, weight="bold"))
button2.place(relx=0.5, rely=0.8, anchor=customtkinter.CENTER)
button3 = customtkinter.CTkButton(master=app, text="Histograma", command=button_function, font=customtkinter.CTkFont(size=13, weight="bold"))
button3.place(relx=0.3, rely=0.8, anchor=customtkinter.CENTER)

rodape = customtkinter.CTkLabel(app, text="© 2023 SIP - Snake Image Processing", font=("Inter", 10), pady=10)
rodape.place(relx=0.5, rely=0.9, anchor=customtkinter.CENTER)

app.mainloop()