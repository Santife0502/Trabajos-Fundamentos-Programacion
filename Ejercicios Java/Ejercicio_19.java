/* Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http://pseint.sourceforge.net). */

// En java, el nombre de un archivo fuente debe coincidir con el nombre de la clase que contiene,
// por lo que este archivo deber�a llamarse "EJERCICIO_19.java."

import java.io.*;

public class ejercicio_19 {

	public static void main(String args[]) throws IOException {
		BufferedReader bufEntrada = new BufferedReader(new InputStreamReader(System.in));
		int dia1;
		int diaactual;
		int numdias;
		int resto;
		System.out.println("Ingrese el d�a de la semana en que cay� el d�a 1 del mes actual");
		System.out.println("1= Lunes");
		System.out.println("2= Martes");
		System.out.println("3= Miercoles");
		System.out.println("4= Jueves");
		System.out.println("5= Viernes");
		System.out.println("6= Sabado");
		System.out.println("7= Domingo");
		dia1 = Integer.parseInt(bufEntrada.readLine());
		System.out.println("Ingrese el n�mero de d�as transcurridos desde el d�a 1 del mes actual: ");
		numdias = Integer.parseInt(bufEntrada.readLine());
		resto = numdias%7;
		diaactual = (dia1+resto-1)%7+1;
		System.out.println("Hoy es el d�a "+diaactual+" de la semana.");
	}


}

