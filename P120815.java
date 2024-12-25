public class P120815 {
    public int getGcd(int a, int b) {
        if (b > a) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        
        while (b > 0) {
            int tmp = b;
            b = a%b;
            a = tmp;
        }
        
        return a;
    }
    public int solution(int n) {
        int x = getGcd(n, 6);
        return n*6/x/6;
    }
}
