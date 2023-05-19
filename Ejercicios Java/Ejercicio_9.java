/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_9.java."

import java.io.*;

public class ejercicio_9 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		String h;
		double incremento;
		String n;
		String nombre;
		int numero_horas;
		int salario;
		double salario2;
		double salario_incremento;
		int valor_horas;
		String z;
		// Calcular el salario de un trabajador segun el numero de horas trabajadas y el valor de las horas, y si pasa de 40 horas se tiene un incremento de 1.5 la hora adicional
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 28/2/2023
		// Definicion de variables
		// Declaracion de variables
		nombre = n;
		numero_horas = z;
		valor_horas = h;
		incremento = 1.5;
		// Entradas y Procesos
		System.out.println("Nombre de Usuario: ");
		nombre = bufEntrada.readLine();
		System.out.println("Numero de Horas Trabajadas: ");
		numero_horas = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Valor Horas Trabajadas: ");
		valor_horas = Integer.parseInt(bufEntrada.readLine());
		salario = (numero_horas*valor_horas);
		salario2 = (salario*incremento);
		salario_incremento = (salario+salario2);
		// Salidas
		if ((numero_horas>40)) {
			System.out.println(nombre+" su salario del trabajador con horas extraordinarias fue de: "+salario_incremento);
		} else {
			System.out.println(nombre+" su salario del trabajador fue de: "+salario);
		}
	}


}

