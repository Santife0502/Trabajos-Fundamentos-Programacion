/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_8.java."

import java.io.*;

public class ejercicio_8 {

	public static void main(String args[]) {
		int num;
		int suma;
		// Calcular la suma de los pares del 2 al 100
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 28/2/2023
		// Definicion de variables
		// Declaracion de variables
		suma = 2;
		num = 4;
		// Procesos
		while ((num<=100)) {
			suma = (suma+num);
			num = (num+2);
		}
		// Salidas
		System.out.println("Suma pares entre 2 y 100= "+suma);
	}


}

