from utilidades import limpiar_pantalla, separador, generador_id_unico, pausar, validar_entero, validar_monto, pedir_datos
import persistencia as ps

def agregar_prestamo():
    limpiar_pantalla()
    separador()
    print('Agregar nuevo prestamo')
    separador()

    id = int(generador_id_unico())
    print('Identificador: ', id)

    nombre = pedir_datos('Ingrese el nombre del prestatario: ')
    monto = pedir_datos('Ingrese el monto del prestamo: ')
    #Verficar que monto sea un float
    Monto = validar_monto(monto)
    fecha = pedir_datos('Ingrese la fecha del prestamo: ')
   

    #Verificar si el Id de prestamo  ya existe
    while any(d['Id'] == id for d in ps.prestamos):
        id = int(generador_id_unico())

    #Agregar el prestamo al diccionario
    prestamo = {
        'Id': id,
        'Nombre': nombre,
        'Monto': Monto,
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

    identificador = pedir_datos('Ingrese el Identificados del prestamos a eliminar: ')
    
    #Validar que el id ingresado es un numero
    id = validar_entero(identificador)
    
    if id is None:
        pass
    else:
        prestamo_encontrado = False
        for prestamo in ps.datos():
            if prestamo['Id'] == id:
                prestamo_encontrado = True
                confirmacion = input(f"Esta seguro de que quiere borrar el prestamo con el identificador {prestamo['Id']} Presione (S) para confirmar: ")
                if confirmacion.lower() == 's':
                    ps.datos().remove(prestamo)
                    separador()
                    print('Prestamo eliminado con exito')
                    separador()
                else:
                    print('Eliminacion cancelada')
                    pausar()
                    break
        if not prestamo_encontrado:
            print('No existe ningun prestamo con este identificador')
            pausar()

    ps.guardar_datos()

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

        opcion = pedir_datos('Ingrese la opcion deseada: ')
        # Verificar que op sea un numero
        op = validar_entero(opcion)
        
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
            case _ :
                print('Opcion invalida') 