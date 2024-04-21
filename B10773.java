import java.util.Stack;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class B10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Stack<Integer> stack = new Stack<>();
        int K = Integer.parseInt(br.readLine());
        for (int i=0; i<K; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) stack.pop();
            else stack.add(num);
        }
        int answer = 0;
        while (!stack.isEmpty()) answer += stack.pop();
        br.close();
        bw.write(String.valueOf(answer)+"\n");
        bw.close();
    }
}