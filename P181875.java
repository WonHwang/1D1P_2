public class P181875 {
    public String[] solution(String[] strArr) {
        String[] answer = new String[strArr.length];
        for (int i=0; i<strArr.length; i++) {
            String string = strArr[i];
            if (i%2 == 1) answer[i] = string.toUpperCase();
            else answer[i] = string.toLowerCase();
        }
        return answer;
    }
}
