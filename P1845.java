import java.util.HashSet;

public class P1845 {
    public int solution(int[] nums) {
        int answer = 0;
        int N = nums.length / 2;
        HashSet<Integer> set = new HashSet<>();
        for (int i:nums) set.add(i);
        answer = N > set.size() ? set.size() : N;
        return answer;
    }
}
