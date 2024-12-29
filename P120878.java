import java.util.ArrayList;

public class P120878 {
        public int solution(int a, int b) {
        int answer = 1;
        for (int i=2; i<1001; i++) {
            if (a%i == 0 && b%i == 0) {
                while (true) {
                    if (a%i != 0 || b%i != 0) break;
                    a /= i;
                    b /= i;
                }
            }
        }
        
        if (b == 1) return 1;
        ArrayList<Integer> div = new ArrayList<>();
        for (int i=2; i<b+1; i++) {
            if (b%i == 0) {
                while (true) {
                    if (b%i != 0) break;
                    div.add(i);
                    b /= i;
                }
            }
        }
        
        for (int i=0; i<div.size(); i++) {
            int num = div.get(i);
            if (num != 2 && num != 5) {
                answer = 2;
                break;
            }
        }
        return answer;
    }
}
