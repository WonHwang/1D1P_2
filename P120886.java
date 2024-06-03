import java.util.Arrays;

public class P120886 {
    public int solution(String before, String after) {
        char[] b, a;
        b = before.toCharArray();
        Arrays.sort(b);
        a = after.toCharArray();
        Arrays.sort(a);
        
        String be = new String(b);
        String af = new String(a);
        
        if (be.equals(af)) return 1;
        return 0;
    }
}
