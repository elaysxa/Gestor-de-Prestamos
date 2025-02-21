import json

prestamos = []

def guardar_prestamo(prestamo):
    prestamos.append(prestamo)

def guardar_datos():
    with open('data/prestamos.json', 'w') as archivo:
        json.dump(prestamos, archivo, indent=4)

def cargar_datos():
    global prestamos
    try:
        with open("data/prestamos.json") as archivo:
            db = json.load(archivo)
    except FileNotFoundError:
        # Crear un archivo vacío si no existe
        guardar_datos()
