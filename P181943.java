public class P181943 {
    public String solution(String my_string, String overwrite_string, int s) {
        int x = s + overwrite_string.length();
        return my_string.substring(0, s) + overwrite_string + my_string.substring(x);
    }
}
