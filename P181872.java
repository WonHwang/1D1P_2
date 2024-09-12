public class P181872 {
    public String getReverse(String str) {
        String result = "";
        for (int i=0; i<str.length(); i++) result = str.charAt(i) + result;
        return result;
    }
    public String solution(String myString, String pat) {
        String answer = getReverse(myString);
        pat = getReverse(pat);
        int idx = answer.indexOf(pat);
        answer = answer.substring(idx, answer.length());
        answer = getReverse(answer);
        return answer;
    }
}
