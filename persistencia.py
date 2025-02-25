import json

prestamos = []

def datos():
    return prestamos

def guardar_prestamo(prestamo):
    prestamos.append(prestamo)
    guardar_datos()  
    return 'Prestamo agregado existosamente'

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

def guardar_datos():
    with open('data/prestamos.json', 'w' ,encoding='utf-8') as archivo:
        json.dump(prestamos, archivo, ensure_ascii=False, indent=4)

def cargar_datos():
    global prestamos
    try:
        with open("data/prestamos.json", 'r', encoding='utf-8') as archivo:
            prestamos = json.load(archivo)
    except FileNotFoundError:
        # Crear un archivo vacío si no existe
        guardar_datos()
    