import java.util.*;

public class P181866 {
    public String[] solution(String myString) {
        String[] string = myString.split("x");
        Arrays.sort(string);
        int cnt = 0;
        for (String x:string) {
            if (!x.equals("")) cnt += 1; 
        }
        String[] answer = new String[cnt];
        int idx = 0;
        for (String x:string) {
            if (!x.equals("")) answer[idx++] = x;
        }
        return answer;
    }
}
