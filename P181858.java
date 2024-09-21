import java.util.ArrayList;
import java.util.Arrays;

public class P181858 {
    public int[] solution(int[] arr, int k) {
        int[] visited = new int[100001];
        Arrays.fill(visited, 0);
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int num : arr) {
            if (visited[num] == 0 && result.size() < k) {
                visited[num] = 1;
                result.add(num);
            }
        }
        
        while (result.size() < k) {
            result.add(-1);
        }
        
        int[] answer = new int[result.size()];
        for (int i=0; i<answer.length; i++) answer[i] = result.get(i);
        
        return answer;

    }
}
