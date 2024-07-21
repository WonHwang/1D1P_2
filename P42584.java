public class P42584 {
    public int[] solution(int[] prices) {
        
        int length = prices.length;
        int[] answer = new int[length];
        
        for (int i=0; i<length; i++) {
            int tmp = 0;
            for (int j=i; j<length; j++) {
                if (prices[i] > prices[j] || j == length-1) {
                    answer[i] = tmp;
                    break;
                }
                else tmp += 1;
            }
        }
        answer[length-1] = 0;
        return answer;
    }
}
