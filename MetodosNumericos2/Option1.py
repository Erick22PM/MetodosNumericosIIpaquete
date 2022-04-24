import numpy as np
import math as m
from tabulate import tabulate

# serie de cadenas que van a ser reutilizadas en el código
singularidad = "No se pudo sacar raíces porque la jacobiana es singular"
valor_x = "Valor inicial de x:  "
valor_y = "Valor inicial de y:  "
valor_z = "Valor inicial de z:  "
valor_lim = "Límite de iteraciones:  "
valor_tol = "Tolerancia del error:  "
reusar_sistema = "¿Deseas volver a trabajar con este sistema (S/N)?   "
repeticion = ""
sistemas = """Selecciona el sistema que deseas usar:

1)  f1(x,y)=x^2+2x-10=0
    f2(x,y)=y+3xy^2-50=0

2)  f1(x,y)=x^2+y^2-9=0
    fx(x,y)=-e^x-2y-3=0
    
3)  f1(x,y,z)=2x^2-4x+y^2+3z^2+6z+2=0
    f2(x,y,z)=x^2+y^2-2y+2z^2-5=0
    f3(x,y,z)=3x^2-12x+y^2-3z^2+8=0
    
4)  f1(x,y,z)=x^2-4x+y^2=0
    f2(x,y,z)=x^2-x-12y+1=0
    f3(x,y,z)=3x^2-12x+y^2-3z^2+8=0

5)  Salir
"""

def sistema1 (x0, y0, lim, tol):
    """Función de resolución del sistema 1"""
    
    # inicializamos el contador y el Ea,
    i = 0
    erabs = 100
    # creamos un vector de numpy para usar el módulo
    X0 = np.array([x0,y0])
    # bandera para el determinante de la matriz
    det = False
    # guardaremos los datos en lista resultados
    resultados = []
    # ciclo para realizar la iteración
    while i < lim and erabs > tol:
        i += 1
        # creamos el vector FXi
        FX0 = np.array([x0**2+x0*y0-10, y0+3*x0*y0**2-50])
        # creamos la matriz Ji
        J0 = np.array([[ 2*x0+y0 , x0 ],[ 3*y0**2 , 1+6*x0*y0 ]])
        # comprobación de matriz no singular
        if np.linalg.det(J0) != 0:
            # obtenemos el nuevo vector a partir del anterior
            X1 = X0 - np.dot(np.linalg.inv(J0),FX0)
            # calculamos el error absoluto
            erabs = max( abs(X1[0]-X0[0]), abs(X1[1]-X0[1]))
            # agregamos los resultados de la iteración a 'resultados'
            resultados.append([i, X1, FX0, erabs])
            # cambiamos los valores de Xi por los nuevos
            X0 = X1
            x0 = X1[0]
            y0 = X1[1]
        else:
            det=True
    print(tabulate(resultados, headers=["it","Xi","FXi","Ea"]))
    # si la matriz es singular
    if det:
        print(singularidad)
    # si se alcanzó la tolerancia
    elif erabs < tol:
        print(f"Se encontró la raíz {X1} en la iteración {i} con un error de {erabs}")
    else:
        print(f"No se alcanzó la tolerancia en las iteraciones indicadas, se encontró la raíz {X1}")

