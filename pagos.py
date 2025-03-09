from utilidades import limpiar_pantalla, separador, pausar, validar_entero, validar_flotante, pedir_datos
import persistencia as ps
from gestion_prestamos import mostrar_prestamo_info
from datetime import datetime

def pagos():
    while True:
        limpiar_pantalla()
        separador()
        print('   💲 PAGOS    ')
        separador()
        print('1.➕ Registar pago')
        print('2.📖 Consultar pago')
        print('3.🗑️  Eliminar pago')
        print('4.📃 Informe de pagos')
        print('5.🔙 Regresar al menu principal')
        separador()
        op = pedir_datos('Ingrese la opcion deseada: ')
        op = validar_entero(op)

        match op:
            case 1: registrar_pago()
            case 2: consultar_pago()
            case 3: eliminar_pago()
            case 4: informe_pago()
            case 5:
                print('Regresando al menu principal')
                pausar()
                break
            case _:
                print('Opcion invalida')
def informe_pago():
    
    limpiar_pantalla()
    separador()
    print(' 📜 INFORME DE PAGOS')
    separador()
    id = pedir_datos('Ingrese el id del prestatario para ver informe de pagos : ')
    id = validar_entero(id)
    separador()
    for prestamo in ps.datos():
        if prestamo['Id'] == id:
            total_pagado = sum(p['Monto'] for p in prestamo.get('Pagos', []))
            saldo_pendiente = prestamo['Pago Total'] - total_pagado
            print (f"👤  Prestamo de:         {prestamo['Nombre']}")
            print(f"💲  Pagado:              {total_pagado:,.2f}")
            print(f"💰  Total a pagar:       {prestamo['Pago Total']:,.2f}")
            print(f"📉  Saldo pendiente      {saldo_pendiente:,.2f}")
            separador()
            pausar()
            if saldo_pendiente <=0:
                print(" ✅ Prestamo saldado completamente ")
                pausar()
    else:
        print('❌ Prestamo no encontrado ')


def comprobante_pago(id, pago):
    for prestamo in ps.datos ():
        if prestamo['Id'] == id:
            separador()
            print('     🧾 COMPROBANTE DE PAGO     ')
            separador()
            print(f"📅  Fecha:            {pago['Fecha']}")
            print(f"📆  Cuota No:         {pago['Cuota No']}")
            print(f"🆔  Prestamo ID:      {prestamo['Id']}")
            print(f"👤  Prestatario:      {prestamo['Nombre']}")
            print(f"💰  Pago realizado:   {pago['Monto']:,.2f}")
            print(f"🗓️  Cuotas Restantes: {prestamo['Cuotas'] - pago['Cuota No']}")
            separador()
            pausar()

def consultar_pago():
   limpiar_pantalla()
   separador()
   print('     📑 CONSULTAR PAGO')
   separador()
   id = pedir_datos(' 🆔 Ingrese el ID del prestamo: ')
   id = validar_entero(id)

   prestamo_encontrado = False
   for prestamo in ps.datos ():
        if prestamo['Id'] == id:
            prestamo_encontrado = True
            limpiar_pantalla()
            print(f"{'👤 Nombre:':>40}\t{prestamo["Nombre"]}")
            print(f"{'💲 Monto:':>40}\t{prestamo["Monto"]:,.2f}")
            print(f"{'📊 Interes:':>40}\t{prestamo["Interes"]}%")
            print('-'*65)
            print(f'\t\tLISTADO DE PAGOS')
            print('-'*65)
            print(f"{'Cuota No':<10}  {'Monto':<15}{'Fecha':<15} {'Pago Faltante':<15}")
            print('-'*65)
            if 'Pagos' not in prestamo or len(prestamo['Pagos']) == 0:
                print(' ❌ No hay pagos registrados para este prestamo')
                
            else:   
                for pago in prestamo['Pagos']:
                    print(f"   {pago['Cuota No']:<7}  {pago['Monto']:<15,.2f}{pago['Fecha']:<15} {pago['Pago Faltante']:<15,.2f}")
                    print('-'*65)
            pausar()
   if not prestamo_encontrado:
        print(' ❌ No se encontro un prestamo con ese ID')
        pausar()
                
def eliminar_pago():
     limpiar_pantalla()
     separador()
     print('     🗑️  ELIMINAR PAGO')
     separador()
     id = pedir_datos('🆔 Ingrese el ID del prestamo: ')
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
    print(' 💲 REGISTRAR PAGO ')
    separador()
    id = pedir_datos('Ingrese el ID del prestamo: ')
    id = validar_entero(id)
    
    
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
            monto = validar_flotante(monto)
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
         