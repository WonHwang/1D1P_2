public class P132267 {
    public int solution(int a, int b, int n) {
        int answer = 0;
        while (n > 0) {
            if (n < a) break;
            int tmp = n / a * b;
            n %= a;
            answer += tmp;
            n += tmp;
        }
        return answer;
    }
}
