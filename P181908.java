public class P181908 {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        int x, y;
        x = my_string.length();
        y = is_suffix.length();
        if (x >= y && my_string.substring(x-y, x).equals(is_suffix)) answer = 1;
        return answer;
    }
}
