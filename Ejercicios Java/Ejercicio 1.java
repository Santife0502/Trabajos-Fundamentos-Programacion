/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIOCAMION.java."

import java.io.*;

public class ejerciciocamion {

	public static void main(String args[]) {
		int aceleracion;
		int tiempo_aceleracion;
		int velocidad_final;
		int velocidad_inicial;
		// Calcular la aceleracion que tuvo un camion
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 10/2/2023
		// Area de definicion de variables
		// Declaracion de variables
		velocidad_final = 25;
		velocidad_inicial = 20;
		tiempo_aceleracion = 5;
		// Entradas
		System.out.println("Velocdad Final "+25);
		System.out.println("Velocidad Inicial "+20);
		System.out.println("Tiempo Aceleracion "+5);
		// Procesos
		aceleracion = (velocidad_final-velocidad_inicial)/tiempo_aceleracion;
		// Salidas
		System.out.println("Aceleracion total de "+aceleracion);
	}


}

