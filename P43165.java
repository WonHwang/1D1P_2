public class P43165 {

    int answer = 0;

    public int solution(int[] numbers, int target) {
        
        dfs(numbers, 0, target, 0);

        return this.answer;
    }

    public void dfs(int[] numbers, int sum, int target, int idx) {

        if (idx >= numbers.length) {
            if (sum == target) this.answer += 1;
            return;
        }

        dfs(numbers, sum + numbers[idx], target, idx+1);
        dfs(numbers, sum - numbers[idx], target, idx+1);

    }
}
