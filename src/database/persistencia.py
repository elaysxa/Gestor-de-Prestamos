import json

prestamos = []


def datos():
    return prestamos

#Guardar los prestamos en la lista
def guardar_prestamo(prestamo):
    prestamos.append(prestamo)
    guardar_datos()  
    return 'Prestamo agregado existosamente'

#Guardar las modificaciones de los prestamos
def modificar_prestamos(id, nombre, monto, fecha, estado, interes, cuotas, pago_total):
    for prestamo in prestamos:
        if prestamo['Id'] == id:
            prestamo['Nombre'] = nombre
            prestamo['Monto'] = monto
            prestamo['Fecha'] = fecha
            prestamo['Estado'] = estado
            prestamo['Interes'] = interes
            prestamo['Cuotas'] = cuotas
            prestamo['Pago Total'] = pago_total
            guardar_datos()
    return '     PRESTAMO MODIFICADO EXITOSAMENTE     '

def guardar_datos():
    try:
        with open('src/database/prestamos.json', 'w' ,encoding='utf-8') as archivo:
            json.dump(prestamos, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f'Error al guardar los datos{e}')
        
def cargar_datos():
    global prestamos
    try:
        with open("src/database/prestamos.json", 'r', encoding='utf-8') as archivo:
            prestamos = json.load(archivo)
    except FileNotFoundError:
        # Crear un archivo vacío si no existe
        guardar_datos()
    