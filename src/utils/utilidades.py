import os
import random
import string
from datetime import datetime
from database.persistencia import prestamos



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
    if not any (d['Id'] == id for d in prestamos):
        return id

