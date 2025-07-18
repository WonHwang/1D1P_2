import java.util.*;

public class P12980 {
    public int solution(int n) {
        int ans = 0;
        
        while (n > 0) {
            if (n%2 != 0) {
                n--;
                ans++;
            }
            n /= 2;
        }
        return ans;
    }
}
