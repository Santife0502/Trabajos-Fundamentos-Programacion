#Ejercicio 2 de Listas y Tuplas
#Programa que almacene asignaturas en una lista y diga " Yo estudio "asignatura" "

asignaturas=[]
canAsig=int(input("Digite el numero de asignaturas que ve: "))
for x in range(canAsig):
 asignatura=input("Digite la asignatura: ")
 asignaturas.append(asignatura)
print("Las asignaturas son: ", asignaturas)
for asignatura in asignaturas:
 print("Yo estudio: " + asignatura)
