public class P389479 {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int[] servers = new int[24];
        for (int i=0; i<24; i++) {
            if (players[i] >= (servers[i]+1)*m) {
                int over = (players[i] - (servers[i]+1)*m) / m;
                over += 1;
                for (int j=i; j<i+k; j++) {
                    if (j < 24) servers[j] += over;
                }
                answer += over;
            }
        }
        return answer;
    }
}