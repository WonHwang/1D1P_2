class P120846 {
    public int solution(int n) {
        int answer = 0;
        
        int[] sieve = new int[101];
        for (int i=0; i<101; i++) sieve[i] = 1;
        sieve[0] = 0;
        sieve[1] = 0;
        for (int i=4; i<101; i+=2) sieve[i] = 0;
        
        for (int i=3; i<101; i+=2) {
            if (sieve[i] == 1) {
                for (int j=2*i; j<101; j+=i) sieve[j] = 0;
            }
        }
        
        for (int i=2; i<n+1; i++) {
            if (sieve[i] == 0) answer += 1;
        }
        return answer;
    }
}