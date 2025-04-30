import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class B2083 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String line = br.readLine();
            if ("# 0 0".equals(line)) break;
            String[] splittedLine = line.split(" ");
            String name = splittedLine[0];
            String stringAge = splittedLine[1];
            String stringWeight = splittedLine[2];
            int age = Integer.parseInt(stringAge);
            int weight = Integer.parseInt(stringWeight);

            if (age > 17 || weight >= 80) System.out.println(name + " Senior");
            else System.out.println(name + " Junior");
        }
        br.close();
    }
}