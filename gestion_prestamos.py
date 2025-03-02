from utilidades import limpiar_pantalla, separador, generador_id_unico, pausar, validar_entero, validar_monto, pedir_datos, validar_fecha
import persistencia as ps
from datetime import datetime

def agregar_prestamo():
    limpiar_pantalla()
    separador()
    print(' AGREGAR PRESTAMO  ')
    separador()

    id = int(generador_id_unico())
    print('Identificador: ', id)

    nombre =  pedir_datos('Ingrese el nombre del prestatario: ').upper()
    
    monto = pedir_datos('Ingrese el monto del prestamo: ')
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
    print('     COMPROBANTE DE PRESTAMO      ')
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
                    print('5. Modificar interes')
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
                        monto = pedir_datos(f'Ingrese el nuevo monto ({prestamo['Monto']:,.2f}) : ')
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
                        interes = pedir_datos(f'Ingrese el nuevo interes ({prestamo['Interes']}%): ')
                        interes = validar_monto(interes)
                        if interes:
                            prestamo ['Interes'] = interes
                    if op == 6:
                        cuotas = pedir_datos(f'Ingrese el nuevo numero de cuotas ({prestamo['Cuotas']}): ')
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
                        limpiar_pantalla()
                        separador()
                        print('     PRESTAMO MODIFICADO EXITOSAMENTE     ')
                        separador()
                        mostrar_prestamo_info(id)
                        break
        if not prestamo_encontrado:
            print('Prestamo no encontrado')
            pausar()
                                       
def mostrar_prestamo_info(id):
    for prestamo in ps.datos():
        if prestamo['Id'] == id:
            print(f" 🆔 Préstamo ID:    {prestamo['Id']}")
            print(f" 👤 A nombre de:    {prestamo['Nombre']}")
            print(f" 💰 Monto:          RD$ {prestamo['Monto']:,.2f}")
            print(f" 📅 Fecha:          {prestamo['Fecha']}")
            print(f" 🔖 Estado:         {prestamo['Estado']}")
            print(f" 📊 Interés:        {prestamo['Interes']}%")
            print(f" 📆 Cuotas:         {prestamo['Cuotas']}")
            print(f" 💳 Pago mensual:   RD$ {prestamo['Pago Mensual']:,.2f}")
            print(f" 💵 Pago Total:     RD$ {prestamo['Pago Total']:,.2f}")
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
    print("     LISTA DE PRESTAMOS      ")
    separador()
    for prestamo in ps.datos():
            print(f" 🆔 Préstamo ID:    {prestamo['Id']}")
            print(f" 👤 A nombre de:    {prestamo['Nombre']}")
            print(f" 💰 Monto:          RD$ {prestamo['Monto']:,.2f}")
            print(f" 📅 Fecha:          {prestamo['Fecha']}")
            print(f" 🔖 Estado:         {prestamo['Estado']}")
            print(f" 📊 Interés:        {prestamo['Interes']}%")
            print(f" 📆 Cuotas:         {prestamo['Cuotas']}")
            print(f" 💳 Pago mensual:   RD$ {prestamo['Pago Mensual']:,.2f}")
            print(f" 💵 Pago Total:     RD$ {prestamo['Pago Total']:,.2f}")
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
    for prestamo in ps.datos():
        if prestamo['Nombre'] == nombre:
            prestamo_encontrado = True
            print(f" 🆔 Préstamo ID:    {prestamo['Id']}")
            print(f" 👤 A nombre de:    {prestamo['Nombre']}")
            print(f" 💰 Monto:          RD$ {prestamo['Monto']:,.2f}")
            print(f" 📅 Fecha:          {prestamo['Fecha']}")
            print(f" 🔖 Estado:         {prestamo['Estado']}")
            print(f" 📊 Interés:        {prestamo['Interes']}%")
            print(f" 📆 Cuotas:         {prestamo['Cuotas']}")
            print(f" 💳 Pago mensual:   RD$ {prestamo['Pago Mensual']:,.2f}")
            print(f" 💵 Pago Total:     RD$ {prestamo['Pago Total']:,.2f}")
            separador()
    pausar() 

    if not prestamo_encontrado:
        print('Prestamo no encontrado ')
        pausar()


def pagos():
    while True:
        limpiar_pantalla()
        separador()
        print('   REGISTRAR PAGO    ')
        separador()
        print('1. Registar pago')
        print('2. Consultar pago')
        print('3. Eliminar pago')
        print('4. Regresar al menu principal')
        separador()
        op = pedir_datos('Ingrese la opcion deseada: ')
        op = validar_entero(op)

        match op:
            case 1:
                registrar_pago()
            case 2:
                consultar_pago()
            case 3:
                eliminar_pago()
            case 4:
                print('Regresando al menu principal')
                pausar()
                break
            case _:
                print('Opcion invalida')

def comprobante_pago(id, pago):
    for prestamo in ps.datos ():
        if prestamo['Id'] == id:
            separador()
            print('     COMPROBANTE DE PAGO     ')
            separador()
            print(f"📅 Fecha:           {pago['Fecha']}")
            print(f"📆 Cuota No:         {pago['Cuota No']}")
            print(f"🆔 Prestamo ID:      {prestamo['Id']}")
            print(f"👤 Prestatario:      {prestamo['Nombre']}")
            print(f"💰 Pago realizado:   {pago['Monto']:,.2f}")
            print(f"🗓️ Cuotas Restantes: {prestamo['Cuotas'] - pago['Cuota No']}")
            separador()
            pausar()
    for prestamo in ps.datos ():
        if prestamo['Id'] == id:
            separador()

