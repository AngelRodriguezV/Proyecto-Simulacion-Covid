from tkinter import Button, Entry, Menubutton, StringVar, Tk, Frame, font, ttk, Label, Menu, filedialog
from tkinter.constants import CENTER, NO
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importando mis clases
import leerDatos as lDt
import estado
import modelos as md

class  App:
    listEstado = []
    listNomE = []
    nameArchivo = ''
    
    def __init__(self,master:Tk) -> None:
        self.master = master
        # Configuracion del master
        self.master.configure(background='#CCCCCC')
        self.miStyle = font.Font(family="Calibri",size=12) # Fuente de letra
        
        barra = Frame(self.master,background='#1E1E1E',width=2000,height=30) # MenuBar
        barra.place(x=0,y=0) # Establecemos la posicion de la barra
        
        # Creamos un submenu
        menubar = Menubutton(barra,text="Archivo",background='#1E1E1E',foreground='#CCCCCC',
                            activebackground='#505050',activeforeground='#CCCCCC',font=self.miStyle)
        menubar.place(x=1,y=1) # Establecemos la posicion del submenu
        menubar.menu = Menu(menubar, tearoff=0)
        menubar["menu"] = menubar.menu
        
        # Establecemos las opciones del submenu y sus funciones
        menubar.menu.add_command(label="Cargar",command=self.abrirArchivo,font=self.miStyle,
                                activebackground='#094771',activeforeground='#CCCCCC')
        menubar.menu.add_command(label="Salir",command=self.master.quit,font=self.miStyle,
                                activebackground='#094771',activeforeground='#CCCCCC')
        
        # Creamos una etiqueta 
        lab1 = Label(self.master,text="Estado:",font=self.miStyle,background='#CCCCCC')
        lab1.place(x=30,y=80)

        # Creamos un combobox que almacene los estados
        self.cobEstado = ttk.Combobox(state="readonly",font=self.miStyle)
        self.cobEstado.place(x=100,y=80)
        
        #  Creamos un boton para seleccionar los datos
        btnSeleccionar = Button(self.master,text="Seleccionar",font=self.miStyle,command=self.funSeleccionar,
                                background='#2D2D2D',foreground='#CCCCCC',activebackground='#16825D',
                                activeforeground='#CCCCCC',)
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

        # Cargamos los datos predeterminados
        # self.Cargar()

        # Frame de Trabajo
        self.frameT = Frame(self.master,width=1320,height=500)
        self.frameT.place(x=20,y=184)

        # Etiqueta
        self.txtEstado = StringVar()
        self.txtEstado.set("")
        self.lab_nomEstado = Label(self.frameT,font=("Calibri",25),textvariable=self.txtEstado)
        self.lab_nomEstado.place(x=200,y=10)
# ==================================================================================================================
        # Frame para el modelo SIR
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
        self.str_sb.set("0.199")
        self.str_sy = StringVar()
        self.str_sy.set("0.0714")
        self.str_st = StringVar()
        self.str_st.set("200")
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
        self.simularSir = Button(self.frameT,text="SIMULAR",font=self.miStyle,command=self.calcularSIR,
                                background='#2D2D2D',foreground='#CCCCCC',activebackground='#16825D',
                                activeforeground='#CCCCCC',)
        # Grafica SIR
        self.figs, self.axs = plt.subplots(dpi=90,figsize=(5,5))
        self.figs.suptitle('SIR')
        self.can_s = FigureCanvasTkAgg(self.figs,self.frameT)
        # TABLA DE SIR
        self.tab_s = ttk.Treeview(self.frameT,height=21)
        self.tab_s['columns'] = ('t','s','i','r')
        self.tab_s.column("#0",width=0,stretch=NO)
        self.tab_s.column("t",anchor=CENTER,width=80)
        self.tab_s.column("s",anchor=CENTER,width=80)
        self.tab_s.column("i",anchor=CENTER,width=80)
        self.tab_s.column("r",anchor=CENTER,width=80)
        self.tab_s.heading("#0",text="",anchor=CENTER)
        self.tab_s.heading("t",text="t",anchor=CENTER)
        self.tab_s.heading("s",text="S",anchor=CENTER)
        self.tab_s.heading("i",text="I",anchor=CENTER)
        self.tab_s.heading("r",text="R",anchor=CENTER)
