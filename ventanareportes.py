import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import Button, Grid, Label
from mysql.connector import Error
import datetime

class VentanaReportes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VENTANA REPORTES")
        self.resizable(0, 0)

        self.tablareportesclien()
        self. generar_reportes_por_clientes()

    def generar_reportes_por_clientes(self, codigo_cliente):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                db="sistema_de_ventas"
            )
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM ventas WHERE CODIGO_CLIENTE={0} ORDER BY CODIGO_DE_VENTA".format(codigo_cliente))
            resultados = cursor.fetchall()
            return resultados
        except Error as ex:
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))

    fecha_venta = datetime.datetime.now()

    def cargar_reportes_en_tabla(self):
        # Limpia la tabla si hay datos anteriores
        for row in self.tablarepor.get_children():
            self.tablarepor.delete(row)

        # Llama a la función para obtener los datos
        codigo_cliente = 2  # Reemplaza con el código del cliente que desees
        datos = self.generar_reportes_por_clientes(codigo_cliente)

        for row in datos:
            self.tablarepor.insert("", "end", values=row)

    def tablareportesclien(self):
        self.tablarepor = ttk.Treeview(self, columns=('CODIGO_DE_VENTA', 'CODIGO_CLIENTE', 'CANTIDAD_DE_PRODUCTOS', 'TOTAL_DE_VENTA', 'FECHA'))
        self.tablarepor.grid(row=1, column=0, padx=10, pady=10, columnspan=5)
        self.tablarepor.heading('#0', text='CODIGO_DE_VENTA', anchor='center')
        self.tablarepor.heading('#1', text='CODIGO_CLIENTE', anchor='center')
        self.tablarepor.heading('#2', text='CANTIDAD_DE_PRODUCTOS', anchor='center')
        self.tablarepor.heading('#3', text='TOTAL_DE_VENTA', anchor='center')
        self.tablarepor.heading('#4', text='FECHA', anchor='center')

        self.label_reporcliente = tk.Label(self, text='REPORTES POR CODIGO DE CLIENTE')
        self.label_reporcliente.config(font=('arial', 12, 'bold'))
        self.label_reporcliente.grid(row=0, column=2, padx=10, pady=10)

        # Agrega un botón para cargar los datos en la tabla
        cargar_button = tk.Button(self, text="Cargar Reportes", command=self.cargar_reportes_en_tabla)
        cargar_button.grid(row=2, column=0, padx=10, pady=10)

def main():
    VENTreport = VentanaReportes()
    VENTreport.mainloop()

if __name__ == '__main__':
    main()














"""import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import Button, Grid, Label
import csv
import mysql.connector
from mysql.connector import Error

class VentanaReportes(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VENTANA REPORTES")
        self.resizable(0, 0)

        self.tablareportesclien()
        self.tablareportesproduc()

    
    def generar_reportes_por_cliente(self, codigo_cliente):
        try:
         conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                db="sistema_de_ventas"
            )
         cursor = conexion.cursor()  
         cursor.execute("SELECT * FROM  ventas WHERE CODIGO_CLIENTE={0} ORDER BY CODIGO_DE_VENTA".format(codigo_cliente))
         resultados=cursor.fetchall()
         return resultados
        except Error as ex:

            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))

    def tablareportesclien(self):
        self.tablarepor = ttk.Treeview(self, columns=('CODIGO_DE_VENTA', 'CODIGO_CLIENTE', 'CANTIDAD_DE_PRODUCTOS', 'TOTAL_DE_VENTA', 'FECHA'))
        self.tablarepor.grid(row=1, column=0, padx=10, pady=10, columnspan=5)
        self.tablarepor.heading('#0', text='CODIGO_DE_VENTA', anchor='center')
        self.tablarepor.heading('#1', text='CODIGO_CLIENTE', anchor='center')
        self.tablarepor.heading('#2', text='CANTIDAD_DE_PRODUCTOS', anchor='center')
        self.tablarepor.heading('#3', text='TOTAL_DE_VENTA', anchor='center')
        self.tablarepor.heading('#4', text='FECHA', anchor='center')

        self.label_reporcliente= tk.Label(self, text='REPORTES POR CODIGO DE CLIENTE')
        self.label_reporcliente.config(font=('arial', 12, 'bold'))
        self.label_reporcliente.grid(row =0, column = 2, padx=10, pady=10)

    
    

    def tablareportesproduc(self):
        self.tablareporprod = ttk.Treeview(self, columns=('CODIGO_DE_VENTA', 'CODIGO_PRODUCTOS', 'CANTIDAD_DE_PRODUCTOS', 'TOTAL_DE_VENTA', 'FECHA'))
        self.tablareporprod.grid(row=3, column=0, padx=10, pady=10, columnspan=5)                
        self.tablareporprod.heading('#0', text='CODIGO_DE_VENTA', anchor='center')
        self.tablareporprod.heading('#1', text='CODIGO_PRODUCTOS', anchor='center')
        self.tablareporprod.heading('#2', text='CANTIDAD_DE_PRODUCTOS', anchor='center')
        self.tablareporprod.heading('#3', text='TOTAL_DE_VENTA', anchor='center')
        self.tablareporprod.heading('#4', text='FECHA', anchor='center')

        self.label_reporproductos= tk.Label(self, text='REPORTES POR CODIGO DE PRODUCTO')
        self.label_reporproductos.config(font=('arial', 12, 'bold'))
        self.label_reporproductos.grid(row =2, column = 2, padx=10, pady=10)
           


    def generar_excelinter(self, nombreReporteinter, ventas):
        file = open(nombreReporteinter + ".csv", "w")
        for venta in ventas:
          file.write(str(venta[0]) + "," + str(venta[1]) + "," + str(venta[2]) + "," + str(venta[3]) + "," + str(venta[4]) + "," + str(venta[5]) + "," + str(venta[6])+ "\n")           
        
def main():
    VENTreport= VentanaReportes()
    VENTreport.mainloop()


if __name__ == '__main__':
    main()"""