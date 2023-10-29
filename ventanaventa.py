import tkinter as tk
from tkinter import ttk
import mysql.connector

class Ventanaventas(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VENTANA VENTAS")
        self.resizable(0, 0)
        self.tablaventas()

    

    def tablaventas(self):
        self.tabla = ttk.Treeview(self, columns=('CODIGO_DE_VENTA', 'CODIGO_CLIENTE', 'CODIGO_PRODUCTOS', 'CANTIDAD_DE_PRODUCTOS', 'TOTAL_DE_VENTA', 'FECHA'))
        self.tabla.grid(row=7, column=0, columnspan=5, padx=10, pady=10)

        self.tabla.heading('#0', text='CODIGO_VENTA', anchor='center')
        self.tabla.heading('#1', text='CODIGO_CLIENTE', anchor='center')
        self.tabla.heading('#2', text='CODIGO_PRODUCTO', anchor='center')  
        self.tabla.heading('#3', text='CANTIDAD_PRODUCTOS', anchor='center')
        self.tabla.heading('#4', text='TOTAL_VENTA', anchor='center')
        self.tabla.heading('#5', text='FECHA', anchor='center')


        self.cargar_datos()
        self.campos_ventas()
        self.habilitar_campos_ventas()
        self.desabilitar_campos_ventas()
        self.guardar_datos_ventas()
        

    def cargar_datos(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                db="sistema_de_ventas"
            )
            cursor = conexion.cursor()
            cursor.execute("SELECT CODIGO_DE_VENTA, CODIGO_CLIENTE, CODIGO_PRODUCTOS, CANTIDAD_DE_PRODUCTOS, TOTAL_DE_VENTA, FECHA FROM ventas")

            ventas = cursor.fetchall()
            
            for fila in ventas:
                self.tabla.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5]))
            
            conexion.close()
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)

    def campos_ventas(self):
       
        self.label_codigocliente= tk.Label(self, text='Codigo del Cliente: ')
        self.label_codigocliente.config(font=('arial', 12, 'bold'))
        self.label_codigocliente.grid(row =9, column = 1, padx=10, pady=10)

        self.micodigocliente= tk.StringVar()
        self.entry_codigo_cliente= tk.Entry(self, textvariable=self.micodigocliente)
        self.entry_codigo_cliente.config(width=50, font=('arial',12))
        self.entry_codigo_cliente.grid(row=9,  column=1, padx=10, pady=10, columnspan=5)

        self.label_codigo_producto= tk.Label(self, text='Codigo del producto: ')
        self.label_codigo_producto.config(font=('arial', 12, 'bold'))
        self.label_codigo_producto.grid(row =10, column = 1, padx=10, pady=10)

        self.micodigo_producto= tk.StringVar()
        self.entry_codigo_produc= tk.Entry(self, textvariable=self.micodigo_producto)
        self.entry_codigo_produc.config(width=50, font=('arial',12))
        self.entry_codigo_produc.grid(row=10,  column=1, padx=10, pady=10, columnspan=5)

        self.label_cantidad_producto= tk.Label(self, text='Cantidad de Productos: ')
        self.label_cantidad_producto.config(font=('arial', 12, 'bold'))
        self.label_cantidad_producto.grid(row =11, column = 1, padx=10, pady=10)

        self.micantidad_product= tk.StringVar()
        self.entry_cant_produc= tk.Entry(self, textvariable=self.micantidad_product)
        self.entry_cant_produc.config(width=50, font=('arial',12))
        self.entry_cant_produc.grid(row=11,  column=1, padx=10, pady=10, columnspan=5)

        self.label_total_venta= tk.Label(self, text='monto Total: ')
        self.label_total_venta.config(font=('arial', 12, 'bold'))
        self.label_total_venta.grid(row =12, column = 1, padx=10, pady=10)

        self.mitotal= tk.StringVar()
        self.entry_total= tk.Entry(self, textvariable=self.mitotal)
        self.entry_total.config(width=50, font=('arial',12))
        self.entry_total.grid(row=12,  column=1, padx=10, pady=10, columnspan=5)
        
        self.label_fecha= tk.Label(self, text='fecha: ')
        self.label_fecha.config(font=('arial', 12, 'bold'))
        self.label_fecha.grid(row =13, column = 1, padx=10, pady=10)

        self.mifecha= tk.StringVar()
        self.entry_fecha= tk.Entry(self, textvariable=self.mifecha)
        self.entry_fecha.config(width=50, font=('arial',12))
        self.entry_fecha.grid(row=13,  column=1, padx=10, pady=10, columnspan=5)

        


   
        #botones
        self.BOTON_NUEVO_VENTAS= tk.Button(self, text='Nuevo', )
        self.BOTON_NUEVO_VENTAS.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#158645', cursor='hand2', activebackground='#35BD6F', activeforeground= '#DAD5D6')
        #self.BOTON_NUEVO_VENTAS.grid(row=5, column=0, padx=10, pady=10)


        self.BOTON_GUARDAR_VENTAS= tk.Button(self, text='guardar')
        self.BOTON_GUARDAR_VENTAS.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#1E1B7D', cursor='hand2', activebackground='#6B69DE', activeforeground='#DAD5D6')

       # self.BOTON_GUARDAR_VENTAS.grid(row=5, column=1, padx=10, pady=10)


        self.BOTONCCANCELAR_VENTASr= tk.Button(self, text='cancelar') 
        self.BOTONCCANCELAR_VENTASr.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#882686', cursor='hand2', activebackground='#EA7BE6', activeforeground='#DAD5D6')

        #self.BOTONCCANCELAR_VENTASr.grid(row=5, column=4, padx=10, pady=10)

        self.BOTON_EDITAR_VENTASr= tk.Button(self, text='editar')
        self.BOTON_EDITAR_VENTASr.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#8A1B0B', cursor='hand2', activebackground='#EA7464', activeforeground='#DAD5D6')

        #self.BOTON_EDITAR_VENTASr.grid(row=5, column=2, padx=10, pady=10)

        self.BOTON_ELIMINAR_VENTAS= tk.Button(self, text='eliminar')
        self.BOTON_ELIMINAR_VENTAS.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#882686', cursor='hand2', activebackground='#EA7BE6', activeforeground='#DAD5D6')

        #self.BOTONELIMINAR_VENTAS.grid(row=5, column=3, padx=10, pady=10) 

        # Botones
        self.BOTON_NUEVO_VENTAS.grid(row=5, column=0, padx=10, pady=10)
        self.BOTON_GUARDAR_VENTAS.grid(row=5, column=1, padx=10, pady=10)
        self.BOTON_EDITAR_VENTASr.grid(row=5, column=2, padx=10, pady=10)
        self.BOTON_ELIMINAR_VENTAS.grid(row=5, column=3, padx=10, pady=10)
        self.BOTONCCANCELAR_VENTASr.grid(row=5, column=4, padx=10, pady=10)
                    
    def guardar_datos_ventas(self):
       
        codigo_cliente = self.entry_codigo_cliente.get()
        codigo_producto = self.entry_codigo_produc.get()
        cantidad_de_productos = self.entry_cant_produc.get()
        total_venta = self.entry_total.get()
        fecha = self.entry_fecha.get()


        insert=("INSERT INTO ventas (CODIGO_CLIENTE,CODIGO_PRODUCTOS, CANTIDAD_DE_PRODUCTOS, TOTAL_DE_VENTA, FECHA) values(%s, %s, %s, %s, %s)")
        valores=(codigo_cliente, codigo_producto, cantidad_de_productos, total_venta, fecha)
        conexion= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            db="sistema_de_ventas"
        )
        cursor=conexion.cursor()
        cursor.execute(insert, valores)
        conexion.commit()
        conexion.close()
        self.desabilitar_campos_ventas()       
        self.tablaventas()

      
        
        

    def habilitar_campos_ventas(self):
         #para enviar campos vacios, osea limpiar cada vez que demos cancelar, creamos arriba los objetos de stringvar
         #self.mi_codigo.set('')
         self.micodigocliente.set('')
         self.micodigo_producto.set('')
         self.micantidad_product.set('')
         self.mitotal.set('')
         self.mifecha.set('')
         #para el estado de los entrys
         #self.entry_codigo.config(state='normal')
         self.entry_codigo_cliente.config(state='normal')
         self.entry_cant_produc.config(state='normal')
         self.entry_cant_produc.config(state='normal')
         self.entry_total.config(state='normal')
         self.entry_fecha.config(state='normal')
             #para los botones
         #self.boton_editar.config(state='normal')
         self.BOTON_GUARDAR_VENTAS.config(state='normal')
         self.BOTONCCANCELAR_VENTASr.config(state='normal')
                 
            

    def  desabilitar_campos_ventas(self):
         #para enviar campos vacios, osea limpiar cada vez que demos cancelar, creamos arriba los objetos de stringvar
         #self.mi_codigo.set('')
         self.micodigocliente.set('')
         self.micodigo_producto.set('')
         self.micantidad_product.set('')
         self.mitotal.set('')
         self.mifecha.set('')

         
             #para los entrys
         #self.entry_codigo.config(state='disabled')
         
         self.entry_codigo_cliente.config(state='disabled')
         self.entry_cant_produc.config(state='disabled')
         self.entry_cant_produc.config(state='disabled')
         self.entry_total.config(state='disabled')
         self.entry_fecha.config(state='disabled')
             #para los botones
         #self.boton_editar.config(state='disabled')

         self.BOTON_GUARDAR_VENTAS.config(state='disabled')
         self.BOTONCCANCELAR_VENTASr.config(state='disabled')

def MAIN():
    Ventanaventa = Ventanaventas()
    Ventanaventas.mainloop()

if __name__ == '__main__':
    MAIN()
