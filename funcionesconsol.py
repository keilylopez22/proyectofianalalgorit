def listar_productos(productos):
    
   
    print("\nproductos: \n")
    contador= 1
    for product in productos:
        datos = "{0}. CODIGO_PRODUCTO: {1} | NOMBRE_PRODUCTO: {2}  |EXISTENCIAS: {3}  |PROVEEDOR: {4} ({5} PRECIO:)"
        print(datos.format(contador, product[0], product[1], product[2], product[3], product[4]))
        contador= contador+1
        print(" ")

#esta funcion es la que nos va a guardar los datos de los productos que creermos
def pedirdatosproducto():  
       nombre_producto= input("ingrese el nombre del producto: ")
       
       existencias_correctas= False
       while(not existencias_correctas):
             existencias_producto= input("ingrese las existencias de ese producto: ")
          
             if existencias_producto.isnumeric():
                  if (int(existencias_producto) > 0):
                      existencias_correctas= True
                      existencias_producto= int(existencias_producto)
                  else:
                       print("sus existencias tienen que ser mayor a 0, producto AGOTADO")  
             else:
                  print("existencias incorrectas: parece que ingresaste un texto, ingtresa un numero por favor")     
       proveedor_del_producto= input("ingrese el nombre del provvedor: ")
         #recordatorio para arreglarlo me crea el producto aun cuando ingreso cero y no tendria por dicha validacion
       precio_correcto= False
       while( not precio_correcto):
            
             precio_producto= (input("ingresa el precio: "))
             if precio_producto.isnumeric():
                  if (float(precio_producto) > 0):
                       precio_correcto= True
                       precio_producto= float(precio_producto)
                       
                  else:
                       print("el precio debe ser mayor a 0")
             else:
                  print("precio incorrecto: parece que ingresaste un texto, ingresa valores numericos por favor")          

       productos=(nombre_producto, existencias_producto, proveedor_del_producto, precio_producto)
       return productos

def pedirproductos(productos):
     listar_productos(productos)
     codigoproducExiste = False
     codigoEditar = input("ingrese el codigo del producto que deseaa editar: ")
     for produt in productos:
          if (str(produt[0]) == codigoEditar):
               codigoproducExiste = True
               break
     if codigoproducExiste:     
          #else:
              # print("codigo incorrecto: el codigo no debe ser mayor a 6 digitos")    
          nombre_producto= input("ingrese el nombre del producto: ")
          
          existencias_correctas= False
          while(not existencias_correctas):
               existencias_producto= input("ingrese las existencias de ese producto: ")
               
               if existencias_producto.isnumeric():
                    if (int(existencias_producto) > 0):
                         existencias_correctas= True
                         existencias_producto= int(existencias_producto)
                    else:
                         print("sus existencias tienen que ser mayor a 0, producto AGOTADO")  
               else:
                    print("existencias incorrectas: parece que ingresaste un texto, ingtresa un numero por favor")     
          proveedor_del_producto= input("ingrese el nombre del provvedor: ")
         

          #recordatorio para arreglarlo me crea el producto aun cuando ingreso cero y no tendria por dicha validacion
          precio_correcto= False
          while( not precio_correcto):
               
               precio_producto= (input("ingresa el precio: "))
               if precio_producto.isnumeric():
                    if (float(precio_producto) > 0):
                         precio_correcto= True
                         precio_producto= float(precio_producto)
                         
                    else:
                         print("el precio debe ser mayor a 0")
               else:
                    print("precio incorrecto: parece que ingresaste un texto, ingresa valores numericos por favor")
               productos= (codigoEditar, nombre_producto, existencias_producto, proveedor_del_producto, precio_producto)
     else:productos= None
     return productos                   
          
          


def pedir_productos_eliminacion(productos):
     listar_productos(productos)
     codigoproducExiste= False
     codigoEliminar= input("ingrese el codigo del producto que deseaa eliminar: ")
     
     for produt in productos:
          

          if (str (produt[0]) == codigoEliminar):
               codigoproducExiste= True
               break
     if not codigoproducExiste:
          codigoEliminar= ""   
     return codigoEliminar   






