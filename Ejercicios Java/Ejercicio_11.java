/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_11.java."

import java.io.*;

public class ejercicio_11 {

	public static void main(String args[]) {
		int num;
		int suma;
		// Calcular la suma de los primeros 50 numeros enteros
		// Version 1.0
		// Desarrollado por Santiago Gomez 
		// 3/3/2023
		// Definicion de variables
		// Declaracion de variables
		suma = 1;
		num = 2;
		// Entradas y procesos
		while (num<=50) {
			suma = (suma+num);
			num = (num+1);
		}
		// Salidas
		System.out.println("La suma de los primeros 50 numeros enteros es de: "+suma);
	}


}

