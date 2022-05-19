import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        // Declaração de variáveis
        double num;
        double somatorio;
        double x;
        double delta;
        double y1;
        double y2;
        double area;
        double pi;

        // Entrada
        Scanner input = new Scanner(System.in);
        num = input.nextDouble();

        // Inicialização de variáveis
        somatorio = 0;
        x = 0;
        delta = 1 / num;

        // Processamento
        while (x < 1) {
            y1 = 1 / (1 + (Math.pow(x,2)));
            x = x + delta;
            y2 = 1 / (1 + (Math.pow(x,2)));
            area = ((y1 + y2) / 2) * delta;
            somatorio = somatorio + area;
        }

        pi = somatorio * 4;

        // Saída
        System.out.println(pi);

        input.close();
    }
}
