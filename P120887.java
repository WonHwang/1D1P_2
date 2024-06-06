public class P120887 {
    public int solution(int i, int j, int k) {
        int answer = 0;
        for (int a=i; a<=j; a++) {
            answer += count(a, k);
        }
        return answer;
    }
    public int count(int n, int k) {
        int result = 0;
        while (n > 0) {
            if (n%10 == k) result += 1;
            n /= 10;
        }
        return result;
    }
}