class P120924 {
    public int solution(int[] common) {
        int answer = 0;
        int a = common[0];
        int b = common[1];
        int c = common[2];
        
        if (2*b == a+c) {
            int d = b-a;
            answer = common[common.length-1] + d;
        }
        
        else if (b*b == a*c) {
            int r = b / a;
            answer = common[common.length-1] * r;
        }
        
        return answer;
    }
}