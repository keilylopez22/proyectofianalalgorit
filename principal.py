#haremos el inventario.pypor consola
from BD.conexionconsol import DAOconsol
import funcionesconsol
from funcionclie import listar_cliente, pedirdatosclientes, pedir_clientes_eliminacion, pedirdatosclientes
from funcionventas import listar_ventas, pedirdatosventas, pedir_ventas_eliminacion, generar_excel
import traceback
import mysql.connector
from funcionesconsol import pedirproductos

"creamos una funcion que nos muestre las opciones que tenemos hacerca de productos"
def menu_principal():
    continuar= True
    while(continuar):
        opcion_correcta= False
        while(not opcion_correcta):
            print("=== MENU PRINCIPAL ===")
            print("1.-LISTAR PRODUCTO")
            print("2.- CREAR PRODUCTO")
            print("3.- EDITAR EXISTENCIAS DEL PRODUCTO")
            print("4.- ELIMINAR PRODUCTO")
            print("5.- VER CLIENTES")
            print("6.- VER VENTAS")
            print("7.- SALIR")
            print("===")
            opcion= int(input("seleccione una opcion por favor: "))
            #while menu_principal:
            
            if opcion <1 or opcion >7:
                print("opcion no valida por favor ingrese una opcion correcta")
            elif opcion ==7:
                continuar= False
                print("gracias por usar este programa") 
                break  
            else:
                opcion_correcta= True
                EjecutarOpcion(opcion)  

def EjecutarOpcion(opcion):
    dao= DAOconsol()
    if opcion ==1:
        try:
            productos= dao.listar_productos()
            if len(productos)>0:
                funcionesconsol.listar_productos(productos)
            else:
                print("no se encontraron productos...")   

        except:
            print("a ocurrido algun error")    

    elif opcion == 2:
       productos= funcionesconsol.pedirdatosproducto()
       try:
           dao.crear_productos(productos)
       except:  
           print("ocurrio un error")  
    elif opcion == 3:
        try:
            productos = dao.listar_productos()
            if len(productos) > 0:
                codigoEditar = funcionesconsol.pedirproductos(productos)
                if not (codigoEditar == ""):
                    nuevas_existencias = int(input("Ingrese las nuevas existencias del producto: "))
                    dao.actualizarProducto(codigoEditar, nuevas_existencias)
                else:
                    print("Código de producto no encontrado...\n")
            else:
                print("No se encontraron productos... ")
        except Exception as err:
            traceback.print_exc()

            

     
    elif opcion == 4:
        try:
            productos= dao.listar_productos()
            if len(productos)>0:
               codigoEliminar = funcionesconsol.pedir_productos_eliminacion(productos)
               if  not(codigoEliminar == ""):
                   dao.eliminar_Producto(codigoEliminar)
               else:
                   print("codigo de producto no encontrado...\n")  
            else:
                print("no se encontraron productos... ")        
        except:
            print("A ocurrido un error...")   
        else:print("opcion no valida")     

         
    elif opcion ==5:
        
        menu_clientes()
       
     
        
    elif opcion ==6 :
       
     menu_ventas()
           

#Empieza menu clientes
def menu_clientes():
    continuar= True
    while(continuar):
        print("=== MENÚ CLIENTES ===")
        print("1. Listar Clientes")
        print("2. Crear Cliente")
        print("3. Editar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        print("6. Salir")
        print("===")
        opcion_correcta= False 
        while(True):
           
            opcion= int(input("seleccione una opcion por favor: "))
            #while menu_principal:
            
            if (opcion < 1 or opcion > 6):
                print("opcion cliente no valida por favor ingrese una opcion cliente correcta")
            elif opcion == 6:
                continuar = False
                print("gracias por usar este programa") 
                break  
            else:
                EjecutaropcionClientes(opcion)

def EjecutaropcionClientes(opcion):
    dao= DAOconsol()

    if opcion == 1:
        try:
            cliente= dao.listar_clientes()
            if len(cliente)>0:
                listar_cliente(cliente)
            else:
                print("no se encontraron clientes...")   

        except Exception as err:
            traceback.print_exc() 
     
            
    elif opcion ==2:
       cliente = pedirdatosclientes()
       try:
           dao.crear_clientes(cliente)
       except:  
           print("ocurrio un error")     
    elif opcion ==3:
       cliente = pedirdatosclientes()
       try:
           dao.editaractualizar_cliente(cliente)
       except Exception as err:
            traceback.print_exc()
        
    elif opcion==1:
        try:
            clientes= dao.listar_clientes()
            if len(clientes)>0:
               codigoEliminar = pedir_clientes_eliminacion(clientes)
               if  not(codigoEliminar == ""):
                   dao.eliminar_clientes(codigoEliminar)
               else:
                   print("codigo de cliente no encontrado...\n")  
            else:
                print("no se encontraron clientes... ")        
        except Exception as err:
            traceback.print_exc()   
        else:print("opcion no valida")
    elif opcion == 5:
       
                menu_principal()
        


#empieza el nenu de ventas

def menu_ventas():
    continuar= True
    while(continuar):
        print("=== MENÚ VENTAS ===")
        print("1. Listar ventas")
        print("2. Crear ventas")
        print("3. eliminar venta")
        print("4. reportes por ventas")
        print("5. reportes por producto")
        print("6. Volver al Menú Principal")
        print("7. Salir")
        print("===")
        opcion_correcta= False
        while(True):
           
            opcion= int(input("seleccione una opcion por favor: "))
            #while menu_principal:
            
            if (opcion < 1 | opcion > 7):
                print("opcion ventas no valida por favor ingrese una opcion cliente correcta")
            elif opcion == 6:
                continuar = False
                print("gracias por usar este programa") 
                break  
            else:
                Ejecutaropcion(opcion)

def Ejecutaropcion(opcion):
    dao= DAOconsol()
    if opcion ==1:
        try:
            ventas= dao.listar_ventas()
            if len(ventas)>0:
                listar_ventas(ventas)
            else:
                print("no se encontro esa venta...")   
        except Exception as err:
            traceback.print_exc()

    elif opcion ==2:
       ventas = pedirdatosventas()
       try:
            dao.crear_ventas(ventas)
       except Exception as err:
            traceback.print_exc()     
    elif opcion == 3:
        try:
            ventas= dao.listar_ventas()
            if len(ventas)>0:
               ventaEliminar = pedir_ventas_eliminacion(ventas)
               if  not(ventaEliminar == ""):
                   dao.eliminar_ventas(ventaEliminar)
               else:
                   print("codigo de venta no encontrado...\n")  
            else:
                print("no se encontro tal venta... ")
        except Exception as err:
            traceback.print_exc()
               
    
    elif opcion == 4:
        codigo_cliente = input("Ingrese codigo cliente: ")
        ventas = dao.generar_reportes_por_cliente(codigo_cliente)
        generar_excel("Reporte ventas por cliente", ventas)
    elif opcion == 5:
        codigo_producto = input("Ingrese el codigo del producto: ")
        ventas = dao.generar_reportes_por_producto(codigo_producto)
        generar_excel("Reporte ventas por producto", ventas)
        
    elif opcion == 6:
        try:         
            menu_principal() 
        except Exception as err:
            traceback.print_exc()            
    else:print("opcion no valida")
        


menu_principal()    




