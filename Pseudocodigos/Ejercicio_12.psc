Algoritmo Ejercicio_12
	//Calcular el producto de los n primeros numeros naturales
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//3/32023
	
	//Definicion de variables
	Definir Cantidad_NumN,Producto,Resultado  Como Entero;
	
	//Declaracion de variables
	Cantidad_NumN<-1;
	Producto<-0;
	Resultado<-1;
	
	
	//Entradas y procesos
	Escribir "Digite Numeros Naturales que se van a multiplicar, al poner 0 se realiza la operacion  ";
	Mientras Cantidad_NumN>0 Hacer
		Escribir "Digite numero";
		Leer Cantidad_NumN;
			Si Cantidad_NumN>0 Entonces
				Resultado<-Cantidad_NumN*Resultado;
				Producto<-Resultado;
			SiNo
				Si Cantidad_NumN<0 Entonces
					Escribir "Numero no valido";
				Fin Si
			Fin Si
		Fin Mientras
		//Salidas
		Si Cantidad_NumN=0 Entonces
		Escribir 'El producto fue de: ',Producto;
    FinSi
	FinAlgoritmo
