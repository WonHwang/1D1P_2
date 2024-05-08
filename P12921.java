class P12921 {
    public int solution(int n) {
        int answer = 0;
        for (int i=2; i<=n; i++) {
            if (isPrime(i)) answer += 1;
        }
        return answer;
    }
    public boolean isPrime(int x) {
        if (x == 2) return true;
        if (x%2 == 0) return false;
        
        for (int i=3; i<=(int) Math.sqrt(x)+1; i+=2) {
            if (x%i == 0) return false;
        }
        return true;
    }
}