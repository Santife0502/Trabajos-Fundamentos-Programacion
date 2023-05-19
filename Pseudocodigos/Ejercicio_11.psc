Algoritmo Ejercicio_11
	//Calcular la suma de los primeros 50 numeros enteros
	//Version 1.0
	//Desarrollado por Santiago Gomez 
	//3/3/2023
	
	//Definicion de variables
	Definir Num,Suma Como Entero;
	
	//Declaracion de variables
	Suma<-1;
	Num<-2;
	
	//Entradas y procesos
	Mientras Num<=50 Hacer
		Suma<-(Suma+Num);
		Num<-(Num+1);
	Fin Mientras
	
	//Salidas
	Escribir "La suma de los primeros 50 numeros enteros es de: ",Suma;
FinAlgoritmo
