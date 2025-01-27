public class P120843 {
    public int solution(int[] numbers, int k) {
        int idx = 0;
        for (int i=0; i<k-1; i++) {
            idx = (idx + 2) % numbers.length;
        }
        return idx+1;
    }
}
