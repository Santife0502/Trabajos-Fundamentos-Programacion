/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_10.java."

import java.io.*;

public class ejercicio_10 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int incremento;
		int ma;
		int minutos;
		int valor_m;
		int valor_m2;
		// Calcular el valor de una llamada Telefonica
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 3/3/2023
		// Definicion de variables
		// Declaracion de variables
		minutos = 0;
		valor_m = 10;
		incremento = 5;
		// Entradas,procesos y salidas
		System.out.println("Digite la cantidad de Minutos: ");
		minutos = Integer.parseInt(bufEntrada.readLine());
		if (minutos>0) {
			if (minutos<3) {
				System.out.println("El valor de la llamada fue de: "+valor_m+" Centimos");
			} else {
				ma = minutos-2;
				valor_m2 = valor_m+(ma*incremento);
				System.out.println("El valor de llamada fue de: "+valor_m2+" Centimos");
			}
		} else {
			System.out.println("ERROR");
		}
	}


}

