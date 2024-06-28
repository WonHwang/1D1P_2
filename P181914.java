public class P181914 {
    public int solution(String number) {
        String answer = "";
        for (int i=0; i<number.length(); i++) {
            answer += number.charAt(i);
            answer = Integer.toString(Integer.parseInt(answer) % 9);
        }
        return Integer.parseInt(answer);
    }
}
