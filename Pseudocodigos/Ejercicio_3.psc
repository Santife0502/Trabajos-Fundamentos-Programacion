Algoritmo Ejercicio_3
	//Calcular la aceleracion y distancia recorrida de una locomotora
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//12/2/2023
	
	//Definicion de variables
	Definir Velocidad_Final,Velocidad_Inicial,Tiempo,Distancia_Recorrido Como Entero;
	Definir Aceleracion Como Real;
	
	//Declaracion de variables
	Velocidad_Final<-25;
	Velocidad_Inicial<-0;
	Tiempo<-10;
	Variable_Operacion<-1/2;
	
	//Entradas
	Escribir "Velocidad Final ", Velocidad_Final;
	Escribir "Velocidad Inicial ", Velocidad_Inicial;
	Escribir "Tiempo de Aceleracion ", Tiempo;
	
	//Procesos
	Aceleracion<-(Velocidad_Final-Velocidad_Inicial)/Tiempo;
	Distancia_Recorrido<-(Variable_Operacion*Velocidad_Final)*Tiempo;
	
	//Salidas
	Escribir "La Aceleracion fue de ", Aceleracion; 
	Escribir "La Distancia Recorrida fue de ", Distancia_Recorrido;
	
	
	
	
FinAlgoritmo
