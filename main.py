from tkinter import Button, Entry, Menubutton, Radiobutton, StringVar, Tk, Frame, font, ttk, Label, Menu
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

        # Etiqueta
        self.txtEstado = StringVar()
        self.txtEstado.set("")
        self.lab_nomEstado = Label(self.frameT,font=("Calibri",25),textvariable=self.txtEstado)
        self.lab_nomEstado.place(x=200,y=10)

        # Frame para el modelo SIR ---------------------------------------------------------------------------------
        self.lab_sTitulo = Label(self.frameT,text="MODELO SIR",font=("Calibri",25))
        # Seleccion de datos sir
        self.str_sn = StringVar()
        self.str_sn.set("0")
        self.str_ss = StringVar()
        self.str_ss.set("0")
        self.str_si = StringVar()
        self.str_si.set("0")
        self.str_sr = StringVar()
        self.str_sr.set("0")
        self.str_sb = StringVar()
        self.str_sb.set("0.1999")
        self.str_sy = StringVar()
        self.str_sy.set("0.0714")
        self.str_st = StringVar()
        self.str_st.set("0")
        self.lab_s1 = Label(self.frameT,text="Fecha:",font=self.miStyle)
        self.cobF1 = ttk.Combobox(self.frameT,state="readonly",font=self.miStyle)
        self.cobF1.bind('<<ComboboxSelected>>',self.mostrarDatosSir)
        self.lab_s2 = Label(self.frameT,text="Datos",font=self.miStyle)
        self.lab_s3 = Label(self.frameT,text="N:",font=self.miStyle)
        self.lab_s4 = Label(self.frameT,text="S:",font=self.miStyle)
        self.lab_s5 = Label(self.frameT,text="I:",font=self.miStyle)
        self.lab_s6 = Label(self.frameT,text="R:",font=self.miStyle)
        self.lab_s7 = Label(self.frameT,text="β:",font=self.miStyle)
        self.lab_s8 = Label(self.frameT,text="γ:",font=self.miStyle)
        self.lab_s9 = Label(self.frameT,text="t:",font=self.miStyle)
        self.txt_s1 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_sn)
        self.txt_s2 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_ss)
        self.txt_s3 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_si)
        self.txt_s4 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_sr)
        self.txt_s5 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_sb)
        self.txt_s6 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_sy)
        self.txt_s7 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_st)
        self.simularSir = Button(self.frameT,text="SIMULAR",font=self.miStyle)
        self.figs, axs = plt.subplots(dpi=90,figsize=(5,5))
        self.figs.suptitle('SIR')
        self.can_s = FigureCanvasTkAgg(self.figs,self.frameT)
        self.can_s.draw()

        # Freme para el modelo Logistico ----------------------------------------------------------------------------
        self.lab_lTitulo = Label(self.frameT,text="MODELO LOGISTICO",font=("Calibri",25))
        

        # Frame para el modelo Gompertz -----------------------------------------------------------------------------
        self.lab_gTitulo = Label(self.frameT,text="MODELO GOMPERTZ",font=("Calibri",25))
        
        # ejercutar metodos de mostrar
        self.fun_btnSir()

    # Funcion para Cargar el archivo
    def Cargar(self):
        self.listEstado = lDt.obtecion_datos(archivo='Datos\\Casos_Diarios.csv')
        for i in self.listEstado:
            self.listNomE.append(str(i.nombre))

    # Funcion del boton seleccionar
    def funSeleccionar(self):
        if self.cobEstado.get() != '':
            self.txtEstado.set("-   "+self.cobEstado.get())
            self.Estadoact = self.listEstado[self.cobEstado.current()]
            self.cobF1['values'] = self.Estadoact.fechas
            #print(str(self.cobEstado.current()))
            #poss = self.listEstado.index(self.cobEstado.get())

    # Funcion para mostrar los datos del sir
    def mostrarDatosSir(self,event):
        if self.cobF1.get() != '':
            self.str_sn.set(str(self.Estadoact.poblacion))
            self.str_ss.set(str(self.Estadoact.poblacion - self.Estadoact.casosDiarios[self.cobF1.current()]))
            self.str_si.set(str(self.Estadoact.casosDiarios[self.cobF1.current()]))

    # Funcion de la visualizacion del modelo sir
    def fun_btnSir(self):
        # Cambiar color del selector
        self.btnSir.config(background='#16825D')
        self.btnLog.config(background='#2D2D2D')
        self.btnGop.config(background='#2D2D2D')
        # Borrar datos
        self.lab_lTitulo.place_forget()
        self.lab_gTitulo.place_forget()
        # Mostrar datos
        self.lab_sTitulo.place(x=10,y=10)
        self.lab_nomEstado.place(x=200,y=10)
        self.lab_s1.place(x=10,y=100)
        self.cobF1.place(x=60,y=100)
        self.lab_s2.place(x=10,y=150)
        self.lab_s3.place(x=25,y=190)
        self.lab_s4.place(x=25,y=230)
        self.lab_s5.place(x=25,y=270)
        self.lab_s6.place(x=25,y=310)
        self.lab_s7.place(x=25,y=350)
        self.lab_s8.place(x=25,y=390)
        self.lab_s9.place(x=25,y=430)
        self.txt_s1.place(x=50,y=190)
        self.txt_s2.place(x=50,y=230)
        self.txt_s3.place(x=50,y=270)
        self.txt_s4.place(x=50,y=310)
        self.txt_s5.place(x=50,y=350)
        self.txt_s6.place(x=50,y=390)
        self.txt_s7.place(x=50,y=430)
        self.simularSir.place(x=280,y=100)
        self.can_s.get_tk_widget().place(x=850,y=20)

    # ocultar los elementos del sir
    def no_btnSir(self):
        self.btnSir.config(background='#2D2D2D')
        self.lab_sTitulo.place_forget()
        self.lab_nomEstado.place_forget()
        self.lab_s1.place_forget()
        self.cobF1.place_forget()
        self.lab_s2.place_forget()
        self.lab_s3.place_forget()
        self.lab_s4.place_forget()
        self.lab_s5.place_forget()
        self.lab_s6.place_forget()
        self.lab_s7.place_forget()
        self.lab_s8.place_forget()
        self.lab_s9.place_forget()
        self.txt_s1.place_forget()
        self.txt_s2.place_forget()
        self.txt_s3.place_forget()
        self.txt_s4.place_forget()
        self.txt_s5.place_forget()
        self.txt_s6.place_forget()
        self.txt_s7.place_forget()
        self.simularSir.place_forget()
        self.can_s.get_tk_widget().place_forget()

    def fun_btnLog(self):
        self.no_btnSir()
        self.btnLog.config(background='#16825D')
        self.btnGop.config(background='#2D2D2D')
        self.lab_gTitulo.place_forget()
        self.lab_lTitulo.place(x=10,y=10)
        self.lab_nomEstado.place(x=300,y=10)
        

    def fun_btnGop(self):
        self.no_btnSir()
        self.btnGop.config(background='#16825D')
        self.btnLog.config(background='#2D2D2D')
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