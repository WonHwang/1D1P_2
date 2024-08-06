public class P181930 {
    public int solution(int a, int b, int c) {
        int answer = 0;
        
        if (a == b && b == c) answer = (a*a*a + b*b*b + c*c*c) * (a*a + b*b + c*c) * (a + b + c);
        
        else if (a != b && b != c && c != a) answer = a + b + c;
        
        else answer = (a*a + b*b + c*c) * (a + b + c);
        
        return answer;
    }
}
