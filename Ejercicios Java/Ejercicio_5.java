/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_D.java."

import java.io.*;

public class ejercicio_d {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int a;
		double descuento;
		double descuentos;
		int h;
		double incremento;
		String n;
		String nombre;
		double salario;
		double salario_base;
		double salario_final;
		int total_horas;
		int valor_horad;
		double valor_horan;
		int z;
		// Calcular el salario de los trabajadores de una empresa
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 20/2/2023
		// Definicion Variables
		// Declaracion de variables y Entradas
		nombre = n;
		System.out.println("Nombre de usuario ");
		nombre = bufEntrada.readLine();
		System.out.println("Numero de Horas Diurnas Trabajadas ");
		a = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Numero de Horas Nocturnas Trabajadas ");
		z = Integer.parseInt(bufEntrada.readLine());
		total_horas = (a+z);
		System.out.println("Total de Horas Trabajadas "+total_horas);
		System.out.println("Valor Horas Diurnas Trabajadas ");
		h = Integer.parseInt(bufEntrada.readLine());
		// Procesos
		valor_horad = (a*h);
		System.out.println("Pago por Horas Diurnas "+valor_horad);
		incremento = 1.40;
		valor_horan = (z*h)*incremento;
		System.out.println("Pago por Horas Nocturnas "+valor_horan);
		salario_base = (valor_horad+valor_horan);
		System.out.println("El Salario Base fue de "+salario_base);
		descuentos = 0.19;
		salario = (salario_base*descuentos);
		salario_final = (salario_base-salario);
		// Salidas
		System.out.println("El Salario Final fue de "+salario_final);
	}


}

