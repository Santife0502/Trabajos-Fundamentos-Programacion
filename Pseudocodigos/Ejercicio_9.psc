Algoritmo Ejercicio_9
	//Calcular el salario de un trabajador segun el numero de horas trabajadas y el valor de las horas, y si pasa de 40 horas se tiene un incremento de 1.5 la hora adicional
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//28/2/2023
	
//Definicion de variables
	Definir Nombre Como Caracter;
	Definir Numero_Horas,Valor_Horas,Salario Como Entero;
	Definir Incremento,Salario2,Salario_Incremento Como Real;
	
	//Declaracion de variables
	Nombre<-n;
	Numero_Horas<-z;
	Valor_Horas<-h;
	Incremento<-1.5;
	
	//Entradas y Procesos
	Escribir "Nombre de Usuario: ";
	Leer Nombre;
	Escribir "Numero de Horas Trabajadas: ";
	Leer Numero_Horas;
	Escribir "Valor Horas Trabajadas: ";
	Leer Valor_Horas;
	Salario<-(Numero_Horas*Valor_Horas);
	Salario2<-(Salario*Incremento);
	Salario_Incremento<-(Salario+Salario2);
	
	//Salidas
	Si (Numero_Horas>40) Entonces;
		Escribir Nombre " su salario del trabajador con horas extraordinarias fue de: ",Salario_Incremento;
	SiNo
		Escribir Nombre " su salario del trabajador fue de: ", Salario;
	Fin Si
	
FinAlgoritmo