# ==================================================================================================================
        # Freme para el modelo Logistico 
        self.lab_lTitulo = Label(self.frameT,text="MODELO LOGISTICO",font=("Calibri",25))
        self.lab_l1 = Label(self.frameT,text="Fecha inico:",font=self.miStyle)
        self.lab_l2 = Label(self.frameT,text="Fecha final:",font=self.miStyle)
        self.lab_l3 = Label(self.frameT,text="Cantidad de datos:",font=self.miStyle)
        self.cob_l1 = ttk.Combobox(self.frameT,state="readonly",font=self.miStyle)
        self.cob_l1.bind('<<ComboboxSelected>>',self.mostarDatosLog)
        self.cob_l2 = ttk.Combobox(self.frameT,state="readonly",font=self.miStyle)
        self.cob_l2.bind('<<ComboboxSelected>>',self.mostarDatosLog)
        self.str_l1 = StringVar()
        self.str_l1.set("")
        self.txt_l1 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_l1,state='disabled')
        self.simularLog = Button(self.frameT,text="SIMULAR",font=self.miStyle,command=self.calcularLog,
                                background='#2D2D2D',foreground='#CCCCCC',activebackground='#16825D',
                                activeforeground='#CCCCCC',)
        # Grafica Logistica
        self.figl, self.axl = plt.subplots(dpi=90,figsize=(5,5))
        self.figl.suptitle('Logistico')
        self.can_l = FigureCanvasTkAgg(self.figl,self.frameT)
        # TABLA DE logistica
        self.tab_l = ttk.Treeview(self.frameT,height=21)
        self.tab_l['columns'] = ('t','P')
        self.tab_l.column("#0",width=0,stretch=NO)
        self.tab_l.column("t",anchor=CENTER,width=100)
        self.tab_l.column("P",anchor=CENTER,width=100)
        self.tab_l.heading("#0",text="",anchor=CENTER)
        self.tab_l.heading("t",text="t",anchor=CENTER)
        self.tab_l.heading("P",text="P",anchor=CENTER)
# ==================================================================================================================
        # Frame para el modelo Gompertz
        self.lab_gTitulo = Label(self.frameT,text="MODELO GOMPERTZ",font=("Calibri",25))
        self.lab_g1 = Label(self.frameT,text="Fecha inico:",font=self.miStyle)
        self.lab_g2 = Label(self.frameT,text="Fecha final:",font=self.miStyle)
        self.lab_g3 = Label(self.frameT,text="Cantidad de datos:",font=self.miStyle)
        self.cob_g1 = ttk.Combobox(self.frameT,state="readonly",font=self.miStyle)
        self.cob_g1.bind('<<ComboboxSelected>>',self.mostarDatosGop)
        self.cob_g2 = ttk.Combobox(self.frameT,state="readonly",font=self.miStyle)
        self.cob_g2.bind('<<ComboboxSelected>>',self.mostarDatosGop)
        self.str_g1 = StringVar()
        self.str_g1.set("")
        self.txt_g1 = Entry(self.frameT,font=self.miStyle,textvariable=self.str_g1,state='disabled')
        self.simularGop = Button(self.frameT,text="SIMULAR",font=self.miStyle,command=self.calcularGop,
                                background='#2D2D2D',foreground='#CCCCCC',activebackground='#16825D',
                                activeforeground='#CCCCCC',)
        # Grafica Gompertz
        self.figg, self.axg = plt.subplots(dpi=90,figsize=(5,5))
        self.figg.suptitle('Gompertz')
        self.can_g = FigureCanvasTkAgg(self.figg,self.frameT)
        # TABLA DE Gompertz
        self.tab_g = ttk.Treeview(self.frameT,height=21)
        self.tab_g['columns'] = ('t','P','dP')
        self.tab_g.column("#0",width=0,stretch=NO)
        self.tab_g.column("t",anchor=CENTER,width=100)
        self.tab_g.column("P",anchor=CENTER,width=100)
        self.tab_g.column("dP",anchor=CENTER,width=100)
        self.tab_g.heading("#0",text="",anchor=CENTER)
        self.tab_g.heading("t",text="t",anchor=CENTER)
        self.tab_g.heading("P",text="P",anchor=CENTER)
        self.tab_g.heading("dP",text="dP",anchor=CENTER)
