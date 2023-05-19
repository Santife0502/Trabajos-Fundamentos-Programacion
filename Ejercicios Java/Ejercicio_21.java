/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_21.java."

import java.io.*;
import java.math.*;

public class ejercicio_21 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double a;
		double b;
		double c;
		double ecu1;
		double ecu2;
		double i;
		double r;
		double v;
		// Resolver una ecuación de segundo grado, dando soluciones con números imaginarios
		// desarrollado por Santiago Gomez
		// Version 1.0
		// 12/3/2023
		// Definicion de variables
		// Entradas
		System.out.println("Ingresa el valor de A: ");
		a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Ingresa el valor de B: ");
		b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Ingresa el valor de C: ");
		c = Double.parseDouble(bufEntrada.readLine());
		// Procesos y Salidas
		while (a==0) {
			System.out.println("Es una indeterminacion ");
		}
		if (a!=0) {
			v = (b*b)-4*a*c;
			if (v==0) {
				ecu1 = -b/(2*a);
				ecu2 = -b/(2*a);
				System.out.println("El primer Valor de x fue de: "+ecu1);
				System.out.println("El segundo Valor de x fue de: "+ecu2);
			} else {
				if (v>0) {
					ecu1 = -b+Math.sqrt((b*b)-4*a*c)/(2*a);
					ecu2 = -b-Math.sqrt((b*b)-4*a*c)/(2*a);
					System.out.println("El primer Valor de x fue de: "+ecu1);
					System.out.println("El segundo Valor de x fue de: "+ecu2);
				} else {
					if (v<0) {
						i = Math.sqrt(Math.abs(-v/(2*a)));
						r = -b/(2*a);
						System.out.println(r+" + "+i+" imaginario");
						System.out.println(r+" - "+i+" imaginario");
					}
				}
			}
		}
	}


}

