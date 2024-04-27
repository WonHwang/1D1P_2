public class P77884 {
    public int solution(int left, int right) {
        int answer = 0;
        for (int i=left; i<=right; i++) {
            if (countDivider(i)) answer += i;
            else answer -= i;
        }
        return answer;
    }
    public boolean countDivider(int n) {
        boolean result = true;
        for (int i=1; i<=n; i++) if (n%i == 0) result = !result;
        return result;
    }   
}