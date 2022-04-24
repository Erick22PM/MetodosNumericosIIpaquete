import numpy as np
import math as m

def MetodoPol(m, X1, Y1):
    while True:
        try:
            g = int(input("ingresa el grado del polinomio deseado"))
        except:
            print("Tiene que ser un valor numerico, prueba nuevamente...")
        else:
            if g < 1 or m < g:
                print("Tiene que tener grado mayor que cero y menor que el numero de datos, prueba nuevamente...")
            else:
                mtrx = np.zeros([g+1, g+1])
                vect = np.zeros([g+1])
                break

    for i in range(g+1):
        for j in range(g+1):
            if i==0 and j==0:
                mtrx[i][j] = m
            elif i==0:
                mtrx[i][j] = sum([pow(x,j+i) for x in X1])
            else:
                if j != g:
                    mtrx[i][j] = mtrx[i-1][j+1]
                else:
                    mtrx[i][j] = sum([pow(x, j+i) for x in X1])
        if i == 0:
            vect[i] = sum(Y1)
        else:
            vect[i] = sum(np.multiply([pow(x, i) for x in X1], Y1))

    if np.linalg.det(mtrx)!=0:
        res = np.matmul(np.linalg.inv(mtrx),vect)
        print("El polinomio resultado es el sigueinte:")
        a: int = 0
        for i in res:
            print(i, end="")
            print("(X^" + str(a) + ")")
            a += 1

        vX = np.zeros(len(X1))
        error: float = 0.0

        for j in range(len(X1)):
            for i in range(len(res)):
                vX[j] = res[i] * pow(X1[j], i) + vX[j]

        for i in range(m):
            error = pow(Y1[i]-vX[i], 2) + error

        print("Con un error de " + str(error))
    else:
        print("El determinante de la matriz es 0, debe cambiar los datos de entrada...")

    X1.clear()
    Y1.clear()

    return 0

def lectura_datos():#___________________________________________________________________________________________________
    m = 0
    Dat: list = []
    X1: list = []
    Y1: list = []
    aux = ""
    cond = """
El archivo tiene que tener la siguiente estructura:
- Datos ordenados de la forma:*Xi *Yi (separados por un espacio)
- salto de linea entre cada par de datos, incluido el ultimo par.
- Ejemplo: 
__________________________________
|1 23                            | *Espacio entre cada Xi Yi
|2 25                            | *Salto de line entre cada i
|3 47                            |
|                                | *Renglon final vacio
----------------------------------"""
    while True:
        op = int(input("""Deseas colocar los datos de la tabla mediante:"
Archivo ...................... ( 1 )
Ingresar por consola ......... ( 2 )"""))
      
        if op!=1 and op!=2:
            print("Tiene que ser 1 o 2, prueba nuevamente")
        else:
            break

    if op==1:
        while True:
          print(cond)
          nombreArchivo = input("\nColoque la ruta del archivo ('C:--\--\--\...\ nombre.txt') ")
          try:
              txt_file = open(nombreArchivo, "r")
          except:
              print("La ruta puesta no existe, prueba nuevamente")
          else:
              break

        # Lectura del numero de datos
        with open(nombreArchivo) as fp:
            for line in fp:
                if line.strip():
                    m += 1
                for character in line:
                    if character.isspace():
                        Dat.append(float(aux))
                        aux = ""
                    else:
                        aux += character
        print("numero de datos ", m)
        txt_file.close()  # se cierra el archivo

        for i in range(m * 2):
            if i % 2 == 0:
                X1.append(Dat[i])
            else:
                Y1.append(Dat[i])
    else:
        while True:
          m = int(input("Coloca el numero de datos"))
          if m < 0:
            print("Tiene que ser mayor que cero...")
          else:
            break

        for i in range(m):
            X1.append(float(input("Coloca el valor " + str(i + 1) + " de X:")))
            Y1.append(float(input("Coloca el valor " + str(i + 1) + " de Y:")))

    while True:
        print("Los datos obtenidos son los siguientes:")
        print("X: ", end="")
        print(X1)
        print("Y: ", end="")
        print(Y1)

        while True:
            resp = int(input("""Los datos son correctos?
            - NO ......... (0)
            - SI ......... (1)
            """))
            if resp != 0 and resp != 1:
                print("Debe seleccionar la opcion 1 o 2...")
            else:
                break

        if resp == 0:
            while True:
                iRen = int(input("Selecciona el i-esimo rengon a modificar (i empieza en 0):"))
                if iRen < 0:
                    print("Debe seleccionar un indice (0, 1, 2, ...")
                else:
                    break
            for i in range(m):
                if i == iRen:
                    X1[i] = float(input("Coloca el valor " + str(i) + " de X:"))
                    Y1[i] = float(input("Coloca el valor " + str(i) + " de Y:"))
        else:
            Dat.clear()
            break



    return m, X1, Y1
#_______________________________________________________________________________________________________________________

def menu_opciones():
    while True:
        m, X1, Y1 = lectura_datos()
        MetodoPol(m, X1, Y1)
        resp = input("¿Deseas trabajar con otra tabla (S/N)? ")
        if resp == "n" or resp == "N":
            print("Regresando al menú principal")
            break
