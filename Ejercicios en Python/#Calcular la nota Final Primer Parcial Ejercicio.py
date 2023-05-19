#Calcular la nota Final Primer Parcial
#Desarrollado por Santiago Gomez
#Version 1.0
#Fecha: 2/4/2023

#Definicion de variables
v_CanEst=0
v_Exteo=0.40
v_ExPra=0.60
v_concic=1
v_NomEst=""
v_GenEst=""
Notas=[]
# Leer cantidad de Estudiantes
v_CanEst= int(input("Digite cantidad de Estudiantes: "))


for v_concic in range(v_CanEst):
    v_nomEst = input("Digite Nombre del Estudiante : ")
    v_GenEst=input("Genero del Estudiante (M/F): ")
    v_notExTeo=float(input("Digite Nota Examen Teorico: "))
    v_notaExpr=float(input("Digite Nota Examen Practico: "))
    #Calculo de la Nota del Primer parcial de FUD
    v_notPriPar= (v_Exteo*v_notExTeo)+(v_ExPra*v_notaExpr)
    print("su Nota fue de: ", v_notPriPar)
    #Nota Maxima y Minima del Parcial
    Notas.append((v_notPriPar, v_GenEst))
Not_Max = max(Notas, key=lambda x: x[0])[0]
Not_Min = min(Notas, key=lambda x: x[0])[0]
suma_Not = sum([x[0] for x in Notas])
Prom_Gen = suma_Not / v_CanEst #Promedio General
Not_Muj = [x[0] for x in Notas if x[1] == "F"] # Nota Maxima, Minima y Promedio de las Mujeres
Not_MaxMuj = max(Not_Muj)
Not_MinMuj = min(Not_Muj)
Prom_NotMuj = sum(Not_Muj) / len(Not_Muj)
Not_Hom = [x[0] for x in Notas if x[1] == "M"] # Nota Maxima, Minima y Promedio de los Hombres
Not_MaxHom = max(Not_Hom)
Not_MinHom = min(Not_Hom)
Prom_NotHom = sum(Not_Hom) / len(Not_Hom)
print("La nota Maxima del Grupo la obtuvo",v_nomEst," y fue de: ",Not_Max)
print("La nota Minima del Grupo la obtuvo ",v_nomEst," y fue de: ",Not_Min)
print('El promedio del Grupo fue de: ',Prom_Gen)
print("La nota Maxima de las Mujeres la obtuvo ",v_nomEst," y fue de: ",Not_MaxMuj)
print("La nota Minima de las Mujeres la obtuvo ",v_nomEst," y fue de: ",Not_MinMuj)
print("El promedio de las Mujeres fue de: ",Prom_NotMuj)
print("La nota Maxima de los Hombres la obtuvo ",v_NomEst," y fue de: ",Not_MaxHom)
print("La nota Minima de los Hombres la obtuvo ",v_NomEst," y fue de: ",Not_MinHom)
print("El promedio de los Hombres fue de: ", Prom_NotHom)







