Algoritmo Ejercicio_13
	//Algoritmo para resolver una ecuacion de segundo grado AX2+BX+C
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//12/3/2023
	
	//Definicion de variables
	Definir A,B,C,Ecu1,Ecu2,V Como Real
	//Declaracion de variables
	A<-a
	B<-b
	C<-c
	
	//Entradas
	Escribir "Resolucion de la ecuacion de segundo grado Ax^2+Bx+C"
	Escribir "Digite el valor de la variable A"
	Leer A
	Escribir "Digite el valor de la variable B"
	Leer B
	Escribir "Digite el valor de la variable C"
	Leer C
	//Procesos y Salidas
	Si A=0 Entonces
		Escribir "La ecuacion es una indeterminacion"
	SiNo
		V= RC (B*B)-4*A*C
		Si V>0 Entonces
			Ecu1<--B+(V)/(2*A)
			Ecu2<- -B-RC(V)/(2*A)
			Escribir "Para resolver la ecuacion se usa la formula -b+-RC(b*b-4ac)/2a "
			Escribir "El primer Valor de x fue de: ",Ecu1
			Escribir "El segundo Valor de x fue de: ",Ecu2
		SiNo
			Si V<0 Entonces
				Ecu1 = -B / (2 * A)
				Escribir "Para resolver la ecuacion se usa la formula -b/2a "
				Escribir "El primer Valor de x fue de: ",Ecu1
			FinSi
		Fin Si
	Fin Si
	
FinAlgoritmo
