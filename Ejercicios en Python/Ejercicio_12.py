# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular el producto de los n primeros numeros naturales
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 3/32023
	# Definicion de variables
	cantidad_numn = int()
	producto = int()
	resultado = int()
	# Declaracion de variables
	cantidad_numn = 1
	producto = 0
	resultado = 1
	# Entradas y procesos
	print("Digite Numeros Naturales que se van a multiplicar, al poner 0 se realiza la operacion  ")
	while cantidad_numn>0:
		print("Digite numero")
		cantidad_numn = int(input())
		if cantidad_numn>0:
			resultado = cantidad_numn*resultado
			producto = resultado
		else:
			if cantidad_numn<0:
				print("Numero no valido")
	# Salidas
	if cantidad_numn==0:
		print("El producto fue de: ",producto)

