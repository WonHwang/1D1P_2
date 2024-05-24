public class P181871 {
    public int solution(String myString, String pat) {
        int answer = 0;
        int size = pat.length();
        for (int i=0; i<myString.length()-size+1; i++) {
            if (myString.substring(i, i+size).equals(pat)) answer += 1;
        }
        return answer;
    }
}
