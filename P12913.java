import java.util.*;

public class P12913 {
    int solution(int[][] land) {
        int answer = 0;
        
        int N = land.length;
        int[][] dp = new int[N][4];
        for (int i=0; i<4; i++) {
            dp[0][i] = land[0][i];
        }
        for (int i=1; i<N; i++) {
            for (int j=0; j<4; j++) {
                LinkedList<Integer> tmp = new LinkedList<>();
                for (int k=0; k<4; k++) {
                    if (j != k) tmp.add(dp[i-1][k]);
                }
                dp[i][j] = Collections.max(tmp) + land[i][j];
            }
        }
        answer = dp[N-1][0];
        for (int i=0; i<dp[N-1].length; i++) {
            if (dp[N-1][i] > answer) answer = dp[N-1][i];
        }
        return answer;
    }
}
