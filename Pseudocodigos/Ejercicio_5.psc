Algoritmo Ejercicio_d
	//Calcular el salario de los trabajadores de una empresa
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//20/2/2023
	
	//Definicion Variables
	Definir a,z,Total_Horas,h,Valor_HoraD Como Entero;
	Definir Incremento,Descuento,Valor_HoraN,Salario_Base,Salario_Final,Salario Como Real;
	Definir Nombre Como Caracter;
	
	//Declaracion de variables y Entradas
	Nombre<-n;
	Escribir "Nombre de usuario ";
	Leer Nombre;
	Escribir "Numero de Horas Diurnas Trabajadas ";
	Leer a;
	Escribir "Numero de Horas Nocturnas Trabajadas ";
	Leer z;
	Total_Horas<-(a+z);
	Escribir "Total de Horas Trabajadas ", Total_Horas;
	Escribir "Valor Horas Diurnas Trabajadas ";
	Leer h;
	
	//Procesos
	Valor_HoraD<-(a*h);
	Escribir "Pago por Horas Diurnas ", Valor_HoraD;
	Incremento<-1.40;
	Valor_HoraN<-(z*h)*Incremento;
	Escribir "Pago por Horas Nocturnas ", Valor_HoraN;
	Salario_Base<-(Valor_HoraD+Valor_HoraN);
	Escribir "El Salario Base fue de ", Salario_Base;
	Descuentos<-0.19;
	Salario<-(Salario_Base*Descuentos);
	Salario_Final<-(Salario_Base-Salario);
	
	//Salidas
	Escribir "El Salario Final fue de ", Salario_Final;
	
	FinAlgoritmo
