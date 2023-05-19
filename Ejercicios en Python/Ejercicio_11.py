# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular la suma de los primeros 50 numeros enteros
	# Version 1.0
	# Desarrollado por Santiago Gomez 
	# 3/3/2023
	# Definicion de variables
	num = int()
	suma = int()
	# Declaracion de variables
	suma = 1
	num = 2
	# Entradas y procesos
	while num<=50:
		suma = (suma+num)
		num = (num+1)
	# Salidas
	print("La suma de los primeros 50 numeros enteros es de: ",suma)

