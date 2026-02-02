import java.util.Scanner;

public class Methods {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter units consumed: ");
        int units = scanner.nextInt();

        int bill = 0;

        if (units <= 100) {
            bill = units * 10;
        } else if (units <= 200) {
            bill = (100 * 10) + ((units - 100) * 15);
        } else if (units <= 300) {
            bill = (100 * 10) + (100 * 15) + ((units - 200) * 20);
        } else {
            bill = (100 * 10) + (100 * 15) + (100 * 20) + ((units - 300) * 25);
        }

        System.out.println("Total Electricity Bill: ₹" + bill);
    }
}
