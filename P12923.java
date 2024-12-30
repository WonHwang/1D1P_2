import java.util.*;

class P12923 {
    public int getDivider(int n) {
        int res = 1;
        if (n == 1) return 0;
        for (int i=2; i<(int) Math.sqrt(n)+1; i++) {
            if (n%i == 0) {
                if (i > res) res = i;
                if (n/i <= 10000000) {
                    if (n/i > res) res = n/i;
                }
            }
        }
        return res;
    }
    public int[] solution(long begin, long end) {
        int N = Long.valueOf(end-begin).intValue()+1;
        int[] answer = new int[N];
        for (int i=0; i<N; i++) {
            int n = Long.valueOf(begin).intValue()+i;
            answer[i] = getDivider(n);
        }
        return answer;
    }
}