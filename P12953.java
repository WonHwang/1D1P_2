class P12953 {
    public int getGcd(int a, int b) {
        while (b > 0) {
            int tmp = b;
            b = a%b;
            a = tmp;
        }
        
        return a;
    }
    public int solution(int[] arr) {
        int answer = arr[0];
        
        if (arr.length > 1) {
            for (int i=1; i<arr.length; i++) {
                answer = answer * arr[i] / getGcd(answer, arr[i]);
            }
        }
        return answer;
    }
}