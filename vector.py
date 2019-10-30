#Tania Delgado - Anyely Gomez
#Vector punto 8

import os
datos=[]

def vector():
    os.system("cls")
    print(":::VECTOR SUMA:::\n")
    suma=0
    for i in range(0,100):
     
        n=int(input("Digite un numero: "))
        if n==suma:
            print("\nNO es posible agregar ese número, ya que la suma")
            print("del ultimo valor: {} y del penultimo valor: {}".format(a,b))
            print("es: ",suma,"\n")
        else:
            datos.append(n)
            a=datos[len(datos)-1]
            b=datos[len(datos)-2]
            suma=a+b
    
vector()
print (datos)