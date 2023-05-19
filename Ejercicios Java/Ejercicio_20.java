/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_20.java."

import java.io.*;

public class ejercicio_20 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		String h;
		String j;
		String n;
		double numero1;
		double numero_1;
		double numero_2;
		double numero_3;
		// Decir cual es el numero mayor de 3 digitados (Los 3 son diferentes)
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 6/3/2023
		// Definicion de variables
		// Declaracion de variables
		numero_1 = n;
		numero_2 = j;
		numero_3 = h;
		// Entradas
		System.out.println("Digite numero 1:");
		numero_1 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite numero 2:");
		numero_2 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite numero 3:");
		numero_3 = Double.parseDouble(bufEntrada.readLine());
		// Procesos y Salidas
		if (numero_1>numero_2 && numero_1>numero_3) {
			System.out.println("El numero mayor fue: "+numero_1);
		} else {
			if (numero_2>numero1 && numero_2>numero_3) {
				System.out.println("El numero mayor fue: "+numero_2);
			} else {
				System.out.println("El numero mayor fue: "+numero_3);
			}
		}
	}


}

