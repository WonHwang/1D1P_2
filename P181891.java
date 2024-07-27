import java.util.ArrayDeque;

public class P181891 {
    public int[] solution(int[] num_list, int n) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        for (int num : num_list) queue.add(num);
        for (int i=0; i<num_list.length-n; i++) {
            queue.addFirst(queue.pollLast());
        }

        int[] answer = new int[queue.size()];
        for (int i=0; i<answer.length; i++) {
            answer[i] = queue.pollFirst();
        }
        
        return answer;
    }
}
