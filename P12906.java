import java.util.*;

public class P12906 {
    public int[] solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        for (int i=0; i<arr.length; i++) {
            if (stack.isEmpty()) stack.add(arr[i]);
            else {
                if (stack.peek() == arr[i]) continue;
                else stack.add(arr[i]);
            }
        }

        int[] answer = new int[stack.size()];
        int idx = stack.size()-1;
        while (!stack.isEmpty()) answer[idx--] = stack.pop();

        return answer;
    }
}
