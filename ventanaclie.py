import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import Button, Grid, Label

class VentanaClient(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("VENTANA CLIENTES")
        self.resizable(0, 0)
        self.tablaclientes()

    

    def tablaclientes(self):
        self.tabla = ttk.Treeview(self, columns=('CODIGO', 'NOMBRE_CLIENTE', 'DIRECCION', 'TELEFONO', 'CORREO'))
        self.tabla.grid(row=6, column=0, columnspan=5, padx=10, pady=10)
        
        self.tabla.heading('#1', text='CODIGO', anchor='center')
        self.tabla.heading('#2', text='NOMBRE', anchor='center')
        self.tabla.heading('#3', text='DIRECCION', anchor='center')
        self.tabla.heading('#4', text='TELEFONO', anchor='center')
        self.tabla.heading('#5', text='CORREO', anchor='center')

        self.cargar_datos()
        self.campos()

    def cargar_datos(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                db="sistema_de_ventas"
            )
            cursor = conexion.cursor()
            cursor.execute("SELECT CODIGO_CLIENTE, NOMBRE_CLIENTE, DIRECCION, TELEFONO, CORREO FROM clientes")
            clientes = cursor.fetchall()
            
            for fila in clientes:
                self.tabla.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3], fila[4]))
            
            conexion.close()
        except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)

    def campos(self):
       
        self.label_Nombrecliente= tk.Label(self, text='NOMBRE: ')
        self.label_Nombrecliente.config(font=('arial', 12, 'bold'))
        self.label_Nombrecliente.grid(row =7, column = 1, padx=10, pady=10)

        self.minombreclien= tk.StringVar()
        self.entry_nombre= tk.Entry(self, textvariable=self.minombreclien)
        self.entry_nombre.config(width=50, font=('arial',12))
        self.entry_nombre.grid(row=7,  column=1, padx=10, pady=10, columnspan=5)

        self.label_direccioncliente= tk.Label(self, text='direccion: ')
        self.label_direccioncliente.config(font=('arial', 12, 'bold'))
        self.label_direccioncliente.grid(row =8, column = 1, padx=10, pady=10)

        self.midireccionclien= tk.StringVar()
        self.entry_direccion= tk.Entry(self, textvariable=self.midireccionclien)
        self.entry_direccion.config(width=50, font=('arial',12))
        self.entry_direccion.grid(row=8,  column=1, padx=10, pady=10, columnspan=5)

        self.label_telefonocliente= tk.Label(self, text='telefono: ')
        self.label_telefonocliente.config(font=('arial', 12, 'bold'))
        self.label_telefonocliente.grid(row =9, column = 1, padx=10, pady=10)

        self.mitelefonoclien= tk.StringVar()
        self.entry_telefono= tk.Entry(self, textvariable=self.mitelefonoclien)
        self.entry_telefono.config(width=50, font=('arial',12))
        self.entry_telefono.grid(row=9,  column=1, padx=10, pady=10, columnspan=5)

        self.label_correocliente= tk.Label(self, text='correo: ')
        self.label_correocliente.config(font=('arial', 12, 'bold'))
        self.label_correocliente.grid(row =10, column = 1, padx=10, pady=10)

        self.micorreoclien= tk.StringVar()
        self.entry_correo= tk.Entry(self, textvariable=self.micorreoclien)
        self.entry_correo.config(width=50, font=('arial',12))
        self.entry_correo.grid(row=10,  column=1, padx=10, pady=10, columnspan=5)
        #botones
        self.BOTON_NUEVO_CLIENTES= tk.Button(self, text='Nuevo', )
        self.BOTON_NUEVO_CLIENTES.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#158645', cursor='hand2', activebackground='#35BD6F', activeforeground= '#DAD5D6')
        #self.BOTON_NUEVO_CLIENTES.grid(row=5, column=0, padx=10, pady=10)


        self.BOTON_GUARDAR_CLIENTES= tk.Button(self, text='guardar')
        self.BOTON_GUARDAR_CLIENTES.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#1E1B7D', cursor='hand2', activebackground='#6B69DE', activeforeground='#DAD5D6')

       # self.BOTON_GUARDAR_CLIENTES.grid(row=5, column=1, padx=10, pady=10)


        self.BOTONCANCELARr= tk.Button(self, text='cancelar') 
        self.BOTONCANCELARr.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#882686', cursor='hand2', activebackground='#EA7BE6', activeforeground='#DAD5D6')

        #self.BOTONCANCELARr.grid(row=5, column=4, padx=10, pady=10)

        self.BOTON_EDITARr= tk.Button(self, text='editar')
        self.BOTON_EDITARr.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#8A1B0B', cursor='hand2', activebackground='#EA7464', activeforeground='#DAD5D6')

        #self.BOTON_EDITARr.grid(row=5, column=2, padx=10, pady=10)

        self.BOTN_ELIMINARr= tk.Button(self, text='eliminar')
        self.BOTN_ELIMINARr.config(width=20, font=('arial', 12, 'bold'),
        fg='#DAD5D6',bg='#882686', cursor='hand2', activebackground='#EA7BE6', activeforeground='#DAD5D6')

        #self.BOTN_ELIMINARr.grid(row=5, column=3, padx=10, pady=10) 

        # Botones
        self.BOTON_NUEVO_CLIENTES.grid(row=5, column=0, padx=10, pady=10)
        self.BOTON_GUARDAR_CLIENTES.grid(row=5, column=1, padx=10, pady=10)
        self.BOTON_EDITARr.grid(row=5, column=2, padx=10, pady=10)
        self.BOTN_ELIMINARr.grid(row=5, column=3, padx=10, pady=10)
        self.BOTONCANCELARr.grid(row=5, column=4, padx=10, pady=10)
            
        


def main():
    ventClient = VentanaClient()
    ventClient.mainloop()

if __name__ == '__main__':
    main()
