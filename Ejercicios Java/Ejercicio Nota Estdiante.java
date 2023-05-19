/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_NOTA_ESTUDIANTE.java."

import java.io.*;

public class ejercicio_nota_estudiante {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		String a;
		String h;
		String i;
		String n;
		double n1;
		double n2;
		double n3;
		String nombre;
		double nota1;
		double nota2;
		double nota3;
		int numero_inasistencias;
		double porcentaje1;
		double porcentaje2;
		double promedio;
		String z;
		// Calcula nota final estudiante
		// Version 1.0
		// Deszarrollado por Santiago Gomez
		// 28/2/2023
		// Definicion de variables
		// Declaracion de variables
		nombre = i;
		nota1 = n;
		nota2 = z;
		nota3 = h;
		numero_inasistencias = a;
		porcentaje1 = 0.35;
		porcentaje2 = 0.3;
		// Entradas
		System.out.println("Nombre de Usuario: ");
		nombre = bufEntrada.readLine();
		System.out.println("Digite la primera Nota: ");
		nota1 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite la segunda Nota: ");
		nota2 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Digite la tercera Nota: ");
		nota3 = Double.parseDouble(bufEntrada.readLine());
		System.out.println("Numero de Inasistencias: ");
		numero_inasistencias = Integer.parseInt(bufEntrada.readLine());
		// Procesos y Salidas
		n1 = (nota1*porcentaje1);
		n2 = (nota2*porcentaje1);
		n3 = (nota3*porcentaje2);
		if ((numero_inasistencias>=12)) {
			System.out.println(nombre+" Reprobo la materia");
		} else {
			promedio = (n1+n2+n3);
			System.out.println(nombre+" su promedio fue de: "+promedio);
		}
		if ((promedio>=3.5)) {
			System.out.println(nombre+" Aprobo la materia");
		} else {
			System.out.println(nombre+" Reprobo la materia con promedio de: "+promedio);
		}
	}


}

