# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular la suma de los pares del 2 al 100
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 28/2/2023
	# Definicion de variables
	num = int()
	suma = int()
	# Declaracion de variables
	suma = 2
	num = 4
	# Procesos
	while (num<=100):
		suma = (suma+num)
		num = (num+2)
	# Salidas
	print("Suma pares entre 2 y 100= ",suma)

