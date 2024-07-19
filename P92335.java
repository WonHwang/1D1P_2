public class P92335 {
    public String getKFromN(int n, int k) {
        String result = "";
        
        while (true) {
            result = Integer.toString(n%k) + result;
            n /= k;
            
            if (n == 0) break;
        }
        
        return result;
    }
    
    public boolean isPrime(long n) {
        
        if (n == 2) return true;
        if (n <= 1 || n%2 == 0) return false;
        
        for (int i=3; i<(int) Math.sqrt(n)+1; i+=2) {
            if (n%i == 0) return false;
        }
        
        return true;
    }
    public int solution(int n, int k) {
        int answer = 0;
        
        String[] splited = getKFromN(n, k).split("0");
        
        for (String num : splited) {
            if (!num.equals("")) {
                long number = Long.parseLong(num);
                if (isPrime(number)) answer += 1;
            }
        }
        return answer;
    }
}
