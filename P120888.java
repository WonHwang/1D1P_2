import java.util.HashSet;

public class P120888 {
    public String solution(String my_string) {
        String answer = "";
        HashSet<Character> set = new HashSet<>();
        for (int i=0; i<my_string.length(); i++) {
            char c = my_string.charAt(i);
            if (!set.contains(c)) {
                set.add(c);
                answer += c;
            }
        }
        return answer;
    }
}
