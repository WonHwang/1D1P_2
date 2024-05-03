public class P12940 {
    public int[] solution(int n, int m) {
        int g = gcd(n, m);
        int[] answer = {g, n*m/g};
        return answer;
    }
    
    public int gcd(int a, int b) {
        if (b > a) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        
        while (b > 0) {
            int tmp = a;
            a = b;
            b = tmp%b;
        }
        
        return a;
    }
}
