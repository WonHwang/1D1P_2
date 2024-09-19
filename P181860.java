import java.util.ArrayDeque;

public class P181860 {
    public int[] solution(int[] arr, boolean[] flag) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int i=0; i<arr.length; i++) {
            if (flag[i]) {
                for (int j=0; j<arr[i]*2; j++) queue.push(arr[i]);
            }
            else {
                for (int j=0; j<arr[i]; j++) queue.pop();
            }
        }
        int[] answer = new int[queue.size()];
        for (int i=0; i<answer.length; i++) answer[i] = queue.pollLast();
        return answer;
    }
}
