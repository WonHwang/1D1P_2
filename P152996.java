class P152996 {
    public long solution(int[] weights) {
        long answer = 0;
        int[] cand = new int[1001];
        for (int weight : weights) cand[weight] += 1;
        int[] target = {2, 3, 4};
        
        for (int i=100; i<=1000; i++) {
            for (int j=i; j<=1000; j++) {
                if (i == j) answer += (long) cand[i]*(cand[i]-1)/2;
                else {
                    for (int a : target) {
                        for (int b : target) {
                            if (a*i == b*j) {
                                answer += (long) cand[i]*cand[j];   
                            }
                        }
                    }
                }
            }
        }
        return answer;
    }
}