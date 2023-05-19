/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_4.java."

import java.io.*;

public class ejercicio_4 {

	public static void main(String args[]) {
		int a;
		double aceleracion;
		double conversor;
		double tiempo_aceleracion;
		int vf;
		int vi;
		// Calcular el tiempo que tardara un cuerpo en alcanzar una velocidad de 144 k/h
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 14/2/2023
		// Definicion de variables
		// Declaracion de variables
		vf = 144;
		vi = 12;
		aceleracion = 2;
		conversor = (vf/3.6);
		// Entradas
		System.out.println("Velocidad Final "+vf);
		System.out.println("Velocidad Final convertida a m/s "+conversor);
		System.out.println("Velocidad Inicial "+vi+" m/s");
		System.out.println("Aceleracion "+aceleracion+" m/s^2");
		// Procesos
		tiempo_aceleracion = (conversor-12)/aceleracion;
		// Salidas
		System.out.println("El Tiempo de Aceleracion fue de "+tiempo_aceleracion+" m/s^2");
	}


}

