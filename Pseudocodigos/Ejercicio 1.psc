Algoritmo EjercicioCamion
	//Calcular la aceleracion que tuvo un camion
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//10/2/2023
	
	//Area de definicion de variables
	Definir Velocidad_Final,Velocidad_Inicial,Tiempo_Aceleracion,Aceleracion Como Entero;
	
	//Declaracion de variables
	Velocidad_Final <- 25;
	Velocidad_Inicial <- 20;
	Tiempo_Aceleracion <- 5;
	
	//Entradas
	Escribir 'Velocdad Final ',25;
	Escribir 'Velocidad Inicial ',20;
	Escribir 'Tiempo Aceleracion ',5;
	
	//Procesos
	Aceleracion <- (Velocidad_Final-Velocidad_Inicial)/Tiempo_Aceleracion;
	
	//Salidas
	Escribir 'Aceleracion total de ',Aceleracion;
FinAlgoritmo