# ==================================================================================================================
        # ejercutar metodos de mostrar
        self.fun_btnSir()
# ==================================================================================================================
    # Funcion para Cargar el archivo
    def abrirArchivo(self):
        self.nameArchivo = filedialog.askopenfilename()
        if self.nameArchivo != '':
            self.Cargar()

    def Cargar(self):
        self.listEstado = lDt.obtecion_datos(archivo=self.nameArchivo)
        for i in self.listEstado:
            self.listNomE.append(str(i.nombre))
        self.cobEstado['values'] = self.listNomE # Asignamos los datos

    # Funcion del boton seleccionar
    def funSeleccionar(self):
        if self.cobEstado.get() != '':
            self.txtEstado.set("-   "+self.cobEstado.get())
            self.Estadoact = self.listEstado[self.cobEstado.current()]
            self.cobF1['values'] = self.Estadoact.fechas
            #print(str(self.cobEstado.current()))
            #poss = self.listEstado.index(self.cobEstado.get())
            self.cob_l1['values'] = self.Estadoact.fechas
            self.cob_l2['values'] = self.Estadoact.fechas
            self.cob_g1['values'] = self.Estadoact.fechas
            self.cob_g2['values'] = self.Estadoact.fechas

    # Calcular los datos de SIR
    def calcularSIR(self):
        if self.cobF1.get() != '':
            n = int(self.str_sn.get())
            s = int(self.str_ss.get())
            i = int(self.str_si.get())
            r = int(self.str_sr.get())
            b = float(self.str_sb.get())
            y = float(self.str_sy.get())
            t = int(self.str_st.get())
            self.rSir = md.SIR(n,s,i,r,t,b,y)
            self.axs.clear()
            self.axs.scatter(self.rSir[0],self.rSir[1], label="Susceptibles")
            self.axs.scatter(self.rSir[0],self.rSir[2], label="Infectados")
            self.axs.scatter(self.rSir[0],self.rSir[3], label="Recuperados")
            self.axs.legend()
            self.can_s.draw()
            self.tab_s.delete(*self.tab_s.get_children())
            for xd in range(0,t):
                self.tab_s.insert(values=[self.rSir[0][xd],self.rSir[1][xd],self.rSir[2][xd],self.rSir[3][xd]],
                                parent='',index='end')

    # Calcular los datos Logisticos
    def calcularLog(self):
        if self.txt_l1.get() != '':
            t = int(self.txt_l1.get())
            pi = self.cob_l1.current()
            pf = self.cob_l2.current()
            self.rLog = md.Logistica(t,self.Estadoact.casosAcumulados[pi:pf])
            self.axl.clear()
            self.axl.scatter(self.rLog[0],self.rLog[1],label="Logistica")
            self.axl.legend()
            self.can_l.draw()
            self.tab_l.delete(*self.tab_l.get_children())
            for xd in range(0,t):
                self.tab_l.insert(values=[self.rLog[0][xd],self.rLog[1][xd]],parent='',index='end')

    # Calcular los datos Gompertz
    def calcularGop(self):
        if self.txt_g1.get() != '':
            t = int(self.txt_g1.get())
            pi = self.cob_g1.current()
            pf = self.cob_g2.current()
            self.rGop = md.gompertz(t,md.cal_constante(self.Estadoact.casosAcumulados[pi:pf]))
            self.axg.clear()
            self.axg.scatter(self.rGop[0],self.rGop[1],label="F Gompertz")
            self.axg.scatter(self.rGop[0],self.rGop[2],label="Derivada")
            self.axg.legend()
            self.can_g.draw()
            self.tab_g.delete(*self.tab_g.get_children())
            for xd in range(0,t):
                self.tab_g.insert(values=[self.rGop[0][xd],self.rGop[1][xd],self.rGop[2][xd]],parent='',index='end')

