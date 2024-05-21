public class P120875 {
    public int solution(int[][] dots) {
        if (isParel(dots[0], dots[1], dots[2], dots[3]) || isParel(dots[0], dots[2], dots[1], dots[3]) || isParel(dots[0], dots[3], dots[1], dots[2])) return 1;
        return 0;
    }
    public boolean isParel(int[] x, int[] y, int[] z, int[] w) {
        if ((x[0] - y[0]) * (z[1] - w[1]) == (x[1] - y[1]) * (z[0] - w[0])) return true;
        return false;
    }
}
