#para los windets
import tkinter as tk
from tkinter import ttk,Listbox
from ventanaclie import VentanaClient
from ventanaventa import Ventanaventas
from ventanareportes import VentanaReportes
import mysql.connector


#menu principal
def barra_menu(ventana_raiz):
    barra_menu = tk.Menu(ventana_raiz)
    ventana_raiz.config(menu = barra_menu, width=300, height=300)

    #primer menu (menu de inicio)
    menu_productos= tk.Menu(barra_menu, tearoff=0) 
    #para agregarlo
    
    
    clientes= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Clientes',menu= clientes )
    clientes.add_command(label='ABRIR', command=VentanaClient)
    clientes.add_separator()
    clientes.add_command(label='CERRAR')
    clientes.add_separator()
    clientes.add_command(label='SALIR') 

    
    ventas= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Ventas', menu= ventas)
    ventas.add_command(label='ABRIR', command=Ventanaventas)
    ventas.add_separator()
    ventas.add_command(label='CERRAR')
    ventas.add_separator()
    ventas.add_command(label='SALIR') 

    
    Reportes_Basicos= tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Reportes basicos', menu=Reportes_Basicos )
    Reportes_Basicos.add_command(label='ABRIR', command=VentanaReportes)
    
#
class frame(tk.Frame):
    def crear_conexion():
        conexion= mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            db="sistema_de_ventas"
      )
        return conexion
    def __init__(self,ventana_raiz= None ):
        super().__init__(ventana_raiz, width=480, height=320)
        self.ventana_raiz = ventana_raiz
        self.pack()
        #self.config( bg='green')
     #para ejecutar campos
        self.campos()
        #grid

        #para ejecutar desabilitar_campos
        self.desabilitar_campos()
        #para  ejecutar habilitar_campos
        self.habilitar_campos()

        #para dibujar la tabla
        self.tabla_productos()
         
       
    
    #
    def campos(self):
            #label de cada campo
            #self.label_codigo =tk.Label(self, text='codigo: ')
            #self.label_codigo.config(font=('arial', 12, 'bold'))
            #self.label_codigo.grid(row =0, column = 0, padx=10, pady=10)
            
            self.label_nombre =tk.Label(self, text='nombre: ')
            self.label_nombre.config(font=('arial', 12, 'bold'))
            self.label_nombre.grid(row =1, column = 0, padx=10, pady=10)

            self.label_existencias =tk.Label(self, text='existencias: ')
            self.label_existencias.config(font=('arial', 12, 'bold'))
            self.label_existencias.grid(row =2, column = 0, padx=10, pady=10)
            
            self.label_proveedor =tk.Label(self, text='proveedor: ')
            self.label_proveedor.config(font=('arial', 12, 'bold'))
            self.label_proveedor.grid(row =3, column = 0, padx=10, pady=10)

            self.label_precio =tk.Label(self, text='precio: ')
            self.label_precio.config(font=('arial', 12, 'bold'))
            self.label_precio.grid(row =4, column = 0, padx=10, pady=10)

            
            #entrys, los campos de entrada
            #creamos el objeto
            #self.mi_codigo= tk.StringVar()
            #self.entry_codigo= tk.Entry(self, textvariable=self.mi_codigo)
            #self.entry_codigo.config(width=50, font=('arial',12))
            #lo empaquetamos con la drid
            #self.entry_codigo.grid(row=0,  column=1, padx=10, pady=10, columnspan=5)

            self.mi_nombre= tk.StringVar()
            self.entry_nombre= tk.Entry(self, textvariable=self.mi_nombre)
            self.entry_nombre.config(width=50, font=('arial',12))
            self.entry_nombre.grid(row=1,  column=1, padx=10, pady=10, columnspan=5)

            self.mi_existencias= tk.StringVar()
            self.entry_existencias= tk.Entry(self, textvariable=self.mi_existencias)
            self.entry_existencias.config(width=50, font=('arial',12))
            self.entry_existencias.grid(row=2,  column=1, padx=10, pady=10, columnspan=5)

            self.mi_proveedor= tk.StringVar()
            self.entry_proveedor= tk.Entry(self, textvariable=self.mi_proveedor)
            self.entry_proveedor.config(width=50, font=('arial',12))
            self.entry_proveedor.grid(row=3,  column=1, padx=10, pady=10, columnspan=5)

            self.mi_precio= tk.StringVar()
            self.entry_precio= tk.Entry(self, textvariable=self.mi_precio)
            self.entry_precio.config(width=50, font=('arial',12))
            self.entry_precio.grid(row=4,  column=1, padx=10, pady=10, columnspan=5)

            #botones
            self.boton_nuevo= tk.Button(self, text='Nuevo', command=self.habilitar_campos)
            self.boton_nuevo.config(width=20, font=('arial', 12, 'bold'),
            fg='#DAD5D6',bg='#158645', cursor='hand2', activebackground='#35BD6F', activeforeground= '#DAD5D6')

            self.boton_nuevo.grid(row=5, column=0, padx=10, pady=10)

           

            self.boton_guardar= tk.Button(self, text='guardar', command=self.guardar_datos)
            self.boton_guardar.config(width=20, font=('arial', 12, 'bold'),
            fg='#DAD5D6',bg='#1E1B7D', cursor='hand2', activebackground='#6B69DE', activeforeground='#DAD5D6')

            self.boton_guardar.grid(row=5, column=1, padx=10, pady=10)

            """self.boton_existencias= tk.Button(self, text='existencias', command=self.habilitar_campos)
            self.boton_existencias.config(width=20, font=('arial', 12, 'bold'),
            fg='#DAD5D6',bg='#882686', cursor='hand2', activebackground='#EA7BE6', activeforeground='#DAD5D6')

            self.boton_existencias.grid(row=5, column=2, padx=10, pady=10)"""

            self.boton_cancelar= tk.Button(self, text='cancelar', command=self.desabilitar_campos)
            self.boton_cancelar.config(width=20, font=('arial', 12, 'bold'),
            fg='#DAD5D6',bg='#882686', cursor='hand2', activebackground='#EA7BE6', activeforeground='#DAD5D6')

            self.boton_cancelar.grid(row=7, column=2, padx=10, pady=10)




            #metodo para habilitar los campos

    def habilitar_campos(self):
         #para enviar campos vacios, osea limpiar cada vez que demos cancelar, creamos arriba los objetos de stringvar
         #self.mi_codigo.set('')
         self.mi_nombre.set('')
         self.mi_existencias.set('')
         self.mi_proveedor.set('')
         self.mi_precio.set('')
         #para el estado de los entrys
         #self.entry_codigo.config(state='normal')
         self.entry_nombre.config(state='normal')
         self.entry_existencias.config(state='normal')
         self.entry_proveedor.config(state='normal')
         self.entry_precio.config(state='normal')
             #para los botones
         #self.boton_editar.config(state='normal')
         self.boton_guardar.config(state='normal')
         self.boton_cancelar.config(state='normal')
                 
            

    def  desabilitar_campos(self):
         #para enviar campos vacios, osea limpiar cada vez que demos cancelar, creamos arriba los objetos de stringvar
         #self.mi_codigo.set('')
         self.mi_nombre.set('')
         self.mi_existencias.set('')
         self.mi_proveedor.set('')
         self.mi_precio.set('')
             #para los entrys
         #self.entry_codigo.config(state='disabled')
         self.entry_nombre.config(state='disabled')
         self.entry_existencias.config(state='disabled')
         self.entry_proveedor.config(state='disabled')
         self.entry_precio.config(state='disabled')
         
             #para los botones
         #self.boton_editar.config(state='disabled')
         self.boton_guardar.config(state='disabled')
         self.boton_cancelar.config(state='disabled')

    #para que despues de guardar se obtengan los datos y se limpien los entrys lo haremos con el metodo get arriba  lo hicimos con los entris para el boton cancelar con el metodo set y que para eso creamos un objetp con la 
    #clase strigvar
    def guardar_datos(self):
        #codigo_producto = self.entry_codigo.get()
        nombre_producto = self.entry_nombre.get()
        existencias_producto = self.entry_existencias.get()
        proveedor_producto = self.entry_proveedor.get()
        precio_producto = self.entry_precio.get()


        insert=("INSERT INTO inventario (NOMBRE_PRODUCTO, EXISTENCIAS, PROVEEDOR, PRECIO) values(%s, %s, %s, %s)")
        valores=(nombre_producto, existencias_producto, proveedor_producto, precio_producto)
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
        self.desabilitar_campos()
        self.tabla_productos()
        

    """def editar_datos(self, PRIMARY_KEY):
        insert= ("SELECT NOMBRE_PRODUCTO, EXITENCIAS, PROVEEDOR, PRECIO FROM")
        valores=(PRIMARY_KEY)

        conexion= mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="",
              db="sistema_de_ventas"
        )

        cursor=conexion.cursor()
        cursor.execute(insert, valores)
        resultado=cursor.fetchone()

        self.entry_nombre.delete(0, 'end')
        self.entry_nombre.insert(0, resultado[0])
        self.entry_existencias.delete(0,'end')
        self.entry_existencias.insert(0, resultado[1])
        self.entry_proveedor.delete(0, 'end')
        self.entry_proveedor.insert(0,resultado[2])
        self.entry_precio.delete(0, 'end')
        self.entry_precio.insert(0, resultado[3])

        self.label.codigo.config(tex=str(PRIMARY_KEY))
    
        #self.desabilitar_campos()  """

    #para diseñar las tablas  
    def tabla_productos(self):
   #para hacerlo tenemos que importar el ttk arribita y con tkk empezaremos a crear la tabla con la funcion treeview
      self.tabla= ttk.Treeview(self,
      column = ('CODIGO' ,'NOMBRE' ,'EXISTENCIAS','PROVEEDOR', 'PRECIO' ))
      self.tabla.grid(row=6, column=0, columnspan=5)

      #para darle el nombre a cada columna de la tabla

      self.tabla.heading('#1',text='CODIGO', anchor='center')
      self.tabla.heading('#2',text='NOMBRE', anchor='center')
      self.tabla.heading('#3',text='EXISTENCIAS', anchor='center')
      self.tabla.heading('#4',text='PROVEEDOR', anchor='center')
      self.tabla.heading('#5',text='PRECIO', anchor='center')
     

      #insertar datos

     
      
      conexion= mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="",
              db="sistema_de_ventas"
      )
      cursor = conexion.cursor()
      cursor.execute("SELECT CODIGO_PRODUCTO, NOMBRE_PRODUCTO, EXISTENCIAS, PROVEEDOR, PRECIO FROM inventario")
      productos = cursor.fetchall()
      conexion.close()
      for fila in productos:
           self.tabla.insert("","end",
       values=(fila[0], fila[1], fila[2],fila[3],fila[4]))
#para que se dibuje la tabla hay que llamarlo desde el constructor que esta arriba

#botones
      self.boton_editar= tk.Button(self, text='editar')
      self.boton_editar.config(width=20, font=('arial', 12, 'bold'),
      fg='#DAD5D6',bg='#8A1B0B', cursor='hand2', activebackground='#EA7464', activeforeground='#DAD5D6')

      self.boton_editar.grid(row=5, column=3, padx=10, pady=10)

      self.boton_eliminar= tk.Button(self, text='eliminar')
      self.boton_eliminar.config(width=20, font=('arial', 12, 'bold'),
            fg='#DAD5D6',bg='#882686', cursor='hand2', activebackground='#EA7BE6', activeforeground='#DAD5D6')

      self.boton_eliminar.grid(row=5, column=4, padx=10, pady=10)

    


        
            
        
    

