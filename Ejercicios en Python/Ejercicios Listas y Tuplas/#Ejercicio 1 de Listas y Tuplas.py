#Ejercicio 1 de Listas y Tuplas
#Programa para imprimir asignaturas

asignaturas=[]
canAsig=int(input("Digite el numero de asignaturas que ve: "))
for x in range(canAsig):
    asignatura=input("Digite la asignatura: ")
    asignaturas.append(asignatura)
print("Las asignaturas son: ", asignaturas)
