public class P120814 {
    public int solution(int n) {
        int answer = 1;
        if (n%7==0) answer = 0;
        answer += n/7;
        return answer;
    }
}
