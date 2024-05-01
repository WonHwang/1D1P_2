public class P12926 {
    public String solution(String s, int n) {
        String answer = "";
        for (int i=0; i<s.length(); i++) {
            char digit = s.charAt(i);
            if ('a' <= digit && digit <= 'z') {
                digit -= 'a';
                digit += n;
                digit %= 26;
                digit += 'a';
            }
            else if ('A' <= digit && digit <= 'Z') {
                digit -= 'A';
                digit += n;
                digit %= 26;
                digit += 'A';
            }
            answer += digit;
        }
        return answer;
    }
}