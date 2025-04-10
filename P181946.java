import java.util.Scanner;

public class P181946 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String[] b = a.split(" ");
        System.out.println(b[0]+b[1]);
        sc.close();
    }
}