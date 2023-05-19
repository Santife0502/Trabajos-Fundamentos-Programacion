suma=0
inicio=1
cantidad=int(input("Digite la cantidad de numeros: "))
while (inicio<=cantidad):
    inicio=inicio+1
    numero=int(input("Digite los numeros a sumar: "))
    suma=int(suma+numero)
print("El resultado es: ",suma)