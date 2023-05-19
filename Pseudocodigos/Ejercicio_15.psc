Algoritmo Ejercicio_15
	//Resolucion de una ecuacion de primer grado
	//Version 1.0
	//Desarrollado por Santiago Gomez
	//5/3/2023
	
	//Definicion de variables
	Definir x,a,b,EcuD,EcuP1,EcuP2 Como Real;
	//Declaracion de variables
	a<-z;
	b<-j;
	
	//Entradas, Procesos y Salidas
	Escribir "La Ecuacion Principal es ax+b=0 ";
	Escribir "Digite el valor de a: ";
	Leer a;
	Escribir "Digite el valor de b: ";
	Leer b;
	Si a<0 Entonces
		EcuP1<-(-b/a);
		Escribir "Al despejar la ecuacion queda asi: x= -b/a ";
		Escribir "El resultado de la ecuacion fue de x= ", EcuP1;
	SiNo
		Si b<0 Entonces
			EcuP2<-(b/a);
			Escribir "Al despejar la ecuacion queda asi: x= b/a ";
			Escribir "El resultado de la ecuacion fue de x= ", EcuP2;
		SiNo
			Si a=0 Entonces
				Escribir "La ecuacion es una Indeterminacion";
			SiNo
				EcuD<-(-b/a);
				Escribir "Al despejar la ecuacion queda asi: x= -b/a ";
				Escribir "El resultado de la ecuacion fue de x= ",EcuD;
			Fin Si
		Fin Si
	FinSi
FinAlgoritmo
