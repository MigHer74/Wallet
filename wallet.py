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

# Estructura de Control del Menu Principal

continuar = True

while continuar:
    sel = input("Elija una opción: ")

    if sel == "x":
        print("Hasta luego")
        continuar = False
    else:
        print("Hiciste la seleccion " + str(sel))