# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

from math import sqrt

if __name__ == '__main__':
	# Calcular el Area de un triangulo conociendo sus lados
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 5/3/2023
	# Definicion de variables
	lado_a = float()
	lado_b = float()
	lado_c = float()
	perimetro = float()
	semi_perimetro = float()
	area = float()
	# Declaracion de variables
	lado_a = a
	lado_b = b
	lado_c = c
	# Entradas y procesos
	print("Digite el valor del primer lado:")
	lado_a = float(input())
	print("Digite el valor del segundo lado:")
	lado_b = float(input())
	print("Digite el valor del tercer lado:")
	lado_c = float(input())
	perimetro = (lado_a+lado_b+lado_c)
	print("El perimetro del triangulo fue de: ",perimetro)
	semi_perimetro = (perimetro/2)
	print("El Semi Perimetro fue de: ",semi_perimetro)
	area = sqrt(semi_perimetro)*(semi_perimetro-lado_a)*(semi_perimetro-lado_b)*(semi_perimetro-lado_c)
	# Salidas
	print("El Area del Triangulo fue de: ",area)

