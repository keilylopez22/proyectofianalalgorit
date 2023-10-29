import mysql.connector
from mysql.connector import Error
"DAO data Acces objet"
import datetime
import openpyxl
import csv
class DAOconsol():
    def __init__(self):
      try:
        self.conexionconsol= mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'sistema_de_ventas'

        )
      except Error as ex:
           print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))


    def multiplicacion(self):
        if self.conexionconsol.is_connected():
          try:
            cursor=self.conexionconsol.cursor()  
            cursor.execute("INSERT INTO [ventas] ([TOTAL_DE_VENTA]) " 
            "SELECT [inventario].valora * [inventario]. FROM [inventario], [inventario]; ")
            resultados=cursor.fetchall()
            return resultados
               
          except Error as ex:
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))
          pass    
       

    #para a empezar vamos a hacer la consulta de los productros correspondientes 

    def listar_productos(self):
        if self.conexionconsol.is_connected():
          try:
            cursor=self.conexionconsol.cursor()  
            cursor.execute("SELECT * FROM  inventario ORDER BY CODIGO_PRODUCTO")
            resultados=cursor.fetchall()
            return resultados
               
          except Error as ex:
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))  


    def crear_productos(self, productos):
       if self.conexionconsol.is_connected():
          try:
             cursor=self.conexionconsol.cursor()
             sql=" INSERT INTO inventario (NOMBRE_PRODUCTO, EXISTENCIAS, PROVEEDOR, PRECIO) VALUES('{0}','{1}','{2}','{3}')"
             
             cursor.execute(sql.format(productos[0], productos[1], productos[2], productos[3]))
             self.conexionconsol.commit() 
             print("¡producto creado! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))

    def actualizarProducto(self, productos):
      
                
        if self.conexionconsol.is_connected():
          try:
              cursor=self.conexionconsol.cursor()
              sql= "UPDATE inventario SET NOMBRE_PRODUCTO= '{0}', EXISTENCIAS='{1}', PROVEEDOR='{2}', PRECIO='{3}' WHERE CODIGO_PRODUCTO = '{4}'"
              cursor.execute(sql.format(productos[1], productos[2], productos[3], productos[4], productos[0]))
              self.conexionconsol.commit() 
              print("¡inventario actualizado! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex)) 

                
    def actualizar_cliente(self, clientes):
        if self.conexionconsol.is_connected():
          try:
             cursor=self.conexionconsol.cursor()
             sql=" UPDATE clientes SET  NOMBRE_CLIENTE= '{0}', DIRECCION='{1}', TELEFONO='{2}', CORREO={3} WHERE CODIGO_CLIENTE = '{4}'"
             
             cursor.execute(sql.format(clientes[1], clientes[2], clientes[3], clientes[4], clientes[0]))
             self.conexionconsol.commit() 
             print("¡CLIENTES actualizados! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex)) 

    def eliminar_Producto (self, codigo_producto_eliminar ): 
        if self.conexionconsol.is_connected():
          try:
             cursor=self.conexionconsol.cursor()
             sql= "DELETE FROM inventario WHERE CODIGO_PRODUCTO= '{0}'"
             
             cursor.execute(sql.format(codigo_producto_eliminar))
             self.conexionconsol.commit() 
             print("¡producto ELIMINADO! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))



    """#estas funciones son para hacer la conexion con clientes y las de arriba son para productos, y la primera es 
    la que me conecta con la base de datos de mi phpmyadmin
   """    

    def listar_clientes(self):

        if self.conexionconsol.is_connected():
          try:
            cursor=self.conexionconsol.cursor()  
            cursor.execute("SELECT * FROM  clientes ORDER BY CODIGO_CLIENTE")
            resultados=cursor.fetchall()
            return resultados
               
          except Error as ex:
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex)) 

    #crear los clientes
    def crear_clientes(self, clientes):
       if self.conexionconsol.is_connected():
          try:
             cursor=self.conexionconsol.cursor()
             sql=" INSERT INTO clientes (NOMBRE_CLIENTE, DIRECCION, TELEFONO, CORREO) VALUES('{0}','{1}','{2}','{3}')"
             
             cursor.execute(sql.format(clientes[1], clientes[2], clientes[3], clientes[4]))
             self.conexionconsol.commit() 
             print("¡cliente creado! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))

    def editaractualizar_cliente(self, clientes):
        if self.conexionconsol.is_connected():
          try:
             cursor=self.conexionconsol.cursor()
             sql=" UPDATE  clientes SET  NOMBRE_CLIENTE= '{0}', DIRECCION='{1}', TELEFONO='{2}', CORREO= '{3}' WHERE CODIGO_CLIENTE = '{4}'"
             print((sql.format(clientes[1], clientes[2], clientes[3], clientes[4], clientes[0])))
             cursor.execute(sql.format(clientes[1], clientes[2], clientes[3], clientes[4], clientes[0]))
             
             self.conexionconsol.commit() 
             print("¡CLIENTES actualizados! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))



    def eliminar_clientes (self, codigo_clientes_eliminar ): 
        if self.conexionconsol.is_connected():
          try:
            cursor=self.conexionconsol.cursor()
            sql= "DELETE FROM clientes WHERE CODIGO_CLIENTE= '{0}'"
             
            cursor.execute(sql.format(codigo_clientes_eliminar))
            self.conexionconsol.commit() 
            print("clientes ELIMINADO! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))      


    """#estas funciones son para hacer la conexion con las ventas y las de arriba son para clientes, productos, y la primera es 
    la que me conecta con la base de datos de mi phpmyadmin
   """             
    def listar_ventas(self):
        if self.conexionconsol.is_connected():  
          try:
            cursor=self.conexionconsol.cursor()  
            cursor.execute("SELECT * FROM  ventas ORDER BY CODIGO_DE_VENTA")
            resultados=cursor.fetchall()
            return resultados
          except Error as ex:

            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex)) 


    def crear_ventas(self, ventas):
       if self.conexionconsol.is_connected():
          try:
             print(ventas)
             cursor=self.conexionconsol.cursor()
             sql=" INSERT INTO ventas (CODIGO_CLIENTE, CODIGO_PRODUCTOS, CANTIDAD_DE_PRODUCTOS, TOTAL_DE_VENTA, FECHA) VALUES('{0}','{1}','{2}','{3}','{4}')"
             
             cursor.execute(sql.format(ventas[0], ventas[1], ventas[2], ventas[3], ventas[4]))
             self.actualizar_existencias(ventas[1], ventas[2]*(-1))
             self.conexionconsol.commit() 
             print("¡venta creada! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))

    def eliminar_ventas (self, codigo_venta_eliminar ): 
        if self.conexionconsol.is_connected():
          try:
            print(codigo_venta_eliminar)
            cursor=self.conexionconsol.cursor()
            sql= "UPDATE ventas SET ESTADO = 0 WHERE CODIGO_DE_VENTA= '{0}'"
             
            cursor.execute(sql.format(codigo_venta_eliminar))
            actualizados = cursor.rowcount
            if actualizados > 0:
              self.conexionconsol.commit()
              sql2="SELECT CANTIDAD_DE_PRODUCTOS, CODIGO_PRODUCTOS FROM ventas WHERE CODIGO_DE_VENTA= '{0}'"
              cursor.execute(sql2.format(codigo_venta_eliminar))
              resultado= cursor.fetchall()
              fila=resultado[0]
              self.actualizar_existencias(int(fila[1]), int(fila[0]))
              print("venta ANULADA! \n")
            else:
               print("La venta ya se encontraba anulada!")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex)) 

    def actualizar_existencias(self, productos, cantidad):
        #print(str(productos) + " - " + str(cantidad))
        if self.conexionconsol.is_connected():
          try:
             cursor=self.conexionconsol.cursor()
             sql=" UPDATE inventario SET EXISTENCIAS=EXISTENCIAS+{0} WHERE CODIGO_PRODUCTO = '{1}'"
             #print(sql.format(cantidad, productos))
             cursor.execute(sql.format(cantidad, productos))
             self.conexionconsol.commit() 
             print("¡inventario actualizado! \n")
          
          except Error as ex:
                      
            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))                           
   

    def generar_reportes_por_cliente(self, codigo_cliente):
        if self.conexionconsol.is_connected():  
          try:
            cursor=self.conexionconsol.cursor()  
            cursor.execute("SELECT * FROM  ventas WHERE CODIGO_CLIENTE={0} ORDER BY CODIGO_DE_VENTA".format(codigo_cliente))
            resultados=cursor.fetchall()
            return resultados
          except Error as ex:

            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))


    def generar_reportes_por_producto(self, codigo_producto):
        if self.conexionconsol.is_connected():  
          try:
            cursor=self.conexionconsol.cursor()  
            cursor.execute("SELECT * FROM  ventas WHERE CODIGO_PRODUCTOS={0} ORDER BY CODIGO_DE_VENTA".format(codigo_producto))
            resultados=cursor.fetchall()
            return resultados
          except Error as ex:

            print("ERROR AL INTENTAR LA CONEXION CON LA BASE DE DATOS: {0}".format(ex))
    

   