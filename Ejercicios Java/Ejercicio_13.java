/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_13.java."

import java.io.*;
import java.math.*;

public class ejercicio_13 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double a;
		double b;
		double c;
		double ecu1;
		double ecu2;
		double v;
		// Algoritmo para resolver una ecuacion de segundo grado AX2+BX+C
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 12/3/2023
		// Definicion de variables
		// Declaracion de variables
		a = a;
		b = b;
		c = c;
		// Entradas
		System.out.println("Resolucion de la ecuacion de segundo grado Ax^2+Bx+C");
		System.out.println("Digite el valor de la variable A");
		a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite el valor de la variable B");
		b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite el valor de la variable C");
		c = Double.parseDouble(bufEntrada.readLine());
		// Procesos y Salidas
		if (a==0) {
			System.out.println("La ecuacion es una indeterminacion");
		} else {
			v = Math.sqrt(b*b)-4*a*c;
			if (v>0) {
				ecu1 = -b+(v)/(2*a);
				ecu2 = -b-Math.sqrt(v)/(2*a);
				System.out.println("Para resolver la ecuacion se usa la formula -b+-RC(b*b-4ac)/2a ");
				System.out.println("El primer Valor de x fue de: "+ecu1);
				System.out.println("El segundo Valor de x fue de: "+ecu2);
			} else {
				if (v<0) {
					ecu1 = -b/(2*a);
					System.out.println("Para resolver la ecuacion se usa la formula -b/2a ");
					System.out.println("El primer Valor de x fue de: "+ecu1);
				}
			}
		}
	}


}

