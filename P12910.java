import java.util.ArrayList;
import java.util.Arrays;

public class P12910 {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int num : arr) {
            if (num%divisor == 0) list.add(num);
        }
        if (list.size() == 0) list.add(-1);
        int[] answer = new int[list.size()];
        for (int i=0; i<list.size(); i++) answer[i] = list.get(i);
        Arrays.sort(answer);
        return answer;
    }
}
