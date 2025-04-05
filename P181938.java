class P181938 {
    public int solution(int a, int b) {
        String A = Integer.toString(a);
        String B = Integer.toString(b);
        int ab = Integer.parseInt(A+B);
        int ab2 = 2*a*b;
        return ab>=ab2?ab:ab2;
    }
}