from utils.utilidades import limpiar_pantalla, separador
from utils.validators import validar_entero
from models.gestion_prestamos import agregar_prestamo, modificar_prestamo, consultar_prestamo, eliminar_prestamo
from models.pagos import pagos

def menu_principal():
    while True:
        limpiar_pantalla()
        separador()
        print('     🪙  SISTEMA DE GESTION DE PRESTAMOS ')
        separador()
        print('1.➕  Agregar prestamo')
        print('2.🔁  Modificar prestamo')
        print('3.🔖  Consultar prestamo')
        print('4.🗑️  Eliminar prestamo')
        print('5.📠  Pagos ')
        print('6.🔚 Salir')
        separador()
        op = validar_entero('Ingrese la opcion deseada: ')
        
        
        match op:
            case 1: agregar_prestamo()
            case 2: modificar_prestamo()
            case 3: consultar_prestamo()
            case 4: eliminar_prestamo()
            case 5: pagos()
            case 6:
                print('Saliendo del sistema')
                break
            case _ :
                print('❌ Opcion invalida')               