import java.util.ArrayList;

public class P181901 {
        public int[] solution(int n, int k) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int x=1; x<=n; x++) {
            if (x%k == 0) arr.add(x);
        }
        int[] answer = new int[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        return answer;
    }
}
