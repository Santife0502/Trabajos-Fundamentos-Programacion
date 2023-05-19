# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular el salario de un trabajador
	# Version1.0
	# Desarrollado por Santiago Gomez
	# 27/2/2023
	# Definicion de variables
	nombre = str()
	numero_horas = int()
	valor_hora = int()
	salario_base = int()
	salario_final = int()
	salario_tasas = float()
	# Declaracion de variables
	nombre = i
	numero_horas = h
	valor_hora = n
	tasas = 0.25
	# Entradas y Procesos
	print("Digite Nombre de Usuario: ")
	nombre = input()
	print("El numro de horas trabajadas fue de: ")
	numero_horas = int(input())
	print("El Valor por las horas trabajadas fue de: ")
	valor_hora = int(input())
	salario_base = (valor_hora*numero_horas)
	print("El Salario Base es de: ",salario_base)
	salario_tasas = (salario_base*tasas)
	print("El salario con la aplicacion de Tasas de Interes es de: ",salario_tasas)
	salario_final = (salario_base-salario_tasas)
	# Salidas
	print(nombre," Su Salario Final fue de: ",salario_final)

