import os
import random
import string
from datetime import datetime
import persistencia as ps
import re


def limpiar_pantalla():
    os.system('cls')

def separador():
    print('-'*50)

def pausar():
    input('Presione una tecla para continuar ')

def generador_id_unico():
    #Genera una cadena de string con numeros de 5 digitos
    caracteres =  string.digits
    id = ''.join(random.choice(caracteres) 
        for _ in range(5))
    if not any (d['Id'] == id for d in ps.prestamos):
        return id

#Validar que la entrada sea un numero entero
def validar_entero(entero):
    try:
        num = int(entero)
        return num
    except ValueError:
        print("Entrada invalida: Ingrese un numero ")
        pausar()
    return None

#Validar que la entrada sea un numero flotante
def validar_monto(monto):
    while True:
        try:
            num = float(monto)            
            return num
        except ValueError:
            print("Entrada invalida: Ingrese un valor numerico")  
            pausar()
            separador()
            monto = pedir_datos('Ingrese el monto nuevamente: ')


#Validar que la entrada no este vacia
def pedir_datos(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.strip():
            return entrada
        else:
            print("La entrada no puede estar vacia, intentelo nuevamente")

#Validar que la fecha sea valida       
def validar_fecha(fecha):
    while True:
        try:
            fecha = datetime.strptime(fecha, '%d/%m/%Y').strftime('%d/%m/%Y')
            return str(fecha)
        except ValueError:
            print("Entrada invalida: Ingrese una fecha valida (dd/mm/yyyy)")
            separador()
            fecha = pedir_datos("Ingrese la fecha nuevamente: ")

def validar_letras(mensaje):
    while True:
        entrada = input(mensaje)
        if re.match(r"^[a-zA-Z\s]+$", entrada):
            return entrada
        else:
            print('❌  Entrada invalida: Ingrese solo letras y espacios')


