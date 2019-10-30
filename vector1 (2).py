#EJERCICIO 1
#fruits = ["Apple, Banana, Orange"]

#print("The first value is: ", fruits[0])
#print("The last value is: ", fruits[2])

#EJERCICIO 2
'''
   Escriba un programa que reciba en una lista de 10 numeros
   ingresados por el usuario desde consola.
'''

#N = []
#i = 1

'''Create List'''

#while i <= 10:
 #   print("Press number ", i ,":")
 #   X = int(input())
 #   N.append(X)
 #   i = i + 1

'''Show List'''

#i = 1
#while i < 10:
#    print("The value in the pos", i ,"is: ", N[i])
#    i = i + 1

#N.__len__()

#EJERCICIO 3
import os
from random import randint, uniform, random

def menu():
    os.system("cls")
    print(":::MENU:::")
    print("[1]. Add new number to list")
    print("[2]. Show list")
    print("[3]. List first. number")
    print("[4]. List last number")
    print("[5]. Exit")
    print(".:: Press an option. ")




N = []

n = int(input("Cuantos numeros aleatorios desea generar? "))


def aleatorios():
    a = randint(0,100)
    return n
