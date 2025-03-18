import java.util.Arrays;

public class P120889 {
        public int solution(int[] sides) {
        Arrays.sort(sides);
        int answer = sides[0] + sides[1] > sides[2] ? 1 : 2;
        return answer;
    }
}
