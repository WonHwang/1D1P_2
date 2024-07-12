public class P12985 {
    public int solution(int n, int a, int b) {
        int answer = 0;
        
        while (true) {
            answer += 1;
            
            a = (a+1)/2;
            b = (b+1)/2;
            
            if (a == b) break;
        }
        return answer;
    }
}
