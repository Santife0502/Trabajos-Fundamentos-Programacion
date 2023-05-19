# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Resolucion de una ecuacion de primer grado
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 5/3/2023
	# Definicion de variables
	x = float()
	a = float()
	b = float()
	ecud = float()
	ecup1 = float()
	ecup2 = float()
	# Declaracion de variables
	x = x
	a = z
	b = j
	# Entradas, Procesos y Salidas
	print("La Ecuacion Principal es ax+b=0 ")
	print("Digite el valor de a: ")
	a = float(input())
	print("Digite el valor de b: ")
	b = float(input())
	if a<0:
		ecup1 = (-b/a)
		print("Al despejar la ecuacion queda asi: x= -b/-a ")
		print("El resultado de la ecuacion fue de x= ",ecup1)
	else:
		if b<0:
			ecup2 = (b/a)
			print("Al despejar la ecuacion queda asi: x= b/a ")
			print("El resultado de la ecuacion fue de x= ",ecup2)
		else:
			if a==0:
				print("La ecuacion es una Indeterminacion")
			else:
				ecud = (-b/a)
				print("Al despejar la ecuacion queda asi: x= -b/a ")
				print("El resultado de la ecuacion fue de x= ",ecud)

