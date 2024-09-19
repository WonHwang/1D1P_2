import java.util.ArrayDeque;

public class P181859 {
    public int[] solution(int[] arr) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        int idx = 0;
        while (idx < arr.length) {
            if (queue.isEmpty()) queue.push(arr[idx]);
            else if (arr[idx] == queue.peek()) queue.pop();
            else queue.push(arr[idx]);
            idx += 1;
        }

        if (queue.isEmpty()) queue.push(-1);
        int[] answer = new int[queue.size()];
        for (int i=0; i<answer.length; i++) answer[i] = queue.pollLast();
        return answer;
    }
}