def sistema2 (x0, y0, lim, tol):
    """Función de resolución del sistema 2"""
    
    # inicializamos el contador y el Ea,
    i = 0
    erabs = 100
    # creamos un vectorde numpy para usar el módulo
    X0 = np.array([x0,y0])
    # bandera para el determinante de la matriz
    det = False
    # guardaremos los datos en lista 'resultados'
    resultados = []
    # ciclo para iterar
    while i < lim and erabs > tol:
        i += 1
        # creamos el vector FXi
        FX0 = np.array([x0**2+y0**2-9, -3-m.exp(x0)-2*y0])
        # creamos la matriz Ji
        J0 = np.array([[ 2*x0 , 2*y0 ],[ -m.exp(x0) , -2 ]])
        # comprobación de no singularidad
        if np.linalg.det(J0) != 0:
            # obtenemos el nuevo vector a partir del anterior
            X1 = X0 - np.dot(np.linalg.inv(J0),FX0)
            # calculamos el error absoluto
            erabs = max( abs(X1[0]-X0[0]), abs(X1[1]-X0[1]))
            # agregamos los resultados de la iteración a 'resultados'
            resultados.append([i, X1, FX0, erabs])
            # cambiamos los valores de Xi por los nuevos
            X0 = X1
            x0 = X1[0]
            y0 = X1[1]
        else:
            det = True
    print(tabulate(resultados, headers=["it","Xi","FXi","Ea"]))
    # si es singular
    if det:
        print(singularidad)
    # si se alcanzó la tolerancia
    elif erabs < tol:
        print(f"Se encontró la raíz {X1} en la iteración {i} con un error de {erabs}")
    else:
        print(f"No se alcanzó la tolerancia en las iteraciones indicadas, se encontró la raíz {X1}")

def sistema3 (x0, y0, z0, lim, tol):
    """Función de resolución de sistema 3"""
  
    # inicializamos el contador y el Ea,
    i = 0
    erabs = 100
    # creamos un vector numpy para usar el módulo
    X0 = np.array([x0,y0,z0])
    # bandera para el determinante de la matriz
    det = False
    # guardaremos los datos en lista 'resultados'
    resultados = []
    # ciclo para iterar
    while i < lim and erabs > tol:
        i += 1
        # creamos el vector FXi
        FX0 = np.array([2*x0**2-4*x0+y0**2+3*z0**2+6*z0+2,
            x0**2+y0**2-2*y0+2*z0**2-5,
            3*x0**2-12*x0+y0**2-3*z0**2+8])
        # creamos la matriz Ji
        J0 = np.array([[ 4*x0-4 , 2*y0 , 6*z0+6 ],
            [ 2*x0 , 2*y0-2 , 4*z0 ],
            [ 6*x0-12 , 2*y0 , -6*z0]])
        # comprobación no singularidad
        if np.linalg.det(J0) != 0:
            # obtenemos el nuevo vector a partir del anterior
            X1 = X0 - np.dot(np.linalg.inv(J0),FX0)
            # calculamos el error absoluto
            erabs = max( abs(X1[0]-X0[0]), abs(X1[1]-X0[1]))
            # agregamos los resultados de la iteración a "resultados"
            resultados.append([i, X1, FX0, erabs])
            # cambiamos los valores de Xi por los nuevos
            X0 = X1
            x0 = X1[0]
            y0 = X1[1]
            z0 = X1[2]
        else:
            det = True
    print(tabulate(resultados, headers=["it","Xi","FXi","Ea"]))
    # si es singular
    if det:
        print(singularidad)
    # si se alcanzó la tolerancia
    elif erabs < tol:
        print(f"Se encontró la raíz {X1} en la iteración {i} con un error de {erabs}")
    else:
        print(f"No se alcanzó la tolerancia en las iteraciones indicadas, se encontró la raíz {X1}")

