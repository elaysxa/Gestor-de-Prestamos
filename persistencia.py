import json

prestamos = []

def datos():
    return prestamos

def guardar_prestamo(prestamo):
    prestamos.append(prestamo)
    guardar_datos()  # Guardar los datos después de agregar el nuevo préstamo
    return 'Prestamo agregado existosamente'

def guardar_datos():
    with open('data/prestamos.json', 'w') as archivo:
        json.dump(prestamos, archivo, indent=4)

def cargar_datos():
    global prestamos
    try:
        with open("data/prestamos.json", 'r') as archivo:
            prestamos = json.load(archivo)
    except FileNotFoundError:
        # Crear un archivo vacío si no existe
        guardar_datos()
    