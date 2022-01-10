from tkinter import Menubutton, Tk, Frame, font, ttk, Label, Menu
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importando mis clases
import leerDatos as lDt
import estado

class  App:
    listEstado = []
    listNomE = []
    
    def __init__(self,master:Tk) -> None:
        self.master = master
        # Configuracion del master
        self.master.configure(background='#CCCCCC')
        # Cargamos los datos predeterminados
        self.Cargar()
        fontStyle = font.Font(family="Calibri",size=12) # Fuente de letra
        barra = Frame(self.master,background='#1E1E1E',width=1000,height=30) # MenuBar
        barra.place(x=0,y=0) # Establecemos la posicion de la barra
        # Creamos un submenu
        menubar = Menubutton(barra,text="Archivo",background='#1E1E1E',foreground='#CCCCCC',activebackground='#505050',activeforeground='#CCCCCC',font=fontStyle)
        menubar.place(x=1,y=1) # Establecemos la posicion del submenu
        menubar.menu = Menu(menubar, tearoff=0)
        menubar["menu"] = menubar.menu
        # Establecemos las opciones del submenu y sus funciones
        menubar.menu.add_command(label="Cargar",command=self.Cargar,font=fontStyle,activebackground='#094771',activeforeground='#CCCCCC')
        menubar.menu.add_command(label="Salir",command=self.master.quit,font=fontStyle,activebackground='#094771',activeforeground='#CCCCCC')
        # Creamos una etiqueta 
        lab1 = Label(self.master,text="Estado:",font=fontStyle)
        lab1.place(x=30,y=50)
        # Creamos un combobox que almacene los estados
        cobEstado = ttk.Combobox(state="readonly",font=fontStyle)
        cobEstado.place(x=100,y=50)
        cobEstado['values'] = self.listNomE

    #  Funcion para C"argar el archivo
    def Cargar(self):
        self.listEstado = lDt.obtecion_datos(archivo='Datos\\Casos_Diarios.csv')
        for i in self.listEstado:
            self.listNomE.append(str(i.nombre))
    
"""
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
"""


if __name__  == "__main__":
    #Creamos la ventana
    root = Tk()
    root.title("Simulación de COVID-19 México") # Establecemos el titulo
    root.geometry("1000x650") # ancho x alto
    app = App(root)
    root.mainloop()