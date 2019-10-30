#Tania Delgado - Anyely Gomez
#Evaluación Nro. 1 - Pensamiento computacional

import os

def jugadores():

    os.system("cls")

    print("Digite la cantidad de jugadores minimo 2, maximo 4: \n")
    print("\t2 - Jugadores")
    print("\t3 - Jugadores")
    print("\t4 - Jugadores")

def carrera():    

    print("\nElija el nivel de tablero a jugar, considere el siguiente menu: \n")
    print("1. Nivel básico(Tablero de 20 posiciones)")
    print("2. Nivel intermedio(Tablero de 30 posiciones)")
    print("3. Nivel avanzado(Tablero de 50 posiciones)\n")
    print("4. Salir")

    op = input("Digite la opcion del menu de acuerdo al nivel que quiere jugar: ")

    if opc=="1":
		print ("1. Nivel básico(Tablero de 20 posiciones)")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif op=="2":
		print ("2. Nivel intermedio(Tablero de 30 posiciones)")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    elif op=="3":
		print ("3. Nivel avanzado(Tablero de 50 posiciones)")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
    elif op=="4":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

carrera()