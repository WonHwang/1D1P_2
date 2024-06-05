public class P181902 {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        for (int i=0; i<my_string.length(); i++) {
            char s = my_string.charAt(i);
            if ('A' <= s && s <= 'Z') answer[(int) s - 'A'] += 1;
            else answer[(int) s - 'a' + 26] += 1;
        }
        return answer;
    }
}
