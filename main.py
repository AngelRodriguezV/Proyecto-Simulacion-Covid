
from tkinter import Tk, Frame, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Creamos la ventana
root = Tk()
root.title("Simulación de COVID-19 México")
root.geometry("900x600") #ancho x alto
'''
frame = Frame(root)
frame.grid(column=0,row=0,sticky="nsew")

fig, ax = plt.subplots(dpi=90, figsize=(7,5))
fig.suptitle('SIR')

canvas = FigureCanvasTkAgg(fig,master=frame)
canvas.draw()
canvas.get_tk_widget().grid(column=0,row=0,rowspan=3)
'''
comEstado = ttk.Combobox(state="readonly")
comEstado.place(x=50,y=50)
comEstado["values"] = ["AGUASCALIENTES","BAJA CALIFORNIA","BAJA CALIFORNIA SUR",
                        "CAMPECHE","CHIAPAS","CHIHUAHUA","DISTRITO FEDERAL","COAHUILA",
                        "COLIMA","DURANGO","GUANAJUATO","GUERRERO","HIDALGO","JALISCO",
                        "MEXICO","MICHOACAN","MORELOS","NAYARIT","NUEVO LEON","OAXACA"]
comModelo = ttk.Combobox(state="readonly")

root.mainloop()