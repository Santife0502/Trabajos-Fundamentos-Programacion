# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Leida una fecha decir el dia de la semana suponiendo que el dia 1 del mes fue lunes
	# Version 1.0
	# Desarrollado por Santiago Gomez
	# 8/3/2023
	# Definicion de variables
	num_dia = int()
	# Declaracion de variables
	num_dia = x
	# Entradas
	print("Digite una Fecha")
	num_dia = int(input())
	# Procesos y salidas
	if num_dia==1 or num_dia==8 or num_dia==15 or num_dia==22 or num_dia==29:
		print("El dia fue Lunes")
	elif num_dia==2 or num_dia==9 or num_dia==16 or num_dia==23 or num_dia==30:
		print("El dia fue martes")
	elif num_dia==3 or num_dia==10 or num_dia==17 or num_dia==24 or num_dia==31:
		print("El dia fue miercoles")
	elif num_dia==4 or num_dia==11 or num_dia==18 or num_dia==25:
		print("El dia fue jueves")
	elif num_dia==5 or num_dia==12 or num_dia==19 or num_dia==26:
		print("El dia fue viernes")
	elif num_dia==6 or num_dia==13 or num_dia==20 or num_dia==27:
		print("El dia fue sabado")
	elif num_dia==7 or num_dia==14 or num_dia==21 or num_dia==28:
		print("El dia fue domingo")
	else:
		print("Digito un dato invalido")

