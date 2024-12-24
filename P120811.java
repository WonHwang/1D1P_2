import java.util.Arrays;

public class P120811 {
        public int solution(int[] array) {
        Arrays.sort(array);
        int n = array.length/2;
        return array[n];
    }
}
