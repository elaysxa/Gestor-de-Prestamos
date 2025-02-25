from utilidades import limpiar_pantalla, separador, generador_id_unico, pausar, validar_entero, validar_monto, pedir_datos, validar_fecha
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
    fecha = pedir_datos('Ingrese la fecha del prestamo (DD/MM/YYYY): ')
    fecha = validar_fecha(fecha)

    interes = pedir_datos('Ingrese el interes anual %: ')
    interes = validar_monto(interes)

    cuotas = pedir_datos('Ingrese el numero de cuotas mensuales: ')
    cuotas = validar_entero(cuotas)
    
    interes_mensual = (interes / 100)/12
    pago_cuotas = round((monto * interes_mensual)/ (1 - (1 + interes_mensual) ** -cuotas),2)
    pago_total = round(pago_cuotas * cuotas,2)

    separador()
    #Verificar si el Id de prestamo  ya existe
    while any(d['Id'] == id for d in ps.prestamos):
        id = int(generador_id_unico())
    
    #Agregar el prestamo al diccionario
    prestamo = {
        'Id': id,
        'Nombre': nombre,
        'Monto': monto,
        'Fecha': fecha,
        'Estado': 'ACTIVO',
        'Interes': interes,
        'Cuotas': cuotas,
        'Pago Mensual': pago_cuotas,
        'Pago Total': pago_total
    }
    #Guardarlos en el json
    ps.guardar_prestamo(prestamo)
    limpiar_pantalla()
    separador()
    print(' COMPROBANTE DE PRESTAMO ')
    separador()
    #Mostrar el prestamo creado
    mostrar_prestamo_info(id)
   
def modificar_prestamo():
   limpiar_pantalla()
   separador()
   print('  MODIFICAR PRESTAMO  ')
   separador()
   
   id = pedir_datos('Ingrese el Id del prestamo que desea modificar: ')
   id = validar_entero(id)
   separador()

   if id is None:
        pass    
   else:
        prestamo_encontrado = False
        for prestamo in ps.datos():
            if prestamo['Id'] == id:
                prestamo_encontrado = True
                mostrar_prestamo_info(id)
                limpiar_pantalla()
                separador()
                while True:
                    limpiar_pantalla()
                    separador()
                    print('    MODO EDICION    ')
                    separador()
                    print('1. Modificar el nombre del prestatario')
                    print('2. Modificar monto')
                    print('3. Modificar fecha')
                    print('4. Modificar estado')
                    print('5. Modifier interes')
                    print('6. Modificar cuotas')
                    print('7. Guardar y salir')
                    separador()
                    op = pedir_datos('Ingrese la opcion deseada: ')
                    separador()
                    op = validar_entero(op)
                    if op == 1:
                        nombre = pedir_datos(f'Ingrese el nuevo nombre ({prestamo['Nombre']}) : ').upper()
                        if nombre:
                            prestamo ['Nombre'] = nombre
                    if op ==2:
                        monto = pedir_datos(f'Ingrese el nuevo monto ({prestamo['Monto']}) : ')
                        monto = validar_monto(monto)
                        if monto:
                            prestamo ['Monto'] = monto        
                    if op == 3:
                        fecha = pedir_datos(f'Ingrese la nueva fecha ({prestamo['Fecha']}) : ')
                        fecha = validar_fecha(fecha)
                        if fecha:
                            prestamo ['Fecha'] = fecha  
                    if op == 4:
                        estado = pedir_datos(f'Ingrese el nuevo estado ({prestamo['Estado']}) : ').upper()
                        if estado:
                            prestamo ['Estado'] = estado 
                    if op == 5:
                        interes = pedir_datos('Ingrese el nuevo interes: ')
                        interes = validar_monto(interes)
                        if interes:
                            prestamo ['Interes'] = interes
                    if op == 6:
                        cuotas = pedir_datos('Ingrese el nuevo numero de cuotas: ')
                        cuotas = validar_entero(cuotas)
                        if cuotas:
                            prestamo ['Cuotas'] = cuotas
                    

                    interes_mensual = (prestamo['Interes'] / 100) / 12
                    pago_cuotas = round((prestamo['Monto'] * interes_mensual) / (1 - (1 + interes_mensual) ** -prestamo['Cuotas']), 2)
                    pago_total = round(pago_cuotas * prestamo['Cuotas'], 2)
                    prestamo['Pago Mensual'] = pago_cuotas
                    prestamo['Pago Total'] = pago_total

                    if op == 7:
                        
                        ps.modificar_prestamos(id, prestamo['Nombre'], prestamo['Monto'], prestamo['Fecha'], prestamo['Estado'], prestamo['Interes'], prestamo['Cuotas'], prestamo['Pago Total'])
                        mostrar_prestamo_info(id)
                        print('Prestamo guardado exitosamente ')
                        pausar()           
                        break
        if not prestamo_encontrado:
            print('Prestamo no encontrado')
            pausar()
                                       
def mostrar_prestamo_info(id):
    for prestamo in ps.datos():
        if prestamo['Id'] == id:
            print(f"Prestamo ID: {prestamo['Id']}")
            print(f"A nombre de: {prestamo['Nombre']}")
            print(f"Por el monto de: {prestamo['Monto']:,.2f}")
            print(f"En la fecha: {prestamo['Fecha']}") 
            print(f"Estado: {prestamo['Estado']}")
            print(f"Interes: {prestamo['Interes']}%")
            print(f"Cuotas: {prestamo['Cuotas']}")
            print(f"Pago mensual: {prestamo['Pago Mensual']:,.2f}")
            print(f"Pago Total: {prestamo['Pago Total']:,.2f}") 
            separador()
            pausar()

def eliminar_prestamo():
    limpiar_pantalla()
    separador()
    print(' ELIMINAR PRESTAMO   ')
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
            print(f"Interes: {prestamos['Interes']}%")
            print(f"Cuotas: {prestamos['Cuotas']:,.2f}")
            print(f"Pago Total: {prestamos['Pago Total']:,.2f}") 
            print(f"Estado: {prestamos['Estado']}") 
            separador()
        pausar() 
    
def buscar_prestamo_id():
    limpiar_pantalla()
    separador()
    print(' BUSCAR PRESTAMO POR ID  ')
    separador()
    id = pedir_datos('Ingrese el Id del prestamo: ')
    id = validar_entero(id)
    separador()

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
    print(' BUSCAR PRESTAMO POR NOMBRE  ')
    separador()
    nombre = pedir_datos('Ingrese el nombre del prestatario: ').upper()
    separador()
    prestamo_encontrado = False
    for prestamos in ps.datos():
        if prestamos['Nombre'] == nombre:
            prestamo_encontrado = True
            print(f"Prestamo ID: {prestamos['Id']}")
            print(f"A nombre de: {prestamos['Nombre']}")
            print(f"Por el monto de: {prestamos['Monto']}")
            print(f"En la fecha: {prestamos['Fecha']}") 
            print(f"Interes: {prestamos['Interes']}%")
            print(f"Cuotas: {prestamos['Cuotas']}")
            print(f"Pago Total: {prestamos['Pago Total']}") 
            print(f"Estado: {prestamos['Estado']}") 
            separador()
            pausar() 

    if not prestamo_encontrado:
        print('Prestamo no encontrado ')
        pausar()
            
def consultar_prestamo():
    while True:
        limpiar_pantalla()
        separador()
        print(' CONSULTAR PRESTAMOS ')  
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