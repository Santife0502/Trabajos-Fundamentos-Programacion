/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_F1.java."

import java.io.*;

public class ejercicio_f1 {

	public static void main(String args[]) {
		double aceleracion;
		double conversor;
		int tiempo_aceleracion;
		int velocidad_final;
		int velocidad_inicial;
		// Calcular aceleracion de un formula 1 que parte del reposo
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 11/2/2023
		// Definicion de variables
		// Declaracion de variables
		velocidad_inicial = 0;
		// k/h
		velocidad_final = 216;
		// s
		tiempo_aceleracion = 10;
		// m/s
		conversor = (velocidad_final/3.6);
		// Entradas
		System.out.println("Velocidad inicial "+velocidad_inicial+"k/h");
		System.out.println("Velocidad Final "+velocidad_final+"k/h");
		System.out.println("Tiempo Aceleracion "+tiempo_aceleracion+"S");
		// Procesos
		aceleracion = (conversor-velocidad_inicial)/tiempo_aceleracion;
		// Salida
		System.out.println("La aceleracion es "+aceleracion+"m/s2");
	}


}

