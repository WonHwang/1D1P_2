import java.util.*;

public class P120896 {
    public String solution(String s) {
        String answer = "";
        HashMap<Character, Integer> dict = new HashMap<>();
        for (int i=0; i<s.length(); i++) {
            char digit = s.charAt(i);
            if (!dict.containsKey(digit)) dict.put(digit, 1);
            else dict.put(digit, dict.get(digit)+1);
        }
        for (char c:dict.keySet()) {
            if (dict.get(c) == 1) answer += c;
        }
        char[] chars = answer.toCharArray();
        Arrays.sort(chars);
        answer = new String(chars);
        return answer;
    }
}
