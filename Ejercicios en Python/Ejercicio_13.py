# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Algoritmo para resolver una ecuacion de segundo grado AX2+BX+C
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 12/3/2023
	# Definicion de variables
	a = float()
	b = float()
	c = float()
	ecu1 = float()
	ecu2 = float()
	v = float()
	# Declaracion de variables
	a = a
	b = b
	c = c
	# Entradas
	print("Resolucion de la ecuacion de segundo grado Ax^2+Bx+C")
	print("Digite el valor de la variable A")
	a = float(input())
	print("Digite el valor de la variable B")
	b = float(input())
	print("Digite el valor de la variable C")
	c = float(input())
	# Procesos y Salidas
	if a==0:
		print("La ecuacion es una indeterminacion")
	else:
		v = sqrt(b*b)-4*a*c
		if v>0:
			ecu1 = -b+(v)/(2*a)
			ecu2 = -b-sqrt(v)/(2*a)
			print("Para resolver la ecuacion se usa la formula -b+-RC(b*b-4ac)/2a ")
			print("El primer Valor de x fue de: ",ecu1)
			print("El segundo Valor de x fue de: ",ecu2)
		else:
			if v<0:
				ecu1 = -b/(2*a)
				print("Para resolver la ecuacion se usa la formula -b/2a ")
				print("El primer Valor de x fue de: ",ecu1)

