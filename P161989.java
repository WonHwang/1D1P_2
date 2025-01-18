public class P161989 {
    public int solution(int n, int m, int[] section) {
        int answer = 1;
        int idx = 0;
        int i = 0;
        while (true) {
            if (section[i] > section[idx]+m-1) {
                answer += 1;
                idx = i;
            }
            
            if (i == section.length-1) break;
            i += 1;
        }
        return answer;
    }
}
