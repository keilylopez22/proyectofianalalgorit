#funciones para clientes
import BD.conexionconsol 
from BD.conexionconsol import DAOconsol



def listar_cliente(clientes):
    print("\nCLIENTES: \n")
    contador= 1
    for client in clientes:
        datos = "{0}. CODIGO_CLIENTE: {1} | NOMBRE_CLIENTE: {2}  |DIRECCION: {3} |TELEFONO: {4} ({5} CORREO)"
        print(datos.format(contador, client[0], client[1], client[2], client[3], client[4]))
        contador= contador+1
        print(" ")

#esta funcion es la que nos va a guardar los datos de los clientes que creermos
def pedirdatosclientes():
       #codigo_correcto= False
       #while(not codigo_correcto):
    codigo_cliente= int(input("ingrese el codigo: "))
          #if len(codigo_producto) <=6:
           # codigo_correcto= True
          #else:
              # print("codigo incorrecto: el codigo no debe ser mayor a 6 digitos")    
    nombre_cliente= input("ingrese el nombre del cliente: ")
    direccion = input("ingrese la direccion del cliente: ")
    telefono= input("ingrese el telefono del cliente: ")
    correo= input("ingrese el correo electronico del cliente: ")
       
    clientes=(codigo_cliente, nombre_cliente, direccion, telefono, correo)
    return clientes


def pedirdatosclientes(clientes):
    listar_cliente(clientes)
    codigoclientecExiste= False
    codigoEditar= input("ingrese el codigo del cliente que deseaa editar: ")
     
    for cliente in clientes:
        if (str (cliente[0]) == codigoEditar):
            codigoclienteExiste= True
            break
    if codigoclienteExiste:
        codigoEditar= int(input("ingrese el codigo: "))
        nombre_clientes= input("ingrese el nombre del clientes: ")
        direccion= input("ingrese el direccion del clientes: ")
        telefono= input("ingrese el telefono del clientes: ")
        correo= input("ingrese el correo del clientes: ")

        clientes=(codigoEditar, nombre_clientes, direccion, telefono, correo)
    else:
        clientes = None
        return clientes

def pedir_clientes_eliminacion(clientes):
     listar_cliente(clientes)
     codigoclienteExiste= False
     codigoEliminar= input("ingrese el codigo del cliente que deseaa eliminar: ")
     
     for cliente in clientes:
          

          if (str (cliente[0]) == codigoEliminar):
               codigoclienteExiste= True
               break
     if not codigoclienteExiste:
          codigoEliminar= ""   
     return codigoEliminar

