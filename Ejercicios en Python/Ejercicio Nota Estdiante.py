# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# Calcula nota final estudiante
	# Version 1.0
	# Deszarrollado por Santiago Gomez
	# 28/2/2023
	# Definicion de variables
	nombre = str()
	nota1 = float()
	nota2 = float()
	nota3 = float()
	n1 = float()
	n2 = float()
	n3 = float()
	promedio = float()
	porcentaje1 = float()
	porcentaje2 = float()
	numero_inasistencias = int()
	# Declaracion de variables
	nombre = i
	nota1 = n
	nota2 = z
	nota3 = h
	numero_inasistencias = a
	porcentaje1 = 0.35
	porcentaje2 = 0.3
	# Entradas
	print("Nombre de Usuario: ")
	nombre = input()
	print("Digite la primera Nota: ")
	nota1 = float(input())
	print("Digite la segunda Nota: ")
	nota2 = float(input())
	print("Digite la tercera Nota: ")
	nota3 = float(input())
	print("Numero de Inasistencias: ")
	numero_inasistencias = int(input())
	# Procesos y Salidas
	n1 = (nota1*porcentaje1)
	n2 = (nota2*porcentaje1)
	n3 = (nota3*porcentaje2)
	if (numero_inasistencias>=12):
		print(nombre," Reprobo la materia")
	else:
		promedio = (n1+n2+n3)
		print(nombre," su promedio fue de: ",promedio)
	if (promedio>=3.5):
		print(nombre," Aprobo la materia")
	else:
		print(nombre," Reprobo la materia con promedio de: ",promedio)

