/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_15.java."

import java.io.*;

public class ejercicio_15 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		double a;
		double b;
		double ecud;
		double ecup1;
		double ecup2;
		String j;
		double x;
		String z;
		// Resolucion de una ecuacion de primer grado
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 5/3/2023
		// Definicion de variables
		// Declaracion de variables
		x = x;
		a = z;
		b = j;
		// Entradas, Procesos y Salidas
		System.out.println("La Ecuacion Principal es ax+b=0 ");
		System.out.println("Digite el valor de a: ");
		a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite el valor de b: ");
		b = Double.parseDouble(bufEntrada.readLine());
		if (a<0) {
			ecup1 = (-b/a);
			System.out.println("Al despejar la ecuacion queda asi: x= -b/-a ");
			System.out.println("El resultado de la ecuacion fue de x= "+ecup1);
		} else {
			if (b<0) {
				ecup2 = (b/a);
				System.out.println("Al despejar la ecuacion queda asi: x= b/a ");
				System.out.println("El resultado de la ecuacion fue de x= "+ecup2);
			} else {
				if (a==0) {
					System.out.println("La ecuacion es una Indeterminacion");
				} else {
					ecud = (-b/a);
					System.out.println("Al despejar la ecuacion queda asi: x= -b/a ");
					System.out.println("El resultado de la ecuacion fue de x= "+ecud);
				}
			}
		}
	}


}

