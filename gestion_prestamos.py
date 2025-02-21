from utilidades import limpiar_pantalla, separador, generador_id_unico, pausar
import persistencia as ps

def agregar_prestamo():
    limpiar_pantalla()
    separador()
    print('Agregar nuevo prestamo')
    separador()

    
    id = int(generador_id_unico())
    print('Identificador: ', id)
    nombre = input(('Ingrese el nombre del prestatario: '))
    monto = float(input('Ingrese el monto del prestamo: '))
    fecha = input(('Ingrese la fecha del prestamo: '))

    #Verificar si el Id de prestamo  ya existe
    while any(d['Id'] == id for d in ps.prestamos):
        id = int(generador_id_unico())

    #Agregar el prestamo al diccionario
    prestamo = {
        'Id': id,
        'Nombre': nombre,
        'Monto': monto,
        'Fecha': fecha
    }
    #Guardarlos en el json
    ps.guardar_prestamo(prestamo)
    pausar()

def modificar_prestamo():
    pass

def eliminar_prestamo():
    pass

def consultar_prestamo():
    pass

