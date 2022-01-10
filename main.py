from tkinter import Tk, Frame, font, ttk, Label, Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Creamos la ventana
root = Tk()
root.title("Simulación de COVID-19 México") # Establecemos el titulo
root.geometry("1000x650") # ancho x alto

menubar = Menu(root,selectcolor="black") # Inicializamos el menu
filemenu = Menu(menubar, tearoff=0) # Inicializamos un submenu para archivo
filemenu.add_command(label="Abrir") # Añadimos la etiqueta para abrir un archivo y su funcion
filemenu.add_separator()
filemenu.add_command(label="Salir",command=root.quit) # Añadimos una opción para salir
menubar.add_cascade(label="Archivo",menu=filemenu) # Agregamos el submenu de archivo
root.config(menu=menubar) # Mostramos el menu

notebook = ttk.Notebook(root,width=980,height=510)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1,text='SIR')
notebook.add(tab2,text='Logístico')
notebook.add(tab3,text='Gompertz')
notebook.grid(padx=10,pady=100)

root.mainloop()