# ==================================================================================================================
    # Funcion para mostrar los datos del sir
    def mostrarDatosSir(self,event):
        if self.cobF1.get() != '':
            self.str_sn.set(str(self.Estadoact.poblacion))
            self.str_ss.set(str(self.Estadoact.poblacion - self.Estadoact.casosDiarios[self.cobF1.current()]))
            self.str_si.set(str(self.Estadoact.casosDiarios[self.cobF1.current()]))
    
    # Mostrar la cantidad de datos logistico
    def mostarDatosLog(self,event):
        if self.cob_l1.get() != '' and self.cob_l2.get() != '':
            if self.cob_l2.current()-self.cob_l1.current() > 0:
                self.str_l1.set(str(self.cob_l2.current()-self.cob_l1.current()))
            else:
                self.str_l1.set('')

    # Funcion para mostrar la cantidad de datos de gompertz
    def mostarDatosGop(self,event):
        if self.cob_g1.get() != '' and self.cob_g1.get() != '':
            if self.cob_g2.current()-self.cob_g1.current() > 0:
                self.str_g1.set(str(self.cob_g2.current()-self.cob_g1.current()))
            else:
                self.str_g1.set('')

# ==================================================================================================================
    # Funcion de la visualizacion del modelo sir
    def fun_btnSir(self):
        # Borrar datos
        self.no_btnLog()
        self.no_btnGop()
        # Mostrar datos
        self.btnSir.config(background='#16825D')
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
        self.tab_s.place(x=500,y=20)

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
        self.tab_s.place_forget()

    # Mostrar la interfaz de logistica
    def fun_btnLog(self):
        # Borrar datos
        self.no_btnSir()
        self.no_btnGop()
        # Mostrar datos
        self.btnLog.config(background='#16825D')
        self.lab_nomEstado.place(x=300,y=10)
        self.lab_lTitulo.place(x=10,y=10)
        self.lab_l1.place(x=10,y=100)
        self.lab_l2.place(x=10,y=150)
        self.lab_l3.place(x=10,y=200)
        self.cob_l1.place(x=100,y=100)
        self.cob_l2.place(x=100,y=150)
        self.txt_l1.place(x=150,y=200)
        self.simularLog.place(x=300,y=100)
        self.can_l.get_tk_widget().place(x=850,y=20)
        self.tab_l.place(x=600,y=20)

    # ocultar los elementos del logistico
    def no_btnLog(self):
        self.btnLog.config(background='#2D2D2D')
        self.lab_lTitulo.place_forget()
        self.lab_l1.place_forget()
        self.lab_l2.place_forget()
        self.lab_l3.place_forget()
        self.cob_l1.place_forget()
        self.cob_l2.place_forget()
        self.txt_l1.place_forget()
        self.simularLog.place_forget()
        self.can_l.get_tk_widget().place_forget()
        self.tab_l.place_forget()

    def fun_btnGop(self):
        # Borrar datos
        self.no_btnSir()
        self.no_btnLog()
        # Mostrar datos
        self.btnGop.config(background='#16825D')
        self.lab_nomEstado.place(x=310,y=10)
        self.lab_gTitulo.place(x=10,y=10)
        self.lab_g1.place(x=10,y=100)
        self.lab_g2.place(x=10,y=150)
        self.lab_g3.place(x=10,y=200)
        self.cob_g1.place(x=100,y=100)
        self.cob_g2.place(x=100,y=150)
        self.txt_g1.place(x=150,y=200)
        self.simularGop.place(x=300,y=100)
        self.can_g.get_tk_widget().place(x=850,y=20)
        self.tab_g.place(x=500,y=20)
    
    def no_btnGop(self):
        self.btnGop.config(background='#2D2D2D')
        self.lab_gTitulo.place_forget()
        self.lab_g1.place_forget()
        self.lab_g2.place_forget()
        self.lab_g3.place_forget()
        self.cob_g1.place_forget()
        self.cob_g2.place_forget()
        self.txt_g1.place_forget()
        self.simularGop.place_forget()
        self.can_g.get_tk_widget().place_forget()
        self.tab_g.place_forget()
# ==================================================================================================================

if __name__  == "__main__":
    #Creamos la ventana
    root = Tk()
    root.title("Simulación de COVID-19 México") # Establecemos el titulo
    w1 = root.winfo_screenwidth()
    h1 = root.winfo_screenheight()
    root.geometry("{w}x{h}".format(w=w1,h=h1)) # ancho x alto
    #root.resizable(False,False)
    root.state('zoomed')
    root.protocol("WM_DELETE_WINDOW",root.quit)
    app = App(root)
    root.mainloop()