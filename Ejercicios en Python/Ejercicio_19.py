# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	dia1 = int()
	diaactual = int()
	numdias = int()
	resto = int()
	print("Ingrese el d�a de la semana en que cay� el d�a 1 del mes actual")
	print("1= Lunes")
	print("2= Martes")
	print("3= Miercoles")
	print("4= Jueves")
	print("5= Viernes")
	print("6= Sabado")
	print("7= Domingo")
	dia1 = int(input())
	print("Ingrese el n�mero de d�as transcurridos desde el d�a 1 del mes actual: ")
	numdias = int(input())
	resto = numdias%7
	diaactual = (dia1+resto-1)%7+1
	print("Hoy es el d�a ",diaactual," de la semana.")

