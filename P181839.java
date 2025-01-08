class P181839 {
    public int abs(int a, int b) {
        return a >= b ? a-b : b-a;
    }
    public int solution(int a, int b) {
        return a%2 != 0 || b%2 != 0 ? (a%2 != 0 && b%2 != 0 ? a*a+b*b : 2*a+2*b) : abs(a, b);
    }
}
