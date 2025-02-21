from utilidades import limpiar_pantalla, separador, generador_id_unico, pausar
import persistencia as ps

def agregar_prestamo():

    limpiar_pantalla()
    separador()
    print('Agregar nuevo prestamo')
    separador()
    ide = generador_id_unico()
    id = print('Identificador: ', ide)
    nombre = input(('Ingrese el nombre del prestatario: '))
    monto = float(input('Ingrese el monto del prestamo: '))
    fecha = input(('Ingrese la fecha del prestamo: '))
    #Agregar el prestamo al diccionario
    prestamo = {
        'Id': ide,
        'Nombre': nombre,
        'Monto': monto,
        'Fecha': fecha
    }
    #Guardarlos en el json
    ps.guardar_prestamo(prestamo)
    ps.guardar_datos()
    print('Prestamo registrado con exito ') 
    pausar()

def modificar_prestamo():
    pass

def eliminar_prestamo():
    pass

def consultar_prestamo():
    pass

