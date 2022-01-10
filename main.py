
from tkinter import Tk, Frame, font, ttk, Label
from typing import no_type_check
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Creamos la ventana
root = Tk()
root.title("Simulación de COVID-19 México")
root.geometry("1000x650") #ancho x alto
'''
frame = Frame(root)
frame.grid(column=0,row=0,sticky="nsew")

fig, ax = plt.subplots(dpi=90, figsize=(7,5))
fig.suptitle('SIR')

canvas = FigureCanvasTkAgg(fig,master=frame)
canvas.draw()
canvas.get_tk_widget().grid(column=0,row=0,rowspan=3)
'''

'''
comEstado = ttk.Combobox(state="readonly")
comEstado.place(x=50,y=50)
comEstado["values"] = ["AGUASCALIENTES","BAJA CALIFORNIA","BAJA CALIFORNIA SUR",
                        "CAMPECHE","CHIAPAS","CHIHUAHUA","DISTRITO FEDERAL","COAHUILA",
                        "COLIMA","DURANGO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO",
                        "MEXICO","MICHOACAN","MORELOS","NAYARIT","NUEVO LEON","OAXACA"]
comModelo = ttk.Combobox(state="readonly")
'''
notebook = ttk.Notebook(root,width=980,height=510)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)
notebook.add(tab1,text='SIR')
notebook.add(tab2,text='Logístico')
notebook.add(tab3,text='Gompertz')
notebook.grid(padx=10,pady=100)

root.mainloop()