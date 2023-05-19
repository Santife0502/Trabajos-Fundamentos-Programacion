/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_7.java."

import java.io.*;

public class ejercicio_7 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int cantidad_numeros;
		double dato;
		double media;
		double suma;
		// Calcular la media de una serie de numeros positivos cuando se coloca el 0
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 28/2/2023
		// area de inicializacion de variables//
		dato = 0;
		media = 0;
		cantidad_numeros = 0;
		suma = 0;
		// Entradas y procesos
		System.out.println("Introducir datos numericos, para calcular la media ");
		dato = Double.parseDouble(bufEntrada.readLine());
		if (dato<0) {
			System.out.println("No se ingresaron numeros positivos ");
		}
		while (dato>0) {
			if (dato>0) {
				suma = suma+dato;
				cantidad_numeros = cantidad_numeros+1;
			}
			dato = Double.parseDouble(bufEntrada.readLine());
		}
		if (dato==0) {
			media = suma/cantidad_numeros;
		}
		// Salidas
		System.out.println("La media de los numeros ingresados fue de: "+media);
	}


}