def consultar_pago():
   limpiar_pantalla()
   separador()
   print('     CONSULTAR PAGO')
   separador()
   id = pedir_datos('Ingrese el ID del prestamo: ')
   id = validar_entero(id)
   for prestamo in ps.datos ():
        if prestamo['Id'] == id:
            limpiar_pantalla()
            print(f"{'👤 Nombre:':>35}\t{prestamo["Nombre"]}")
            print(f"{'💰 Monto:':>35}\t{prestamo["Monto"]:,.2f}")
            print(f"{'📊 Interes:':>35}\t{prestamo["Interes"]}%")
            print('-'*65)
            print(f'\t\tLISTADO DE PAGOS')
            print('-'*65)
            print(f"{'Cuota No':<10}  {'Monto':<15}{'Fecha':<15} {'Pago Faltante':<15}")
            print('-'*65)
            for pago in prestamo['Pagos']:
                print(f"   {pago['Cuota No']:<7}  {pago['Monto']:<15,.2f}{pago['Fecha']:<15} {pago['Pago Faltante']:<15,.2f}")
            print('-'*65)
            pausar()
def eliminar_pago():
     limpiar_pantalla()
     separador()
     print('     ELIMINAR PAGO')
     separador()
     id = pedir_datos('Ingrese el ID del prestamo: ')
     id = validar_entero(id)
     limpiar_pantalla()
     for prestamo in ps.datos():
        if prestamo['Id'] == id:
            if 'Pagos' in prestamo:
                separador()
                print(f"👤 Prestatario:     {prestamo['Nombre']}")
                print(f"💰 Monto:           {prestamo['Monto']:,.2f}")
                print(f"📊 Interes:         {prestamo['Interes']}%")
                print(f"📆 Cuotas:          {prestamo['Cuotas']}")
                separador()
                print('     LISTA DE PAGOS     ')   
                separador()
                for i, pago in enumerate (prestamo['Pagos']):  
                    print(f" {i +1 }. Fecha: {pago['Fecha']}, Monto: {pago['Monto']:,.2f}")
                separador()

                indice = pedir_datos('Ingrese el numero del pago que desea eliminar: ')
                indice = validar_entero(indice)
                
                if indice is None:
                    pass
                else:
                    if 0 < indice <= len(prestamo['Pagos']):
                        pago = prestamo['Pagos'][indice - 1]
                        confirmacion = input(f"Esta seguro de que quiere borrar este pago de {pago['Monto']:,.2f}? (S/N): ")
                        if confirmacion.lower() == 's': 
                            monto = pago['Monto']
                            prestamo['Pagos']
                            #Restar el monto del pago eliminado al Pago Faltante

                            prestamo['Pago']['Pago Faltante'] = round(prestamo['Pago']['Pago Faltante'] + monto, 2)
                            #prestamo['Pago Total'] = round(prestamo['Pago Total'] + monto, 2)
                            prestamo['Pagos'].pop(indice - 1)
                            prestamo['Estado'] = 'ACTIVO'
                            ps.guardar_datos()
                            separador()
                            print(f' ✅ Pago de {monto:,.2f} eliminado con exito. Nuevo saldo: {prestamo["Pago Total"]:,.2f}')
                            separador()
                            mostrar_prestamo_info(id)
                            break
                        else:
                            print(' ❌ Eliminacion cancelada')
                            pausar()
                            break
                    else:
                        print(' ⚠️ Indice invalido')
                        pausar()

            else:
                print('No hay pagos registrados para este prestamo')

def registrar_pago():
    limpiar_pantalla()
    separador()
    print(' REGISTRAR PAGO ')
    separador()
    id = pedir_datos('Ingrese el ID del prestamo: ')
    id = validar_entero(id)
    
    """Registra un pago para un préstamo existente y actualiza el saldo pendiente."""
    prestamo_encontrado = False
    for prestamo in ps.datos():
        #Crear la lista de pagos

        if prestamo['Id'] == id:
            prestamo_encontrado = True
            if 'Pagos' not in prestamo:
                prestamo['Pagos'] = []

            separador()
            mostrar_prestamo_info(id)
            separador()

            monto = input(f"Ingrese el monto del pago ({prestamo['Pago Mensual']:,.2f}): ")
            monto = validar_monto(monto)
            separador()
            #Sumar todos los pagos realizados

            total_pagado = sum(p['Monto'] for p in prestamo['Pagos'])
            pago_faltante = round(prestamo['Pago Total'] - total_pagado - monto, 2)
            #Agregar el pago a la lista de pagos
            pago = {
                'Cuota No': len(prestamo['Pagos']) + 1,
                'Monto': monto,
                'Fecha': datetime.now().strftime('%d/%m/%Y'),
                #Pago faltante es igual al pago total menos el monto del pago faltante
                'Pago Faltante': pago_faltante
            }
            prestamo['Pagos'].append(pago)
            
            if pago_faltante <= 0:
                prestamo['Estado'] = 'PAGADO'

            ps.guardar_datos()
            limpiar_pantalla()
            print(f"✅ Pago de {monto:,.2f} registrado. Saldo restante: {pago['Pago Faltante']:,.2f}")
            comprobante_pago(id, pago) 
    
    if not prestamo_encontrado:
        print('⚠️  No se encontró un préstamo con ese ID')
        pausar()
         
def consultar_prestamo():
    while True:
        limpiar_pantalla()
        separador()
        print(' CONSULTAR PRESTAMOS ')  
        separador()
        print('1. Mostrar todos los prestamos')
        print('2. Buscar prestamo por identificador')
        print('3. Buscar prestamo por nombre')
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