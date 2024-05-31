public class P120848 {
    public int solution(int n) {
        int answer = 0;
        int[] factorial = new int[11];
        factorial[1] = 1;
        for (int i=2; i<11; i++) factorial[i] = i*factorial[i-1];
        for (int i=10; i>0; i--) {
            if (n >= factorial[i]) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}