def sistema4 (x0, y0, z0, lim, tol):
    """Función resolución de sistema 4"""
  
    # inicializamos el contador y el Ea,
    i = 0
    erabs = 100
    # creamos un vector numpy para usar el módulo
    X0 = np.array([x0,y0,z0])
    # bandera para el determinante de la matriz
    det = False
    # guardaremos los datos en lista 'resultados'
    resultados = []
    # ciclo para iterar
    while i < lim and erabs > tol:
        i += 1
        # creamos el vector FXi
        FX0 = np.array([x0**2-4*x0+y0**2,
            x0**2-x0-12*y0+1,
            3*x0**2-12*x0+y0**2-3*z0**2+8])
        # creamos la matriz Ji
        J0 = np.array([[ 2*x0-4 , 2*y0 , 0 ],
            [ 2*x0-1 , -12 , 0 ],
            [ 6*x0-12 , 2*y0 , -6*z0]])
        # comprobación de determinante != 0
        if np.linalg.det(J0) != 0:
            # obtenemos el nuevo vector a partir del anterior
            X1 = X0 - np.dot(np.linalg.inv(J0),FX0)
            # calculamos el error absoluto
            erabs = max( abs(X1[0]-X0[0]), abs(X1[1]-X0[1]))
            # agregamos los resultados de la iteración a "resultados"
            resultados.append([i, X1, FX0, erabs])
            # cambiamos los valores de Xi por los nuevos
            X0 = X1
            x0 = X1[0]
            y0 = X1[1]
            z0 = X1[2]
        else:
            det = True
    print(tabulate(resultados, headers=["it","Xi","FXi","Ea"]))
    # si es singular
    if det:
        print(singularidad)
    # si se alcanzó la tolerancia
    elif erabs < tol:
        print(f"Se encontró la raíz {X1} en la iteración {i} con un error de {erabs}")
    else:
        print(f"No se alcanzó la tolerancia en las iteraciones indicadas, se encontró la raíz {X1}")

def tomar_datos_r2(sistema):
    """Función de recolección de datos iniciales
    
    Función que toma los valores iniciales para 
    comenzar a iterar. Luego envía al sistema 
    elegido. Funciona para los sistemas de 2 variables.
    """

    #ciclo para mantenerse en el mismo sistema
    while True:
        x = float(input(valor_x))
        y = float(input(valor_y))
        lim = int(input(valor_lim))
        tol = float(input(valor_tol))
        if sistema == 1:
            sistema1(x, y, lim, tol)
        else:
            sistema2(x, y, lim, tol)
        repeticion = input(reusar_sistema)
        if repeticion == "n" or repeticion == "N":
            break

def tomar_datos_r3(sistema):
    """Función de recolección de datos iniciales
    
    Función que toma los valores iniciales para 
    comenzar a iterar. Luego envía al sistema 
    elegido. Funciona para los sistemas de 3 variables.
    """

    # ciclo para mantenerse en el mismo sistema
    while True:
        x = float(input(valor_x))
        y = float(input(valor_y))
        z = float(input(valor_z))
        lim = int(input(valor_lim))
        tol = float(input(valor_tol))
        if sistema == 3:
            sistema3(x, y, z, lim, tol)
        else:
            sistema4(x, y, z, lim, tol)
        repeticion = input(reusar_sistema)
        if repeticion == "n" or repeticion == "N":
            break

def seleccionar_opcion():
    """Función para seleccionar el sistema de ecuaciones
  
    Función que envía a la lectura de datos iniciales
    adecuada. Si la opción seleccionada fue salir,
    regresa al menú sin preguntar sobre otro sistema.
    Regresa bool pasar_pregunta
    """

    # ciclo para dar una respuesta válida
    while True:
        respuesta = int(input("¿Con qué sistema deseas trabajar (1 a 5)? "))
        if 1 <= respuesta <= 5:
            break
        else:
            print("Respuesta fuera del rango")
    if 1 <= respuesta <=2:
        tomar_datos_r2(respuesta)
        return True
    if 3 <= respuesta <= 4:
        tomar_datos_r3(respuesta)
        return True
    else:
        return False


def menu_opciones():
    """Menú de opciones de opción 1"""

    # ciclo para mantenerse dentro de opción 1
    while True:
        print(sistemas)
        pasar_pregunta = seleccionar_opcion()
        salir_sistema = "n"
        if pasar_pregunta:
            print("Regresando al menú del método")
            salir_sistema = input("¿Deseas trabajar con otro sistema (S/N)? ")
        if salir_sistema == "n" or salir_sistema == "N":
            print("Regresando al menú principal")
            break