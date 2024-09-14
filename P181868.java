public class P181868 {
    public String[] solution(String my_string) {
        my_string = my_string.replaceAll("\\s+", " ");
        if (my_string.charAt(0) == ' ') my_string = my_string.substring(1);
        if (my_string.charAt(my_string.length()-1) == ' ') my_string = my_string.substring(0, my_string.length());
        return my_string.split(" ");
    }
}
