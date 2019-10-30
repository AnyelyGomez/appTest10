
#Tania Delgado - Anyely Gomez
#Fibonacci

import os

os.system("cls")
print(":::FIBONACCI:::\n")

print("Imprimir por pantalla los 20 primeros términos de la sucesión Fibonacci.\n")

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
for x in range(20):
    print(fib(x))