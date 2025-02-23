import java.util.HashMap;

public class P389478 {
    public int solution(int n, int w, int num) {
        int answer = 0;
        HashMap<Integer, Integer> warehouse = new HashMap<>();
        int order = 1;

        for (int i=1; i<n+1; i++) {
            warehouse.put(i, order);
            if (i%w == 0) continue;
            if ((i/w)%2 != 0) order -= 1;
            else order += 1;
        }

        int target = warehouse.get(num);
        for (int i=num; i<=n; i++) {
            if (warehouse.get(i) == target) answer += 1;
        }
        return answer;
    }
}
