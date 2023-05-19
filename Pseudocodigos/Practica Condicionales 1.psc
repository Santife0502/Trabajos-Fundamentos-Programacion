Algoritmo Practica_Condicional1
	//Leer 2 numeros e informar cual es el mayor
	//Version 1.0
	//Desarrollado por: Santiago Gomez
	//27/02/2023
	
	//Area de definicion de variable
	Definir v_numUno,v_numero2,v_Mayor Como Real;
	
	//Inicializar Variables
	v_numUno<-0;
	v_numero2<-0;
	v_Mayor<-0;
	
	//Entradas
	Escribir "Digite el primer numero: ";
	Leer v_numUno;
	Escribir "Digite el segundo numero: ";
	Leer v_numero2;
	
	//Procesos y Salidas
	Si v_numUno=v_numero2 Entonces
		Escribir " No hay numero mayor, los dos son iguales";
	SiNo
		Si v_numUno>v_numero2 Entonces
			v_Mayor= v_numUno;
		SiNo
			v_Mayor=v_numero2;
		Fin Si
		Escribir "El numero mayor es:", v_Mayor;
	Fin Si

FinAlgoritmo
