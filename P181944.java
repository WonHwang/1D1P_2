import java.util.Scanner;

public class P181944 {
        public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] oe = {"even", "odd"};
        System.out.println(n + " is " + oe[n%2]);
    }
}
