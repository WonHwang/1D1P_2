public class P120871 {
    public int solution(int n) {
        int answer = 0;
        for (int i=1; i<n+1; i++) {
            answer += 1;
            while (answer%3 == 0 || Integer.toString(answer).indexOf('3') >= 0) answer += 1;
        }
        return answer;
    }
}
