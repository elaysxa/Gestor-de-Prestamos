from database.persistencia import cargar_datos
from views.interfaz import menu_principal


def main():
    cargar_datos()
    menu_principal()

if __name__ == "__main__":
    main()
