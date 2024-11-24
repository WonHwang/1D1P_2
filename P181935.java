public class P181935 {
    public int solution(int n) {
        int x = n/2;
        return n%2==1 ? (x+1)*(x+1) : 2*x*(x+1)*(2*x+1)/3;
    }
}
