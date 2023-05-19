Algoritmo Ejercicio_19
	
	Definir dia1, diaActual, numDias, resto Como Entero
	
	Escribir "Ingrese el día de la semana en que cayó el día 1 del mes actual"
	Escribir "1= Lunes"
	Escribir "2= Martes"
	Escribir "3= Miercoles"
	Escribir "4= Jueves"
	Escribir "5= Viernes"
	Escribir "6= Sabado"
	Escribir "7= Domingo"
	Leer dia1
	
	Escribir "Ingrese el número de días transcurridos desde el día 1 del mes actual: "
	Leer numDias
	
	resto <- numDias % 7
	diaActual <- (dia1 + resto - 1) % 7 + 1
	
	Escribir "Hoy es el día ", diaActual, " de la semana."
	
FinAlgoritmo

