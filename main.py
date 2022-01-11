from tkinter import Button, Menubutton, StringVar, Tk, Frame, font, ttk, Label, Menu
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
        self.miStyle = font.Font(family="Calibri",size=12) # Fuente de letra
        
        # Cargamos los datos predeterminados
        self.Cargar()
        barra = Frame(self.master,background='#1E1E1E',width=2000,height=30) # MenuBar
        barra.place(x=0,y=0) # Establecemos la posicion de la barra
        
        # Creamos un submenu
        menubar = Menubutton(barra,text="Archivo",background='#1E1E1E',foreground='#CCCCCC',
                            activebackground='#505050',activeforeground='#CCCCCC',font=self.miStyle)
        menubar.place(x=1,y=1) # Establecemos la posicion del submenu
        menubar.menu = Menu(menubar, tearoff=0)
        menubar["menu"] = menubar.menu
        
        # Establecemos las opciones del submenu y sus funciones
        menubar.menu.add_command(label="Cargar",command=self.Cargar,font=self.miStyle,
                                activebackground='#094771',activeforeground='#CCCCCC')
        menubar.menu.add_command(label="Salir",command=self.master.quit,font=self.miStyle,
                                activebackground='#094771',activeforeground='#CCCCCC')
        
        # Creamos una etiqueta 
        lab1 = Label(self.master,text="Estado:",font=self.miStyle,background='#CCCCCC')
        lab1.place(x=30,y=80)

        # Creamos un combobox que almacene los estados
        self.cobEstado = ttk.Combobox(state="readonly",font=self.miStyle)
        self.cobEstado.place(x=100,y=80)
        self.cobEstado['values'] = self.listNomE # Asignamos los datos
        
        #  Creamos un boton para seleccionar los datos
        btnSeleccionar = Button(self.master,text="Seleccionar",font=self.miStyle,command=self.funSeleccionar,
                                background='black',foreground='white')
        btnSeleccionar.place(x=300,y=80)

        # Opciones para visualizar los metodos
        self.btnSir = Button(self.master,text="SIR",command=self.fun_btnSir,font=self.miStyle,width=10,
                            background='#2D2D2D',foreground='#CCCCCC',activebackground='#16825D',
                            activeforeground='#CCCCCC',)
        self.btnSir.place(x=20,y=150)
        self.btnLog = Button(self.master,text="Logistico",command=self.fun_btnLog,font=self.miStyle,width=10,
                            background='#2D2D2D',foreground='#CCCCCC',activebackground='#16825D',
                            activeforeground='#CCCCCC')
        self.btnLog.place(x=110,y=150)
        self.btnGop = Button(self.master,text="Gompertz",command=self.fun_btnGop,font=self.miStyle,width=10,
                            background='#2D2D2D',foreground='#CCCCCC',activebackground='#16825D',
                            activeforeground='#CCCCCC')
        self.btnGop.place(x=200,y=150)

        # Frame de Trabajo
        self.frameT = Frame(self.master,width=1320,height=500)
        self.frameT.place(x=20,y=184)
        # Frame para el modelo SIR
        self.lab_sTitulo = Label(self.frameT,text="MODELO SIR",font=("Calibri",25))
        self.lab_sTitulo.place(x=10,y=10)

        self.txtEstado = StringVar()
        self.txtEstado.set("")
        self.lab_nomEstado = Label(self.frameT,font=("Calibri",25),textvariable=self.txtEstado)
        self.lab_nomEstado.place(x=200,y=10)

        # Freme para el modelo Logistico
        self.lab_lTitulo = Label(self.frameT,text="MODELO LOGISTICO",font=("Calibri",25))
        

        # Frame para el modelo Gompertz
        self.lab_gTitulo = Label(self.frameT,text="MODELO GOMPERTZ",font=("Calibri",25))
        

    # Funcion para C"argar el archivo
    def Cargar(self):
        self.listEstado = lDt.obtecion_datos(archivo='Datos\\Casos_Diarios.csv')
        for i in self.listEstado:
            self.listNomE.append(str(i.nombre))

    # Funcion del boton seleccionar
    def funSeleccionar(self):
        if self.cobEstado.get() != '':
            self.txtEstado.set("-   "+self.cobEstado.get())
            print(str(self.cobEstado.current()))
            #poss = self.listEstado.index(self.cobEstado.get())

    # Funcion de la visualizacion del modelo sir
    def fun_btnSir(self):
        self.btnSir.config(background='#16825D')
        self.btnLog.config(background='#2D2D2D')
        self.btnGop.config(background='#2D2D2D')
        self.lab_lTitulo.place_forget()
        self.lab_gTitulo.place_forget()
        self.lab_sTitulo.place(x=10,y=10)
        self.lab_nomEstado.place(x=200,y=10)

    def fun_btnLog(self):
        self.btnLog.config(background='#16825D')
        self.btnSir.config(background='#2D2D2D')
        self.btnGop.config(background='#2D2D2D')
        self.lab_sTitulo.place_forget()
        self.lab_gTitulo.place_forget()
        self.lab_lTitulo.place(x=10,y=10)
        self.lab_nomEstado.place(x=300,y=10)
        

    def fun_btnGop(self):
        self.btnGop.config(background='#16825D')
        self.btnLog.config(background='#2D2D2D')
        self.btnSir.config(background='#2D2D2D')
        self.lab_sTitulo.place_forget()
        self.lab_lTitulo.place_forget()
        self.lab_gTitulo.place(x=10,y=10)
        self.lab_nomEstado.place(x=310,y=10)

if __name__  == "__main__":
    #Creamos la ventana
    root = Tk()
    root.title("Simulación de COVID-19 México") # Establecemos el titulo
    w1 = root.winfo_screenwidth()
    h1 = root.winfo_screenheight()
    root.geometry("{w}x{h}".format(w=w1,h=h1)) # ancho x alto
    #root.resizable(False,False)
    root.state('zoomed')
    app = App(root)
    root.mainloop()