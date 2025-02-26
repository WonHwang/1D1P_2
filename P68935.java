class P68935 {
    public int solution(int n) {
        int answer = 0;
        String result = "";
        
        while (n > 0) {
            result += Integer.toString(n%3);
            n /= 3;
        }
        
        int tmp = 1;
        for (int i=result.length()-1; i>=0; i--) {
            char digit = result.charAt(i);
            answer += Character.getNumericValue(digit) * tmp;
            tmp *= 3;
        }
        return answer;
    }
}