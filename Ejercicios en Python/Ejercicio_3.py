# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular la aceleracion y distancia recorrida de una locomotora
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 12/2/2023
	# Definicion de variables
	velocidad_final = int()
	velocidad_inicial = int()
	tiempo = int()
	distancia_recorrido = int()
	aceleracion = float()
	# Declaracion de variables
	velocidad_final = 25
	velocidad_inicial = 0
	tiempo = 10
	variable_operacion = 1/2
	# Entradas
	print("Velocidad Final ",velocidad_final)
	print("Velocidad Inicial ",velocidad_inicial)
	print("Tiempo de Aceleracion ",tiempo)
	# Procesos
	aceleracion = (velocidad_final-velocidad_inicial)/tiempo
	distancia_recorrido = (variable_operacion*velocidad_final)*tiempo
	# Salidas
	print("La Aceleracion fue de ",aceleracion)
	print("La Distancia Recorrida fue de ",distancia_recorrido)

