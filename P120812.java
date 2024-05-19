public class P120812 {
    class Solution {
        public int solution(int[] array) {
            int answer = 0;
            int max = 0;
            int[] count = new int[1001];
            for (int i=0; i<array.length; i++) count[array[i]]++;
            for (int i=0; i<1001; i++) {
                if (count[i] > max) {
                    max = count[i];
                    answer = i;
                }
            }
            
            int maxCount = 0;
            for (int i=0; i<1001; i++) {
                if (count[i] == max) maxCount += 1;
            }
            
            if (maxCount > 1) answer = -1;
            return answer;
        }
    }
}