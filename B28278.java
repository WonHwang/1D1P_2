import java.util.LinkedList;
import java.util.List;
import java.io.*;

public class B28278 {
    public static void main(String[] args) throws IOException{
        List<String> stack = new LinkedList<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        for (int i=0; i<N; i++) {
            String[] line = br.readLine().split(" ");
            
            switch(line[0]) {
                case "1":
                stack.add(line[1]);
                break;

                case "2":
                if (stack.size() > 0) {
                    bw.write(stack.get(stack.size()-1));
                    stack.remove(stack.size()-1);
                }
                else {
                    bw.write("-1");
                }
                bw.newLine();
                break;

                case "3":
                bw.write(String.valueOf(stack.size()));
                bw.newLine();
                break;

                case "4":
                if (stack.size() > 0) bw.write("0");
                else bw.write("1");
                bw.newLine();
                break;

                case "5":
                if (stack.size() > 0) bw.write(stack.get(stack.size()-1));
                else bw.write("-1");
                bw.newLine();
                break;
            }
        }
        bw.close();
    }
}