import java.util.ArrayList;
import java.util.Arrays;

public class P120907 {
    public static String[] solution(String[] quiz) {
        ArrayList<String> arr = new ArrayList<>();
        ArrayList<String> ex = new ArrayList<>();
        ArrayList<Integer> res = new ArrayList<>();
        
        for (String q : quiz) {
            String[] tmp = q.split("=");
            System.out.println(Arrays.toString(tmp));
            ex.add(tmp[0].trim());
            res.add(Integer.valueOf(tmp[1].trim()));
        }
        
        for (int i=0; i<ex.size(); i++) {
            String e = ex.get(i);
            String[] tmp = e.split("\\ \\+\\ ");
            System.out.println(Arrays.toString(tmp));
            if (tmp.length > 1) {
                int a = Integer.parseInt(tmp[0].trim());
                int b = Integer.parseInt(tmp[1].trim());
                if (a + b == res.get(i)) arr.add("0");
                else arr.add("X");
            }
            else {
                tmp = e.split("\\ \\-\\ ");
                System.out.println(Arrays.toString(tmp));
                int a = Integer.parseInt(tmp[0].trim());
                int b = Integer.parseInt(tmp[1].trim());
                if (a - b == res.get(i)) arr.add("0");
                else arr.add("X");
            }
        }
        String[] answer = new String[arr.size()];
        for (int i=0; i<answer.length; i++) answer[i] = arr.get(i);
        return answer;
    }

    public static void main(String[] args) {
        String[] quiz = new String[] {"5 + 6 = 11"};
        System.out.println(Arrays.toString(solution(quiz)));
    }
}
