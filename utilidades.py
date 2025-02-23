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
    id = ''.join(random.choice(caracteres) for _ in range(5))
    return id

def validar_entero(entero):
    try:
        num = int(entero)
        return num
    except ValueError:
        print("Entrada invalida: Ingrese un numero: ")
        pausar()
    return None

def validar_monto(monto):
    try:
        num = float(monto)
        return num
    except ValueError:
        print("Entrada invalida: Ingrese un valor numerico")  
        pausar()
#Validar que las entradas no esten vacias

def pedir_datos(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.strip():
            return entrada
        else:
            print("La entrada no puede estar vacia, intentelo nuevamente")
        
            
        
