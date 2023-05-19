#Ejercicio 5 Listas y Tuplas
#programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas

lista=[1,2,3,4,5,6,7,8,9,10]
for k in range(1, 11):
    for x in range(1,11):
        if lista[-x]<lista[x-1]:
            aux=lista[-x]
            lista[-x]=lista[x-1]
            lista[x-1]=aux
print("La lista de mayor a menor es: ")
print(lista)            