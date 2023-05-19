#Ejercicio 2 examen listas

numeros=[]
canNum=int(input("Digite la cantidad de numeros de la lista: "))
for x in range(canNum):
    num=int(input("Digite el numero: "))
    numeros.append(num)    
print("Lista completa: ")
print(numeros)
num2=int(input("Digite el numero que quiere reemplazar: "))
while num2 not in numeros:
    num2 = int(input("Valor no encontrado, ingrese nuevamente: "))
    if num2 in numeros: 
        break
while num2 in numeros:
    ind = numeros.index(num2)
    numeros[ind] = -1

print(numeros)    




