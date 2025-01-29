import java.util.Scanner;

public class P181949 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        for (int i=0; i<a.length(); i++) {
            char d = a.charAt(i);
            if ('a' <= d && d <= 'z') d = (char) ((int) d - (int) 'a' + (int) 'A');
            else if ('A' <= d && d <= 'Z') d = (char) ((int) d - (int) 'A' + (int) 'a');
            System.out.print(d);
        }
        System.out.println();
        sc.close();
    }    
}
