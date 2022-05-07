import java.util.Scanner;

public class ex3_java {
	public static void main(String[] args) {

		int num;
		Scanner input = new Scanner(System.in);
		input.close();

		System.out.print("Insira um número: ");
		num = input.nextInt();
		
		int result = num % 2;

		if (result != 0) {
			System.out.println(num + " IMPAR");
		} else {
			System.out.println(num + " PAR");
		}
		
	}
}
// ! End