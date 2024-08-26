public class P181900 {
    public boolean contain(int[] arr, int x) {
        for (int y : arr) if (y == x) return true;
        return false;
    }
    public String solution(String my_string, int[] indices) {
        String answer = "";
        for (int i=0; i<my_string.length(); i++) {
            if (!contain(indices, i)) answer += my_string.charAt(i);
        }
        return answer;
    }
}
