# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular el salario de un trabajador segun el numero de horas trabajadas y el valor de las horas, y si pasa de 40 horas se tiene un incremento de 1.5 la hora adicional
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 28/2/2023
	# Definicion de variables
	nombre = str()
	numero_horas = int()
	valor_horas = int()
	salario = int()
	incremento = float()
	salario2 = float()
	salario_incremento = float()
	# Declaracion de variables
	nombre = n
	numero_horas = z
	valor_horas = h
	incremento = 1.5
	# Entradas y Procesos
	print("Nombre de Usuario: ")
	nombre = input()
	print("Numero de Horas Trabajadas: ")
	numero_horas = int(input())
	print("Valor Horas Trabajadas: ")
	valor_horas = int(input())
	salario = (numero_horas*valor_horas)
	salario2 = (salario*incremento)
	salario_incremento = (salario+salario2)
	# Salidas
	if (numero_horas>40):
		print("El salario del trabajador con horas extraordinarias fue de: ",salario_incremento)
	else:
		print("El salario del trabajador fue de: ",salario)

