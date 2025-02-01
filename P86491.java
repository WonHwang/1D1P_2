public class P86491 {
    public int solution(int[][] sizes) {
        int answer = 0;
        int w = 0;
        int h = 0;
        for (int[] size : sizes) {
            int W = size[0];
            int H = size[1];
            
            if (H > W) {
                int tmp = H;
                H = W;
                W = tmp;
            }
            
            if (W > w) w = W;
            if (H > h) h = H;
        }
        
        answer = w*h;
        return answer;
    }
}
