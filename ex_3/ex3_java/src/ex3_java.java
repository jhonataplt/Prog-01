// Leia SOMENTE um número inteiro e imprima uma mensagem //
// contendo o número e um texto: PAR, se o número lido for //
// divisível por 2 ou exclusivo IMPAR, se o número lido não for //
// divisível por 2. //

import java.util.Scanner;

public class ex3_java {
	public static void main(String[] args) {

		// Declaração de Varáveis
		int num;
		Scanner input = new Scanner(System.in);
		
		// Entrada
		System.out.print("Insira um número: ");
		num = input.nextInt();
		
		// Processamento + Saída
		int result = num % 2;

		if (result != 0) {
			System.out.println(num + " IMPAR");
		} else {
			System.out.println(num + " PAR");
		}
		input.close();
	}
}
// ! End