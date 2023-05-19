# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular el tiempo que tardara un cuerpo en alcanzar una velocidad de 144 k/h
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 14/2/2023
	# Definicion de variables
	vf = int()
	vi = int()
	a = int()
	conversor = float()
	# Declaracion de variables
	vf = 144
	vi = 12
	aceleracion = 2
	conversor = (vf/3.6)
	# Entradas
	print("Velocidad Final ",vf)
	print("Velocidad Final convertida a m/s ",conversor)
	print("Velocidad Inicial ",vi," m/s")
	print("Aceleracion ",aceleracion," m/s^2")
	# Procesos
	tiempo_aceleracion = (conversor-12)/aceleracion
	# Salidas
	print("El Tiempo de Aceleracion fue de ",tiempo_aceleracion," m/s^2")

