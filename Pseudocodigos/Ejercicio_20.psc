Algoritmo Ejercicio_20
	//Decir cual es el numero mayor de 3 digitados (Los 3 son diferentes)
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//6/3/2023
	
	//Definicion de variables
	Definir Numero_1,Numero_2,Numero_3 Como Real
	
	//Declaracion de variables
	Numero_1<-n;
	Numero_2<-j;
	Numero_3<-h;
	//Entradas
	Escribir "Digite numero 1:";
	Leer Numero_1;
	Escribir "Digite numero 2:";
	Leer Numero_2;
	Escribir "Digite numero 3:";
	Leer Numero_3;
	//Procesos y Salidas
	Si Numero_1>Numero_2 y Numero_1>Numero_3 Entonces
		Escribir "El numero mayor fue: ",Numero_1;
	SiNo
		Si Numero_2>Numero1 y Numero_2>Numero_3 Entonces
			Escribir "El numero mayor fue: ", Numero_2;
		SiNo
			Escribir "El numero mayor fue: ",Numero_3;
			
		Fin Si
	Fin Si
	
FinAlgoritmo
