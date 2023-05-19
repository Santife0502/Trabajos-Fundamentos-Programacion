/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_6.java."

import java.io.*;

public class ejercicio_6 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		String h;
		String i;
		String n;
		String nombre;
		int numero_horas;
		int salario_base;
		int salario_final;
		double salario_tasas;
		double tasas;
		int valor_hora;
		// Calcular el salario de un trabajador
		// Version1.0
		// Desarrollado por Santiago Gomez
		// 27/2/2023
		// Definicion de variables
		// Declaracion de variables
		nombre = i;
		numero_horas = h;
		valor_hora = n;
		tasas = 0.25;
		// Entradas y Procesos
		System.out.println("Digite Nombre de Usuario: ");
		nombre = bufEntrada.readLine();
		System.out.println("El numro de horas trabajadas fue de: ");
		numero_horas = Integer.parseInt(bufEntrada.readLine());
		System.out.println("El Valor por las horas trabajadas fue de: ");
		valor_hora = Integer.parseInt(bufEntrada.readLine());
		salario_base = (valor_hora*numero_horas);
		System.out.println("El Salario Base es de: "+salario_base);
		salario_tasas = (salario_base*tasas);
		System.out.println("El salario con la aplicacion de Tasas de Interes es de: "+salario_tasas);
		salario_final = (salario_base-salario_tasas);
		// Salidas
		System.out.println(nombre+" Su Salario Final fue de: "+salario_final);
	}


}

