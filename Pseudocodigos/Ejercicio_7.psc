Algoritmo Ejercicio_7
	//Calcular la media de una serie de numeros positivos cuando se coloca el 0
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//28/2/2023
	Definir Cantidad_Numeros Como Entero
	Definir Media, Suma, Dato Como Real

	//area de inicializacion de variables//
	Dato = 0
	Media = 0 
	Cantidad_Numeros = 0
	Suma<-0
	//Entradas y procesos
	Escribir "Introducir datos numericos, para calcular la media "
	Leer Dato
	Si Dato<0 Entonces
		Escribir "No se ingresaron numeros positivos "
	FinSi
	 Mientras Dato>0 Hacer
		Si Dato>0 Entonces
			Suma<-Suma+Dato
			Cantidad_Numeros<-Cantidad_Numeros+1
		Fin Si
		Leer Dato
	Fin Mientras
	
	Si Dato=0 Entonces
		Media<-Suma/Cantidad_Numeros
		
	FinSi
	
	//Salidas
	Escribir "La media de los numeros ingresados fue de: ", Media
	
FinAlgoritmo
