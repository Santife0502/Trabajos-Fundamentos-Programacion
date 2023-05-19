/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "PRACTICA_CONDICIONAL1.java."

import java.io.*;

public class practica_condicional1 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int v_mayor;
		int v_numero2;
		int v_numuno;
		// Leer 2 numeros e informar cual es el mayor
		// Version 1.0
		// Desarrollado por: Santiago Gomez
		// 27/02/2023
		// Area de definicion de variable
		// Inicializar Variables
		v_numuno = 0;
		v_numero2 = 0;
		v_mayor = 0;
		// Entradas
		System.out.println("Digite el primer numero: ");
		v_numuno = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Digite el segundo numero: ");
		v_numero2 = Integer.parseInt(bufEntrada.readLine());
		// Procesos
		if (v_numuno==v_numero2) {
			System.out.println(" No hay numero mayor, los dos son iguales");
		} else {
			if (v_numuno>v_numero2) {
				v_mayor = v_numuno;
			} else {
				v_mayor = v_numero2;
			}
			System.out.println("El numero mayor es:"+v_mayor);
		}
	}


}

