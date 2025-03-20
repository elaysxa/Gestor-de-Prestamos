from datetime import datetime
import re
from utils.utilidades import separador
#Validar que la entrada sea un numero entero
def validar_entero(mensaje):
    while True:
        entero = input(mensaje)
        try:
            num = int(entero)
            return num
        except ValueError:
            print("❌ Entrada invalida: Ingrese un numero ")
           

#Validar que la entrada sea un numero flotante
def validar_flotante(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            num = float(entrada)            
            return num
        except ValueError:
            print(" ❌ Entrada invalida: Ingrese un valor numerico")  
            
#Validar que la fecha sea valida       
def validar_fecha(mensaje):
    while True:
        fecha = input(mensaje)
        try:
            fecha = datetime.strptime(fecha, '%d/%m/%Y').strftime('%d/%m/%Y')
            return str(fecha)
        except ValueError:
            print("❌  Entrada invalida: Ingrese una fecha valida (dd/mm/yyyy)")
            separador()

#Validar que la entrada sea solo de letras 
def validar_letras(mensaje):
    while True:
        entrada = input(mensaje)
        if re.match(r"^[a-zA-Z\s]+$", entrada):
            return entrada
        else:
            print('❌  Entrada invalida: Ingrese solo letras y espacios')
            separador


