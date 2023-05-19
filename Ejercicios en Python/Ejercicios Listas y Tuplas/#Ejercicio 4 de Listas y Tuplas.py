#Ejercicio 4 de Listas y Tuplas
#Programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

numeros=[]
for x in range(6):
    num=int(input("Digite numero escogido del 1 al 49: "))
    numeros.append(num)
for k in range(5):
    for i in range(5):
        if numeros[i]>numeros[i+1]:
            aux=numeros[i]
            numeros[i]=numeros[i+1]
            numeros[i+1]=aux
print("Los numeros de la loteria de mayo a menor son:")
print(numeros)            


