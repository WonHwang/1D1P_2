public class P181834 {
    public String solution(String myString) {
        String answer = "";
        for (int i=0; i<myString.length(); i++) {
            char digit = myString.charAt(i);
            if (digit < 'l') answer += "l";
            else answer += digit;
        }
        return answer;
    }
}
