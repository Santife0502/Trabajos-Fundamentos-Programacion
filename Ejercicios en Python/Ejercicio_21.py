# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Resolver una ecuación de segundo grado, dando soluciones con números imaginarios
	# desarrollado por Santiago Gomez
	# Version 1.0
	# 12/3/2023
	# Definicion de variables
	a = float()
	b = float()
	c = float()
	ecu1 = float()
	ecu2 = float()
	r = float()
	v = float()
	i = float()
	# Entradas
	print("Ingresa el valor de A: ")
	a = float(input())
	print("Ingresa el valor de B: ")
	b = float(input())
	print("Ingresa el valor de C: ")
	c = float(input())
	# Procesos y Salidas
	while a==0:
		print("Es una indeterminacion ")
	if a!=0:
		v = (b*b)-4*a*c
		if v==0:
			ecu1 = -b/(2*a)
			ecu2 = -b/(2*a)
			print("El primer Valor de x fue de: ",ecu1)
			print("El segundo Valor de x fue de: ",ecu2)
		else:
			if v>0:
				ecu1 = -b+sqrt((b*b)-4*a*c)/(2*a)
				ecu2 = -b-sqrt((b*b)-4*a*c)/(2*a)
				print("El primer Valor de x fue de: ",ecu1)
				print("El segundo Valor de x fue de: ",ecu2)
			else:
				if v<0:
					i = sqrt(abs(-v/(2*a)))
					r = -b/(2*a)
					print(r," + ",i," imaginario")
					print(r," - ",i," imaginario")

