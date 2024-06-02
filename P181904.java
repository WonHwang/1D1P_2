public class P181904 {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        int idx = c-1;
        while (true) {
            if (idx >= my_string.length()) break;
            answer += my_string.charAt(idx);
            idx += m;
        }
        return answer;
    }
}
