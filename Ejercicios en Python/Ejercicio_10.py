# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular el valor de una llamada Telefonica
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 3/3/2023
	# Definicion de variables
	minutos = int()
	valor_m = int()
	incremento = int()
	ma = int()
	valor_m2 = int()
	# Declaracion de variables
	minutos = 0
	valor_m = 10
	incremento = 5
	# Entradas,procesos y salidas
	print("Digite la cantidad de Minutos: ")
	minutos = int(input())
	if minutos>0:
		if minutos<3:
			print("El valor de la llamada fue de: ",valor_m," Centimos")
		else:
			ma = minutos-2
			valor_m2 = valor_m+(ma*incremento)
			print("El valor de llamada fue de: ",valor_m2," Centimos")
	else:
		print("ERROR")

