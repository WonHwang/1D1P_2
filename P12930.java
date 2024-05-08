public class P12930 {
    public String solution(String s) {
        String answer = "";
        boolean capital = true;
        
        for (int i=0; i<s.length(); i++) {
            char digit = s.charAt(i);
            if (digit == ' ') {
                capital = true;
                answer += " ";
            }
            else {
                if (capital) answer += Character.toUpperCase(digit);
                else answer += Character.toLowerCase(digit);
                capital = !capital;
            }
        }
        
        return answer;
    }
}