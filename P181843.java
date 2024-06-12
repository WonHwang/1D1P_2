public class P181843 {
    public int solution(String my_string, String target) {
        if (my_string.equals(target)) return 1;
        for (int i=0; i<my_string.length()-target.length()+1; i++) {
            if (my_string.substring(i, i+target.length()).equals(target)) return 1;
        }
        return 0;
    }
}
