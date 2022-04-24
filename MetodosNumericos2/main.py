import Option1 as op1
import Option2 as op2
import Option3 as op3

def main():
    print("""Programa 1
Por:
- García Moreno Aldo
- Jarquin Garcia Salvador
- Palomares Olegario Alexis
- Perez Mendoza Erick""")
    opciones_menu = """Selecciona la opción que quieras ver:
    1)  Sistemas resueltos por el método de Newton

    2)  Interpolación polinomial por el método de Newton

    3)  Minimos cuadrados polinomiales
    
    4)  Salir
    """
    cont = ""
    while True:
        resp = 0
        while 4 < resp or resp < 1:
            resp = int(input(opciones_menu))
            if 4 < resp or resp < 1:
                print("Opción fuera de rango")
        if resp == 1:
            op1.menu_opciones()
        elif resp == 2:
            op2.menu_opciones()
        elif resp == 3:
            op3.menu_opciones()
        else:
            print("Adiós :)")
            break
        cont = input("¿Deseas continuar en el programa (S/N)?    ")
        if cont == "n" or cont == "N":
            print("Adiós :)")
            break
        

if __name__ == "__main__":
    main()