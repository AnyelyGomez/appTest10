#Tania Delgado - Anyely Gomez
#Factorial

import os

def fac():
    os.system("cls")
    print(":::FACTORIAL:::\n")
    n = int(input("Ingrese un numero mayor que cero: "))

    while n <= 0:
        print("\nEl numero ingresado no es correcto!!!")
        n = int(input("Ingrese un numero mayor que cero: "))
    
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("\nEl factorial de ", n, " es ", factorial, "\n")
         
fac()