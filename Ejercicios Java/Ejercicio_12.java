/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_12.java."

import java.io.*;

public class ejercicio_12 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int cantidad_numn;
		int producto;
		int resultado;
		// Calcular el producto de los n primeros numeros naturales
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 3/32023
		// Definicion de variables
		// Declaracion de variables
		cantidad_numn = 1;
		producto = 0;
		resultado = 1;
		// Entradas y procesos
		System.out.println("Digite Numeros Naturales que se van a multiplicar, al poner 0 se realiza la operacion  ");
		while (cantidad_numn>0) {
			System.out.println("Digite numero");
			cantidad_numn = Integer.parseInt(bufEntrada.readLine());
			if (cantidad_numn>0) {
				resultado = cantidad_numn*resultado;
				producto = resultado;
			} else {
				if (cantidad_numn<0) {
					System.out.println("Numero no valido");
				}
			}
		}
		// Salidas
		if (cantidad_numn==0) {
			System.out.println("El producto fue de: "+producto);
		}
	}


}

