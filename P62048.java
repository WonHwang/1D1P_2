public class P62048 {
    public long getGcd(long a, long b) {
        long res = 1;
        for (long i=1; i<b+1; i++) {
            if (a%i == 0 && b%i == 0) res = i;
        }
        return res;
    }
    public long solution(int W, int H) {
        if (H > W) {
            int tmp = W;
            W = H;
            H = tmp;
        }
        
        long w = Long.valueOf(W);
        long h = Long.valueOf(H);
        long gcd = getGcd(w, h);
        long a = w/gcd;
        long b = h/gcd;
        long x = a*b - (a-1)*(b-1);
        long size = h/b;
        long answer = w*h - x*size;
        return answer;
    }
}
