Algoritmo Ejercicio_19
	
	Definir dia1, diaActual, numDias, resto Como Entero
	
	Escribir "Ingrese el d�a de la semana en que cay� el d�a 1 del mes actual"
	Escribir "1= Lunes"
	Escribir "2= Martes"
	Escribir "3= Miercoles"
	Escribir "4= Jueves"
	Escribir "5= Viernes"
	Escribir "6= Sabado"
	Escribir "7= Domingo"
	Leer dia1
	
	Escribir "Ingrese el n�mero de d�as transcurridos desde el d�a 1 del mes actual: "
	Leer numDias
	
	resto <- numDias % 7
	diaActual <- (dia1 + resto - 1) % 7 + 1
	
	Escribir "Hoy es el d�a ", diaActual, " de la semana."
	
FinAlgoritmo

