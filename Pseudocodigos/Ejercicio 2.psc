Algoritmo Ejercicio_f1
	//Calcular aceleracion de un formula 1 que parte del reposo
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//11/2/2023
	
	//Definicion de variables
	Definir Conversor, Aceleracion Como Real;
	Definir Velocidad_Final,Velocidad_Inicial,Tiempo_Aceleracion Como Entero;
	
	//Declaracion de variables
	Velocidad_Inicial<-0;
	Velocidad_Final<-216;//k/h
	Tiempo_Aceleracion<-10;//s
	Conversor<-(Velocidad_Final/ 3.6); //m/s
	
	//Entradas
	Escribir "Velocidad inicial ", Velocidad_Inicial, "k/h";
	Escribir "Velocidad Final ", Velocidad_Final, "k/h";
	Escribir "Tiempo Aceleracion ", Tiempo_Aceleracion, "S";
	
	//Procesos
	Aceleracion<-(Conversor-Velocidad_Inicial)/Tiempo_Aceleracion;
	
	//Salida
	Escribir "La aceleracion es ", Aceleracion, "m/s2";
	
FinAlgoritmo
