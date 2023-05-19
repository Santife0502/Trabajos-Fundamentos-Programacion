/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_18.java."

import java.io.*;

public class ejercicio_18 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int num_dia;
		String x;
		// Leida una fecha decir el dia de la semana suponiendo que el dia 1 del mes fue lunes
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 8/3/2023
		// Definicion de variables
		// Declaracion de variables
		num_dia = x;
		// Entradas
		System.out.println("Digite una Fecha");
		num_dia = Integer.parseInt(bufEntrada.readLine());
		// Procesos y salidas
		switch (num_dia) {
		case 1: case 8: case 15: case 22: case 29:
			System.out.println("El dia fue Lunes");
			break;
		case 2: case 9: case 16: case 23: case 30:
			System.out.println("El dia fue martes");
			break;
		case 3: case 10: case 17: case 24: case 31:
			System.out.println("El dia fue miercoles");
			break;
		case 4: case 11: case 18: case 25:
			System.out.println("El dia fue jueves");
			break;
		case 5: case 12: case 19: case 26:
			System.out.println("El dia fue viernes");
			break;
		case 6: case 13: case 20: case 27:
			System.out.println("El dia fue sabado");
			break;
		case 7: case 14: case 21: case 28:
			System.out.println("El dia fue domingo");
			break;
		default:
			System.out.println("Digito un dato invalido");
		}
	}


}

