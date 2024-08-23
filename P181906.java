public class P181906 {
    public int solution(String my_string, String is_prefix) {
        String tmp = "";
        if (is_prefix.length() > my_string.length()) return 0;
        for (int i=0; i<is_prefix.length(); i++) tmp += my_string.charAt(i);
        return is_prefix.equals(tmp) ? 1 : 0;
    }
}
