Algoritmo Ejercicio_17
	//Calcular el Area de un triangulo conociendo sus lados
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//5/3/2023
	
	//Definicion de variables
	Definir Lado_a,Lado_b,Lado_c,Perimetro,Semi_Perimetro,Area Como Real;
	
	//Declaracion de variables
	Lado_a<-a;
	Lado_b<-b;
	Lado_c<-c;
	
	//Entradas y procesos
	Escribir "Digite el valor del primer lado:";
	Leer Lado_a;
	Escribir "Digite el valor del segundo lado:";
	Leer Lado_b;
	Escribir "Digite el valor del tercer lado:";
	Leer Lado_c;
	Perimetro<-(Lado_a+Lado_b+Lado_c);
	Escribir "El perimetro del triangulo fue de: ", Perimetro;
	Semi_Perimetro<-(Perimetro/2);
	Escribir "El Semi Perimetro fue de: ",Semi_Perimetro;
	Area<-RC (Semi_Perimetro)*(Semi_Perimetro-Lado_a)*(Semi_Perimetro-Lado_b)*(Semi_Perimetro-Lado_c);
	
	//Salidas
	Escribir "El Area del Triangulo fue de: ", Area;
FinAlgoritmo
