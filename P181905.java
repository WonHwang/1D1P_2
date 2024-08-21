public class P181905 {
    public String getReverse(String str) {
        String result = "";
        for (int i=str.length()-1; i>=0; i--) result += str.charAt(i);
        return result;
    }
    public String solution(String my_string, int s, int e) {
        String answer = "";
        answer = my_string.substring(0, s) + getReverse(my_string.substring(s, e+1)) + my_string.substring(e+1);
        return answer;
    }
}
