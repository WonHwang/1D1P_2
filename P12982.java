import java.util.*;

public class P12982 {
    public int solution(int[] d, int budget) {
        int answer = d.length;
        int total = 0;
        for (int i=0; i<d.length; i++) total += d[i];
        Arrays.sort(d);
        for (int i=d.length-1; i>=0; i--) {
            if (total <= budget) break;
            total -= d[i];
            answer -= 1;
        }
        return answer;
    }
}
