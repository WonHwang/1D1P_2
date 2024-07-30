public class P181942 {
    public String solution(String str1, String str2) {
        String answer = "";
        for (int i=0; i<2*str1.length(); i++) {
            answer += i%2 == 1 ? str2.charAt(i/2) : str1.charAt(i/2);
        }
        return answer;
    }
}
