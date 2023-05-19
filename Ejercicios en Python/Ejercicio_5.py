# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular el salario de los trabajadores de una empresa
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 20/2/2023
	# Definicion Variables
	a = int()
	z = int()
	total_horas = int()
	h = int()
	valor_horad = int()
	incremento = float()
	descuento = float()
	valor_horan = float()
	salario_base = float()
	salario_final = float()
	salario = float()
	nombre = str()
	# Declaracion de variables y Entradas
	nombre = n
	print("Nombre de usuario ")
	nombre = input()
	print("Numero de Horas Diurnas Trabajadas ")
	a = int(input())
	print("Numero de Horas Nocturnas Trabajadas ")
	z = int(input())
	total_horas = (a+z)
	print("Total de Horas Trabajadas ",total_horas)
	print("Valor Horas Diurnas Trabajadas ")
	h = int(input())
	# Procesos
	valor_horad = (a*h)
	print("Pago por Horas Diurnas ",valor_horad)
	incremento = 1.40
	valor_horan = (z*h)*incremento
	print("Pago por Horas Nocturnas ",valor_horan)
	salario_base = (valor_horad+valor_horan)
	print("El Salario Base fue de ",salario_base)
	descuentos = 0.19
	salario = (salario_base*descuentos)
	salario_final = (salario_base-salario)
	# Salidas
	print("El Salario Final fue de ",salario_final)

