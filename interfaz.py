from utilidades import limpiar_pantalla, separador, validar_entero
from gestion_prestamos import agregar_prestamo, modificar_prestamo, consultar_prestamo, eliminar_prestamo, consultar_prestamo
from pagos import pagos

def menu_principal():
    while True:
        limpiar_pantalla()
        separador()
        print('     SISTEMA DE GESTION DE PRESTAMOS ')
        separador()
        print('1. Agregar prestamo')
        print('2. Modificar prestamo')
        print('3. Consultar prestamo')
        print('4. Eliminar prestamo')
        print('5. Registrar pago')
        separador()
        opcion = input('Ingrese la opcion deseada: ')
        # Verificar que op sea un numero
        op = validar_entero(opcion)
        match op:
            case 1:
                agregar_prestamo()
            case 2:
                modificar_prestamo()
            case 3:
                consultar_prestamo()
            case 4:
                eliminar_prestamo()
            case 5:
                pagos()
            case 6:
                print('Saliendo del sistema')
                break
            case _ :
                print('Opcion invalida')               