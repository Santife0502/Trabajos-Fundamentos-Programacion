Algoritmo Ejercicio_18
	//Leida una fecha decir el dia de la semana suponiendo que el dia 1 del mes fue lunes
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//8/3/2023
	
	//Definicion de variables
	Definir Num_Dia Como Entero;
	
	//Declaracion de variables
	Num_Dia<-x;
	
	//Entradas
	Escribir "Digite una Fecha";
	Leer Num_Dia;
	//Procesos y salidas
	Segun Num_Dia Hacer
		1,8,15,22,29:;
			Escribir "El dia fue Lunes";
		2,9,16,23,30:;
			Escribir "El dia fue martes";
		3,10,17,24,31:;
			Escribir "El dia fue miercoles";
		4,11,18,25:;
			Escribir "El dia fue jueves";	
		5,12,19,26:;
			Escribir "El dia fue viernes";
		6,13,20,27:;
			Escribir "El dia fue sabado";
		7,14,21,28:;
			Escribir "El dia fue domingo";	
		De Otro Modo:
			Escribir "Digito un dato invalido";
	Fin Segun
FinAlgoritmo
