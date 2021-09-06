# Importacion de modulos
import os

# Estructura de Control del Menu Principal
# Limpieza de Pantalla y Mostrar el Menu 
continuar = True

while continuar:

    # Limpieza de pantalla
    os.system ("cls") 

    # Menu del Programa
    print("Menu Principal")
    print()
    print("1. Recibir")
    print("2. Transferir")
    print("3. Balance Sencillo")
    print("4. Balance General")
    print("5. Historico de Transacciones")
    print()
    print("x. Salir")
    print()

    sel = input("Elija una opción: ")

    if sel == "1":
        print("Seleccionaste Recibir")
    elif sel == "2":
        print("Seleccionaste Transferir")
    elif sel == "3":
        print("Seleccionaste Balance Sencillo")
    elif sel == "4":
        print("Seleccionaste Balance General")
    elif sel == "5":
        print("Seleccionaste Historico de Transacciones")
    elif sel == "x" or sel == "X":
        print("Adios, Hasta luego")
        continuar = False
    else:
        print("Opción " + sel + ",no es valida")