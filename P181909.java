import java.util.Arrays;

public class P181909 {
    public String getReverse(String str) {
        String result = "";
        for (int i=str.length()-1; i>=0; i--) result += str.charAt(i);
        return result;
    }
    public String[] solution(String my_string) {
        String[] answer = new String[my_string.length()];
        my_string = getReverse(my_string);
        for (int i=0; i<my_string.length(); i++) {
            String str = my_string.substring(0, i+1);
            str = getReverse(str);
            answer[i] = str;
        }
        Arrays.sort(answer);
        return answer;
    }
}