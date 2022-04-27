//! Import Libraries
import java.util.Scanner;

public class ex3_java {
	public static void main(String[] args) {

		// ! Variable Declaration
		try (Scanner input = new Scanner(System.in)) {
			int num;

			// ! Input
			System.out.print("Insert a number here: ");
			num = input.nextInt();

			// ! Data Processment + Output
			int result = num % 2;

			if (result != 0) {
				System.out.println(num + " IMPAR");
			} else {
				System.out.println(num + " PAR");
			}
		}
	}
}
// ! End