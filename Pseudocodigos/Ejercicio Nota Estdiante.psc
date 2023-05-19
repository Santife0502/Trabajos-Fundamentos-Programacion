Algoritmo Ejercicio_Nota_Estudiante
	//Calcula nota final estudiante
	//Version 1.0
	//Deszarrollado por Santiago Gomez
	//28/2/2023
	
	//Definicion de variables
	Definir Nombre Como Caracter;
	Definir Nota1,Nota2,Nota3,N1,N2,N3,Promedio,Porcentaje1,Porcentaje2 Como Real;
	Definir Numero_Inasistencias Como Entero;
	
	//Declaracion de variables
	Nombre<-i;
	Nota1<-n;
	Nota2<-z;
	Nota3<-h;
	Numero_Inasistencias<-a;
	Porcentaje1<-0.35;
	Porcentaje2<-0.3;
	
	//Entradas
	Escribir "Nombre de Usuario: ";
	Leer Nombre;
	Escribir "Digite la primera Nota: ";
	Leer Nota1;
	Escribir "Digite la segunda Nota: ";
	Leer Nota2;
	Escribir "Digite la tercera Nota: ";
	Leer Nota3;
	Escribir "Numero de Inasistencias: ";
	Leer Numero_Inasistencias;
	
	//Procesos y Salidas
	N1<-(Nota1*Porcentaje1);
	N2<-(Nota2*Porcentaje1);
	N3<-(Nota3*Porcentaje2);
	Si (Numero_Inasistencias>=12) Entonces
		Escribir Nombre " Reprobo la materia";
	SiNo
		Promedio<-(N1+N2+N3);
		Escribir Nombre " su promedio fue de: ",Promedio;
	Fin Si
	Si (Promedio>=3.5) Entonces
		Escribir Nombre " Aprobo la materia";
	SiNo
		Escribir Nombre " Reprobo la materia con promedio de: ",Promedio;
	Fin Si
	
	
FinAlgoritmo
