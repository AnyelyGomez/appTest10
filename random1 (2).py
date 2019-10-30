#randint: generate random integer numbers
#uniform: generate random foat numbers
import  os
from random import randint, uniform, random

def Z():
    a = randint(0,100)
    return a

def R():
    b = uniform(0,100)
    return b

os.system("cls")
print("The Z number generated is: ", Z())
print("The R number generated is: ", R())