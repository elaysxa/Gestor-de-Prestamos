from utilidades import limpiar_pantalla, separador, generador_id_unico, pausar, validar_entero, validar_monto, pedir_datos
import persistencia as ps

def agregar_prestamo():
    limpiar_pantalla()
    separador()
    print('Agregar nuevo prestamo')
    separador()

    id = int(generador_id_unico())
    print('Identificador: ', id)

    nombre =  pedir_datos('Ingrese el nombre del prestatario: ').upper()
    
    monto = pedir_datos('Ingrese el monto del prestamo: ')
    #Verficar que monto sea un float

    monto = validar_monto(monto)
    fecha = pedir_datos('Ingrese la fecha del prestamo: ')
    separador()
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
    limpiar_pantalla()
    separador()
    print('COMPROBANTE DE PRESTAMO')
    separador()
    #Mostrar el prestamo creado
    mostrar_prestamo_info(id)
   

def modificar_prestamo():
    limpiar_pantalla()
    separador()
    print('MODIFICAR PRÉSTAMO')
    separador()
    print('1. Buscar por Id')
    print('2. Buscar por nombre')
    print('3. Regresar al menú principal')

    op = pedir_datos('Ingrese la opción deseada: ')
    op = validar_entero(op)
    limpiar_pantalla()

    if op == 1:
        id = pedir_datos('Ingrese el Id del prestatario: ')
        id = validar_entero(id)

        prestamo_encontrado = False
        for prestamo in ps.datos():
            if prestamo['Id'] == id:
                prestamo_encontrado = True
                separador()
                mostrar_prestamo_info(id)
                separador()

                print(f"Id: {prestamo['Id']}")
                nombre = input('Ingrese el nuevo nombre del prestatario (deje en blanco para mantener el actual): ').upper()
                if nombre:
                    prestamo['Nombre'] = nombre

                monto = input('Ingrese nuevo monto del préstamo (deje en blanco para mantener el actual): ')
                if monto:
                    monto = validar_monto(monto)
                    prestamo['Monto'] = monto

                fecha = input('Ingrese la nueva fecha del préstamo (deje en blanco para mantener la actual): ')
                if fecha:
                    prestamo['Fecha'] = fecha

                ps.modificar_prestamos(id, prestamo['Nombre'], prestamo['Monto'], prestamo['Fecha'])
                print('Préstamo modificado con éxito')
                pausar()
        
        if not prestamo_encontrado:
            print('No se encontró un préstamo con ese Id')
            pausar()

    elif op == 2:
        nombre = pedir_datos('Ingrese el nombre del prestatario: ').upper()

        prestamo_encontrado = False
        for prestamo in ps.datos():
            if prestamo['Nombre'] == nombre:
                prestamo_encontrado = True
                mostrar_prestamo_info(prestamo['Id'])
                separador()

                print(f"Id: {prestamo['Id']}")
                nuevo_nombre = input('Ingrese el nuevo nombre del prestatario (deje en blanco para mantener el actual): ').upper()
                if nuevo_nombre:
                    prestamo['Nombre'] = nuevo_nombre

                monto = input('Ingrese nuevo monto del préstamo (deje en blanco para mantener el actual): ')
                if monto:
                    monto = validar_monto(monto)
                    prestamo['Monto'] = monto

                fecha = input('Ingrese la nueva fecha del préstamo (deje en blanco para mantener la actual): ')
                if fecha:
                
                    prestamo['Fecha'] = fecha

                ps.modificar_prestamos(prestamo['Id'], prestamo['Nombre'], prestamo['Monto'], prestamo['Fecha'])
                print('Préstamo modificado con éxito')
                pausar()

        if not prestamo_encontrado:
            print('No se encontró un préstamo con ese nombre')
            pausar()

    elif op == 3:
        print('Regresando al menú principal')
        pausar()

    else:
        print('Opción inválida')
        pausar()
        
def mostrar_prestamo_info(id):
    for prestamo in ps.datos():
        if prestamo['Id'] == id:
            print(f"Prestamo ID: {prestamo['Id']}")
            print(f"A nombre de: {prestamo['Nombre']}")
            print(f"Por el monto de: {prestamo['Monto']}")
            print(f"En la fecha: {prestamo['Fecha']}")  
            separador()
            pausar()

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
            print(f"En la fecha: {prestamos['Fecha']}")  
            separador()
        pausar() 
    
def buscar_prestamo_id():
    limpiar_pantalla()
    separador()
    print('BUSCAR PRESTAMO POR ID')
    separador()
    id = pedir_datos('Ingrese el Id del prestamo: ')
    separador()
    id = validar_entero(id)
    prestamo_encontrado = False
    for prestamo in ps.datos():
        if prestamo['Id'] == id :
            prestamo_encontrado = True
            mostrar_prestamo_info(id)
    if not prestamo_encontrado:
        print('El prestamo no existe')
        pausar()

def buscar_prestamo_nombre():
    limpiar_pantalla()
    separador()
    print('BUSCAR PRESTAMO POR NOMBRE')
    separador()
    nombre = pedir_datos('Ingrese el nombre del prestatario: ').capitalize()
    prestamo_encontrado = False
    for prestamos in ps.datos():
        if prestamos['Nombre'] == nombre:
            prestamo_encontrado = True
            print(f"Prestamo ID: {prestamos['Id']}")
            print(f"A nombre de: {prestamos['Nombre']}")
            print(f"Por el monto de: {prestamos['Monto']}")
            print(f"En la fecha: {prestamos['Fecha']}")  
            separador()
            pausar() 

    if not prestamo_encontrado:
        print('Prestamo no encontrado ')
        pausar()
            
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