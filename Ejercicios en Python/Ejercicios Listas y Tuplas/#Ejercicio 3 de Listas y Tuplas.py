#Ejercio 3 de Listas y Tuplas
#Programa para almacenar las asignaturas de un curso y pregunte al usuario la nota que ha sacado en cada asignatura

asignaturas=[]
notas=[]
canAsig=int(input("Digite la cantidad de materias que ve: "))
for x in range (canAsig):
    asign=input("Digite la asignatura: ")
    nota=float(input("Digite la nota de la asignatura anterior: "))
    asignaturas.append(asign)
    notas.append(nota)
print("Las asignaturas fueron: ", asignaturas)
for i in range(len(asignaturas)):
    print("En la asignatura", asignaturas[i], "ha sacado", notas[i])  