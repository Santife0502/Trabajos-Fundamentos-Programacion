/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_17.java."

import java.io.*;
import java.math.*;

public class ejercicio_17 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		String a;
		double area;
		String b;
		String c;
		double lado_a;
		double lado_b;
		double lado_c;
		double perimetro;
		double semi_perimetro;
		// Calcular el Area de un triangulo conociendo sus lados
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 5/3/2023
		// Definicion de variables
		// Declaracion de variables
		lado_a = a;
		lado_b = b;
		lado_c = c;
		// Entradas y procesos
		System.out.println("Digite el valor del primer lado:");
		lado_a = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite el valor del segundo lado:");
		lado_b = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite el valor del tercer lado:");
		lado_c = Double.parseDouble(bufEntrada.readLine());
		perimetro = (lado_a+lado_b+lado_c);
		System.out.println("El perimetro del triangulo fue de: "+perimetro);
		semi_perimetro = (perimetro/2);
		System.out.println("El Semi Perimetro fue de: "+semi_perimetro);
		area = Math.sqrt(semi_perimetro)*(semi_perimetro-lado_a)*(semi_perimetro-lado_b)*(semi_perimetro-lado_c);
		// Salidas
		System.out.println("El Area del Triangulo fue de: "+area);
	}


}

