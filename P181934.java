class P181934 {
    public int solution(String ineq, String eq, int n, int m) {
        int answer = 0;
        if (">".equals(ineq)) {
            if ("=".equals(eq)) answer = n >= m ? 1 : 0;
            else answer = n > m ? 1 : 0;
        }
        else {
            if ("=".equals(eq)) answer = n <= m ? 1 : 0;
            else answer = n < m ? 1 : 0;
        }
        
        return answer;
    }
}