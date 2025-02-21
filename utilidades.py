import os
import random
import string


def limpiar_pantalla():
    os.system('cls')

def separador():
    print('-'*40)

def pausar():
    input('Presione una tecla para continuar ')

def generador_id_unico():
    #Genera una cadena de string con numeros de 5 digitos
    caracteres =  string.digits
    id = ''.join(random.choice(caracteres) for i in range(5))
    return id

def validar_datos():
    pass