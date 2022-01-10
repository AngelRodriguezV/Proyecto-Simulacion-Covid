from tkinter import Menubutton, Tk, Frame, font, ttk, Label, Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Creamos la ventana
root = Tk()
root.title("Simulación de COVID-19 México") # Establecemos el titulo
root.geometry("1000x650") # ancho x alto
root.configure(background='#CCCCCC')

fontStyle = font.Font(family="Calibri",size=12) # Fuente de letra
barra = Frame(root,background='#1E1E1E',width=1000,height=30) # MenuBar
barra.place(x=0,y=0) # Establecemos la posicion de la barra
# Creamos un submenu
menubar = Menubutton(barra,text="Archivo",background='#1E1E1E',foreground='#CCCCCC',activebackground='#505050',activeforeground='#CCCCCC',font=fontStyle)
menubar.place(x=1,y=1) # Establecemos la posicion del submenu
menubar.menu = Menu(menubar, tearoff=0)
menubar["menu"] = menubar.menu
# Establecemos las opciones del submenu y sus funciones
menubar.menu.add_command(label="Cargar",font=fontStyle,activebackground='#094771',activeforeground='#CCCCCC')
menubar.menu.add_command(label="Salir",font=fontStyle,activebackground='#094771',activeforeground='#CCCCCC')

s = ttk.Style()
s.configure("TNotebook")
notebook = ttk.Notebook(root,width=980,height=510)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1,text='SIR')
notebook.add(tab2,text='Logístico')
notebook.add(tab3,text='Gompertz')
notebook.grid(padx=10,pady=100)

root.mainloop()