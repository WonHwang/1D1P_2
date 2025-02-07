class P120829 {
    public int solution(int angle) {
        int[] x = new int[] {1, 3};
        int[] y = new int[] {0, 2, 4};
        if (angle%90 > 0) return x[angle/90];
        else return y[angle/90];
    }
}