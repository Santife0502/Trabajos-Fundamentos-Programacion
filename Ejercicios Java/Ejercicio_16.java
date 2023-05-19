/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_16.java."

import java.io.*;

public class ejercicio_16 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		String b;
		String d;
		double impuesto1;
		double impuesto2;
		double incremento;
		String n;
		String nombre;
		int numero_horas;
		int salario_b;
		double salario_i;
		double salario_im1;
		double salario_im2;
		double salario_ti1;
		double salario_ti2;
		double salario_total;
		int valor_horas;
		// Calcular la nomina semanal de un trabajador
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 5/3/2023
		// Definicion de variables
		// Declaracion de variables
		nombre = n;
		numero_horas = d;
		valor_horas = b;
		incremento = 1.5;
		impuesto1 = 0.2;
		impuesto2 = 0.3;
		// Entradas
		System.out.println("Digite Nombre de usuario:");
		nombre = bufEntrada.readLine();
		System.out.println("Total de Horas Trabajadas: ");
		numero_horas = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Valor por las Horas Trabajadas: ");
		valor_horas = Integer.parseInt(bufEntrada.readLine());
		salario_b = (numero_horas*valor_horas);
		// Procesos y Salidas
		if (numero_horas<=35) {
			salario_b = (numero_horas*valor_horas);
			System.out.println(nombre+" su Salario Base fue de: "+salario_b+" Euros");
		} else {
			salario_i = (salario_b*incremento);
			salario_total = (salario_b+salario_i);
			System.out.println(nombre+" su Salario Total fue de: "+salario_total+" Euros");
		}
		if (salario_b<=2000) {
			if (salario_total<=2000) {
				System.out.println(nombre+" su Salario no tuvo aplicacion de impuestos");
			} else {
				if (salario_total==2220) {
					salario_ti1 = (salario_total*impuesto1);
					System.out.println(nombre+" su Salario Final con aplicacion de Impuestos es de: "+salario_ti1+" Euros");
				} else {
					if (salario_total>2220) {
						salario_ti2 = (salario_total*impuesto2);
						System.out.println("su Salario Final con aplicacion de Impuestos fue de: "+salario_ti2+" Euros");
					}
				}
			}
		} else {
			if (salario_b==2220) {
				salario_im1 = (salario_b*impuesto1);
				System.out.println(nombre+" su Salario Final con Aplicacion de Impuestos fue de: "+salario_im1+" Euros");
			} else {
				if (salario_b>2220) {
					salario_im2 = (salario_b*impuesto2);
					System.out.println(nombre+" su Salario Final con aplicacion de Impuestos fue de: "+salario_im2+" Euros");
				}
			}
		}
	}


}

