from utilidades import limpiar_pantalla, separador, pausar
from gestion_prestamos import agregar_prestamo, modificar_prestamo, consultar_prestamo, eliminar_prestamo, consultar_prestamo, buscar_prestamo_id, buscar_prestamo_nombre

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
        print('5. Salir')
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
                agregar_prestamo()
            case 2:
                modificar_prestamo()
            case 3:
                consultar_prestamo()
            case 4:
                eliminar_prestamo()
            case 5:
                print('Saliendo del programa')
                break                