import java.util.ArrayDeque;
import java.util.Stack;

public class P64061 {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int N = board.length;
        @SuppressWarnings("unchecked")
        ArrayDeque<Integer>[] queues = new ArrayDeque[N+1];
        for (int i=0; i<N+1; i++) queues[i] = new ArrayDeque<>();

        for (int i=0; i<N; i++) {
            for (int j=0; j<N; j++) {
                if (board[j][i] != 0) {
                    queues[i+1].add(board[j][i]);
                }
            }
        }
        Stack<Integer> results = new Stack<>();

        for (int num : moves) {
            if (!queues[num].isEmpty()) {
                results.add(queues[num].poll());

                int size = results.size();
                if (size >= 2 && results.get(size-1).intValue() == results.get(size-2).intValue()) {
                    results.pop();
                    results.pop();
                    answer += 2;
                }
            }
        }

        return answer;
    }
}
