Algoritmo Ejercicio_21
	
	//Resolver una ecuación de segundo grado, dando soluciones con números imaginarios
	//desarrollado por Santiago Gomez
	//Version 1.0
	//12/3/2023
	
	//Definicion de variables
	Definir A,B,C,Ecu1,Ecu2,R,V,i Como Real;
	
	//Entradas
	Escribir "Ingresa el valor de A: ";
	Leer A;
	Escribir "Ingresa el valor de B: ";
	Leer B;
	Escribir "Ingresa el valor de C: ";
	Leer C;
	//Procesos y Salidas
	Mientras A = 0 Hacer
		Escribir "Es una indeterminacion ";
	FinMientras
	Si a <> 0 Entonces
		V = (B * B) - 4 * A * C;
		Si V = 0 Entonces
			Ecu1 = -B / (2 * A);
			Ecu2 = -B / (2 * A);
			Escribir "El primer Valor de x fue de: ",Ecu1;
			Escribir "El segundo Valor de x fue de: ",Ecu2;
		SiNo
			Si V > 0 Entonces
				Ecu1 = -B + RC ( (B * B)  - 4 * A * C) / (2 * A);
				Ecu2 = -B - RC ( (B * B) - 4 * A * C) / (2 * A);
				Escribir "El primer Valor de x fue de: ",Ecu1;
				Escribir "El segundo Valor de x fue de: ",Ecu2;
				
			SiNo
				Si V < 0 Entonces
					i = RC (abs(-V / (2 * A) ) );
					R = -B / (2 * A);
					Escribir R " + " I " imaginario";
					Escribir R " - " I " imaginario";
		
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo