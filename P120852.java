import java.util.ArrayList;

public class P120852 {
    public int[] solution(int n) {
        
        ArrayList<Integer> primes = new ArrayList<>();
        ArrayList<Integer> arr = new ArrayList<>();
        int[] prime = new int[10000];
        for (int i=0; i<10000; i++) prime[i] = 1;
        prime[0] = 0;
        prime[1] = 0;
        primes.add(2);
        for (int i=4; i<10000; i+=2) prime[i] = 0;
        for (int i=3; i<10000; i+=2) {
            if (prime[i] != 0) {
                primes.add(i);
                for (int j=2*i; j<10000; j+=i) prime[j] = 0;
            }
        }
        
        while (true) {
            if (n == 1) break;
            for (int i=0; i<primes.size(); i++) {
                int p = primes.get(i);
                if (n%p == 0) {
                    arr.add(p);
                    while (n%p == 0) n /= p;
                }
            }
        }
        
        int[] answer = new int[arr.size()];
        for (int i=0; i<answer.length; i++) answer[i] = arr.get(i);
        
        return answer;
    }
}
