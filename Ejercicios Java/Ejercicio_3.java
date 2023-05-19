/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo debería llamarse "EJERCICIO_3.java."

import java.io.*;

public class ejercicio_3 {

	public static void main(String args[]) {
		double aceleracion;
		int distancia_recorrido;
		int tiempo;
		double variable_operacion;
		int velocidad_final;
		int velocidad_inicial;
		// Calcular la aceleracion y distancia recorrida de una locomotora
		// Version 1.0
		// Desarrollado por Santiago Gomez
		// 12/2/2023
		// Definicion de variables
		// Declaracion de variables
		velocidad_final = 25;
		velocidad_inicial = 0;
		tiempo = 10;
		variable_operacion = 1/2;
		// Entradas
		System.out.println("Velocidad Final "+velocidad_final);
		System.out.println("Velocidad Inicial "+velocidad_inicial);
		System.out.println("Tiempo de Aceleracion "+tiempo);
		// Procesos
		aceleracion = (velocidad_final-velocidad_inicial)/tiempo;
		distancia_recorrido = (variable_operacion*velocidad_final)*tiempo;
		// Salidas
		System.out.println("La Aceleracion fue de "+aceleracion);
		System.out.println("La Distancia Recorrida fue de "+distancia_recorrido);
	}


}

