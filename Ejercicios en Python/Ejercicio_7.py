# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular la media de una serie de numeros positivos cuando se coloca el 0
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 28/2/2023
	cantidad_numeros = int()
	media = float()
	suma = float()
	dato = float()
	# area de inicializacion de variables//
	dato = 0
	media = 0
	cantidad_numeros = 0
	suma = 0
	# Entradas y procesos
	print("Introducir datos numericos, para calcular la media ")
	dato = float(input())
	if dato<0:
		print("No se ingresaron numeros positivos ")
	while dato>0:
		if dato>0:
			suma = suma+dato
			cantidad_numeros = cantidad_numeros+1
		dato = float(input())
	if dato==0:
		media = suma/cantidad_numeros
	# Salidas
	print("La media de los numeros ingresados fue de: ",media)

