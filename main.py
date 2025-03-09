from interfaz import menu_principal
import persistencia as ps

def main():
    ps.cargar_datos()
    menu_principal()

if __name__ == "__main__":
    main()
