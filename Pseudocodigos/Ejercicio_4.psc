Algoritmo Ejercicio_4
	//Calcular el tiempo que tardara un cuerpo en alcanzar una velocidad de 144 k/h
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//14/2/2023
	
	//Definicion de variables
	Definir VF,VI,A Como Entero;
	Definir Conversor Como Real;
	
	//Declaracion de variables
	VF<-144;
	VI<-12;
	Aceleracion<-2;
	Conversor<-(VF/3.6);
	
	//Entradas
	Escribir "Velocidad Final " , VF;
	Escribir 'Velocidad Final convertida a m/s ', Conversor;
	Escribir "Velocidad Inicial ", VI " m/s";
	Escribir "Aceleracion ", Aceleracion " m/s^2";
	
	//Procesos
	Tiempo_Aceleracion<-(Conversor-12)/Aceleracion;
	
	//Salidas
	Escribir "El Tiempo de Aceleracion fue de ", Tiempo_Aceleracion " m/s^2";
	
	
	
	
FinAlgoritmo
