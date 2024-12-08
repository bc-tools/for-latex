import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Qui êtes-vous ? ");

        String name = scanner.nextLine().trim();

        if (name.isEmpty()) {
            System.out.println("Ah, pas très bavard aujourd'hui !");

        } else {
            System.out.println("Bonjour " + name + ".");
            System.out.println("Épatant ! En fait, pas du tout...");
        }

        scanner.close();
    }
}
