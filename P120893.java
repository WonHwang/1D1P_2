public class P120893 {
    public String solution(String my_string) {
        String answer = "";
        for (int i=0; i<my_string.length(); i++) {
            char x = my_string.charAt(i);
            if ('a' <= x && x <= 'z') answer += (char) (x - 'a' + 'A');
            else answer += (char) (x - 'A' + 'a');
        }
        return answer;
    }
}
