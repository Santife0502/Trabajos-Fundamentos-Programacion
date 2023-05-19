#Ejercicio sueldos lista 2
sueldos=[]
for x in range(5):
    valor=int(input("Ingrese el sueldo: "))
    sueldos.append(valor)
print("Lista sin ordenar")
print(sueldos)

canInt=0
for k in range(4):     #se coloca un segundo ciclo para repetir el proceso con todos los datos ingresados
    for x in range (4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
            canInt=canInt+1
print("Lista ordenada")
print(sueldos)    
print("Cantidad de intercambios:", canInt) 
       

