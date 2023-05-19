# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Leer 2 numeros e informar cual es el mayor
	# Version 1.0
	# Desarrollado por: Santiago Gomez
	# 27/02/2023
	# Area de definicion de variable
	v_numuno = float()
	v_numero2 = float()
	v_mayor = float()
	# Inicializar Variables
	v_numuno = 0
	v_numero2 = 0
	v_mayor = 0
	# Entradas
	print("Digite el primer numero: ")
	v_numuno = float(input())
	print("Digite el segundo numero: ")
	v_numero2 = float(input())
	# Procesos
	if v_numuno==v_numero2:
		print(" No hay numero mayor, los dos son iguales")
	else:
		if v_numuno>v_numero2:
			v_mayor = v_numuno
		else:
			v_mayor = v_numero2
		print("El numero mayor es:",v_mayor)

