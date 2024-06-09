import java.util.*;
import java.lang.Math;

public class P120897 {
    public Integer[] solution(int n) {
        List<Integer> arr = new ArrayList<Integer>();
        Integer[] answer = {};
        for (int i=1; i<(int) Math.sqrt(n)+1; i++) {
            if (n%i == 0) {
                arr.add(i);
                if (i != n/i) arr.add(n/i);
            }
        }
        answer = arr.toArray(answer);
        Arrays.sort(answer);

        return answer;
    }
}
