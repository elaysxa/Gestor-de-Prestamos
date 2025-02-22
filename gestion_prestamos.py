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
    limpiar_pantalla()
    separador()
    print('ELIMINAR PRESTAMO')
    separador()

def listar_prestamos():
    limpiar_pantalla()
    separador()
    print('Todos los prestamos')
    separador()
    if len(ps.datos()) == 0:
        print('No hay prestamos')
    else:
        for prestamos in ps.datos():
            print(f"Prestamo ID: {prestamos['Id']}")
            print(f"A nombre de: {prestamos['Nombre']}")
            print(f"Por el monto de: {prestamos['Monto']}")
            print(f"Hasta la fecha de: {prestamos['Fecha']}")  
            separador()
        pausar() 

def buscar_prestamo_id():
    print('ID')

def buscar_prestamo_nombre():
    print('nombre')

def consultar_prestamo():
    while True:
        limpiar_pantalla()
        separador()
        print('CONSULTAR PRESTAMOS')  
        separador()
        print('1. Mostrar todos los prestamos')
        print('2. Buscar prestamo por identificador')
        print('3. Buscar prestamo por por nombre')
        print('4. Regresar al menu principal')
        separador()
    # Verificar que op sea un numero
        try:
            op = int(input('Ingrese la opcion deseada: '))
        except ValueError:
            print("Entrada invalida")  
            pausar()
            continue  
        
        match op:
            case 1:
                listar_prestamos()
            case 2:
                buscar_prestamo_id()
            case 3:
                buscar_prestamo_nombre()
            case 4:
                print('Regresando al menu principal')
                pausar()
                break