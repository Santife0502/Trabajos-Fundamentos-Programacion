# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular la aceleracion que tuvo un camion
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 10/2/2023
	# Area de definicion de variables
	velocidad_final = int();
	velocidad_inicial = int();
	tiempo_aceleracion = int();
	aceleracion = int();
	# Declaracion de variables
	velocidad_final = 25;
	velocidad_inicial = 20;
	tiempo_aceleracion = 5;
	# Entradas
	print("Velocdad Final ",25);
	print("Velocidad Inicial ",20);
	print("Tiempo Aceleracion ",5);
	# Procesos
	aceleracion = (velocidad_final-velocidad_inicial)/tiempo_aceleracion;
	# Salidas
	print("Aceleracion total de ",aceleracion);

