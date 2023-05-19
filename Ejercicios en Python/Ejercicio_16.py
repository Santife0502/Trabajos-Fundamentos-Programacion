# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcular la nomina semanal de un trabajador
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 5/3/2023
	# Definicion de variables
	nombre = str()
	incremento = float()
	impuesto1 = float()
	impuesto2 = float()
	salario_i = float()
	salario_total = float()
	salario_ti1 = float()
	salario_ti2 = float()
	salario_im1 = float()
	salario_im2 = float()
	numero_horas = int()
	valor_horas = int()
	salario_b = int()
	# Declaracion de variables
	nombre = n
	numero_horas = d
	valor_horas = b
	incremento = 1.5
	impuesto1 = 0.2
	impuesto2 = 0.3
	# Entradas
	print("Digite Nombre de usuario:")
	nombre = input()
	print("Total de Horas Trabajadas: ")
	numero_horas = int(input())
	print("Valor por las Horas Trabajadas: ")
	valor_horas = int(input())
	salario_b = (numero_horas*valor_horas)
	# Procesos y Salidas
	if numero_horas<=35:
		salario_b = (numero_horas*valor_horas)
		print(nombre," su Salario Base fue de: ",salario_b," Euros")
	else:
		salario_i = (salario_b*incremento)
		salario_total = (salario_b+salario_i)
		print(nombre," su Salario Total fue de: ",salario_total," Euros")
	if salario_b<=2000:
		if salario_total<=2000:
			print(nombre," su Salario no tuvo aplicacion de impuestos")
		else:
			if salario_total==2220:
				salario_ti1 = (salario_total*impuesto1)
				print(nombre," su Salario Final con aplicacion de Impuestos es de: ",salario_ti1," Euros")
			else:
				if salario_total>2220:
					salario_ti2 = (salario_total*impuesto2)
					print("su Salario Final con aplicacion de Impuestos fue de: ",salario_ti2," Euros")
	else:
		if salario_b==2220:
			salario_im1 = (salario_b*impuesto1)
			print(nombre," su Salario Final con Aplicacion de Impuestos fue de: ",salario_im1," Euros")
		else:
			if salario_b>2220:
				salario_im2 = (salario_b*impuesto2)
				print(nombre," su Salario Final con aplicacion de Impuestos fue de: ",salario_im2," Euros")

