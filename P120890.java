public class P120890 {
    public int solution(int[] array, int n) {
        int min = 9999999;
        int[] gap = new int[array.length];
        for (int i=0; i<gap.length; i++) {
            int dif = n >= array[i] ? n - array[i] : array[i] - n;
            gap[i] = dif;
            if (dif < min) min = dif;
        }
        int answer = 9999999;
        for (int i=0; i<gap.length; i++) {
            if (gap[i] == min) {
                if (array[i] < answer) answer = array[i];
            }
        }
        
        return answer != 9999999 ? answer : -1;
    }
}
