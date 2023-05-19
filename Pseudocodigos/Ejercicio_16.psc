Algoritmo Ejercicio_16
	//Calcular la nomina semanal de un trabajador
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//5/3/2023
	
	//Definicion de variables
	Definir Nombre Como Caracter
	Definir Incremento,Impuesto1,Impuesto2,Salario_I,Salario_Total,Salario_IP1,Salario_IP2,Salario_IP3,Salario_IP4,Salario_T1,Salario_T2,Salario_T3,Salario_T4 Como Real
	Definir Numero_Horas,Valor_Horas,Salario_B,Horas_Extra Como Entero
	
	//Declaracion de variables
	Nombre<-n;
	Numero_Horas<-d;
	Valor_Horas<-b;
	Incremento<-1.5;
	Impuesto1<-0.2;
	Impuesto2<-0.3;
	
	//Entradas
	Escribir "Digite Nombre de usuario:";
	Leer Nombre;
	Escribir "Total de Horas Trabajadas: ";
	Leer Numero_Horas;
	Si Numero_Horas<0 Entonces
		Escribir "Valor no valido"
		
	SiNo
		Escribir "Valor por las Horas Trabajadas: ";
		Leer Valor_Horas;
	Fin Si
	Salario_B<-(Numero_Horas*Valor_Horas);
    
	//Procesos y Salidas
	Si Numero_Horas<=35 Entonces
		Salario_B<-(Numero_Horas*Valor_Horas);
		
		Escribir Nombre " su Salario Base fue de: ", Salario_B " Euros";
	SiNo
		Horas_Extra<-Numero_Horas-35
		Salario_I<-(Horas_Extra*Valor_Horas*Incremento);
		Salario_Total<-(35*Valor_Horas)+Salario_I;
		Escribir Nombre " su Salario Total fue de: ", Salario_Total " Euros";
	Fin Si
	Si Salario_B<=2000 Entonces
		Si Salario_Total<=2000 Entonces
			Escribir Nombre " su Salario no tuvo aplicacion de impuestos";
		SiNo
			Si Salario_Total>2000 y Salario_Total<=2220  Entonces
				Salario_I<-Salario_Total-2000
				Salario_IP1<-Salario_I*Impuesto1
				Salario_T1<-Salario_Total-Salario_IP1
				Escribir Nombre " su Salario Final con aplicacion de Impuestos es de: ",Salario_T1 " Euros";
			SiNo
				Si Salario_Total>2220 Entonces
					Salario_I<-(220*Impuesto1) + Salario_Total-2220*Impuesto2
					Salario_IP2<-Salario_I*Impuesto2
					Salario_T2<-Salario_Total-Salario_IP2
					Escribir "su Salario Final con aplicacion de Impuestos fue de: ", Salario_T2 " Euros";
				Fin Si
			Fin Si
		Fin Si
	SiNo
		Si Salario_B>2000 y Salario_B<=2220 Entonces
			Salario_I<-Salario_Total-2000
			Salario_IP3<-Salario_I*Impuesto1
			Salario_T3<-Salario_B-Salario_IP3
			Escribir Nombre " su Salario Final con Aplicacion de Impuestos fue de: ",Salario_T3 " Euros";
		SiNo
			Si Salario_B>2220 Entonces;
				Salario_I<-(220*Impuesto1) + Salario_Total-2220*Impuesto2
				Salario_IP4<-Salario_I*Impuesto2
				Salario_T4<-Salario_B-Salario_IP4
				Escribir Nombre " su Salario Final con aplicacion de Impuestos fue de: ",Salario_T4 " Euros";
			Fin Si
		Fin Si
	Fin Si
	
	
FinAlgoritmo
