#from tkinter import *
import tkinter as tk 
from client.gui_app import frame, barra_menu
from tkinter import ttk, Label, Listbox, LabelFrame




def main():
 #   Label.config(text='HOLA MUNDO') 
#para crear la ventana
    Ventana_raiz= tk.Tk()
    Ventana_raiz.resizable(0,0)
    barra_menu(Ventana_raiz)
    #titulo
    Ventana_raiz.title("sistema de ventas con crud python, tkinter")

  
    

        
    #etiqueta
    #Label = tk.Label(Ventana_raiz, text="BIENVENIDO A MI APP")
    ##Label.pack()
#boton =tk.Button(Ventana_raiz, text="haz click aqui", command=main)
    #boton.pack()
        #le indicamos al programa que queremos una ventana de 400*280

        #lbl= Label(Ventana_raiz, text="este es un label")
        #lbl.pack()
        #btn= Button(Ventana_raiz, text="presione")
        #btn.pack()
        #bienvenido= LabelFrame(Ventana_raiz, text="formulario de gestion del sistema de ventas")
        #bienvenido.place(x=50, y=50, width=500, height=400)

        #labels y entris
    
        #contenedor de los elementos

        #frame = tk.Frame(Ventana_raiz)
        #frame.pack()
        #frame.config(width=480, height=320, bg= 'green')
    app = frame(ventana_raiz = Ventana_raiz)

    app.mainloop()

if __name__ == '__main__' :
    main() 
    