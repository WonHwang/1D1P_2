import java.util.Arrays;
import java.util.HashMap;

public class P120882 {
        public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        int[][] scores = new int[score.length][score[0].length];
        for (int i=0; i<score.length; i++) {
            System.arraycopy(score[i], 0, scores[i], 0, score[0].length);
        }
        
        Arrays.sort(scores, (x, y) -> y[0]+y[1]-x[0]-x[1]);
        HashMap<Integer, Integer> rank = new HashMap<>();
        int cnt = 1;
        for (int[] sc : scores) {
            if (rank.containsKey(sc[0]+sc[1]))cnt += 1;
            else {
                rank.put(sc[0]+sc[1], cnt);
                cnt += 1;
            }
        }
        for (int i=0; i<score.length; i++) answer[i] = rank.get(score[i][0]+score[i][1]);
        return answer;
    }
}
