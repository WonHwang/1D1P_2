public class P12924 {
    public int solution(int n) {
        
        int answer = 0;
        int[] arr = new int[10001];
        for (int i=1; i<10001; i++) arr[i] = i*(i+1)/2;
        for (int i=1; i<n+1; i++) {
            for (int j=i-1; j>=0; j--) {
                if (arr[i] - arr[j] == n) answer += 1;
                if (arr[i] - arr[j] > n) break;
            }
        }
        return answer;
    }
}
