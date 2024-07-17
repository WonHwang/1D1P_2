public class P181913 {
    public String solution(String my_string, int[][] queries) {
        for (int[] query : queries) {
            int a = query[0];
            int b = query[1];
            String sub = my_string.substring(a, b+1);
            StringBuffer str = new StringBuffer(sub);
            my_string = my_string.substring(0, a) + str.reverse().toString() + my_string.substring(b+1);
        }
        return my_string;
    }
}
