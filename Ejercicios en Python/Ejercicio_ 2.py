# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular aceleracion de un formula 1 que parte del reposo
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 11/2/2023
	# Definicion de variables
	conversor = float()
	aceleracion = float()
	velocidad_final = int()
	velocidad_inicial = int()
	tiempo_aceleracion = int()
	# Declaracion de variables
	velocidad_inicial = 0
	# k/h
	velocidad_final = 216
	# s
	tiempo_aceleracion = 10
	# m/s
	conversor = (velocidad_final/3.6)
	# Entradas
	print("Velocidad inicial ",velocidad_inicial,"k/h")
	print("Velocidad Final ",velocidad_final,"k/h")
	print("Tiempo Aceleracion ",tiempo_aceleracion,"S")
	# Procesos
	aceleracion = (conversor-velocidad_inicial)/tiempo_aceleracion
	# Salida
	print("La aceleracion es ",aceleracion,"m/s2")

