public class P120921 {
    public int solution(String A, String B) {
        int len = A.length();
        int answer = 0;
        while (true) {
            if (A.equals(B)) break;
            if (answer > len) break;
            answer++;
            A = A.charAt(len-1) + A.substring(0, len-1);
        }
        if (answer > len) answer = -1;
        return answer;
    }
}
