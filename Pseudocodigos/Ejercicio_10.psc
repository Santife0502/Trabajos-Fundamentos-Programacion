Algoritmo Ejercicio_10
	//Calcular el valor de una llamada Telefonica
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//3/3/2023
	
	//Definicion de variables
	Definir Minutos,Valor_M,Incremento,MA,Valor_M2 Como Entero;
	//Declaracion de variables
	Minutos<-0;
	Valor_M<-10;
	Incremento<-5;
	
	//Entradas,procesos y salidas
	Escribir "Digite la cantidad de Minutos: ";
	Leer Minutos;
	Si Minutos>0 Entonces
		Si Minutos<3 Entonces
			Escribir "El valor de la llamada fue de: ",Valor_M " Centimos";
		SiNo
			MA<-Minutos-2;
		    Valor_M2<-Valor_M+(MA*Incremento);
			Escribir "El valor de llamada fue de: ", Valor_M2 " Centimos";
		Fin Si
	SiNo
		Escribir "ERROR";

	Fin Si
FinAlgoritmo
