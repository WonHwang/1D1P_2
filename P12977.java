public class P12977 {
    int answer = 0;
    boolean[] sieve = new boolean[3001];

    public int solution(int[] nums) {

        this.sieve[0] = false;
        this.sieve[1] = false;
        this.sieve[2] = true;
        for (int i=4; i<3001; i+=2) this.sieve[i] = false;
        for (int i=3; i<3001; i+=2) this.sieve[i] = true;
        for (int i=3; i<3001; i+=2) {
            if (this.sieve[i]) {
                for (int j=2*i; j<3001; j+=i) this.sieve[j] = false;
            }
        }

        dfs(nums, 0, 0, 0);

        return this.answer;
    }

    public void dfs(int[] nums, int idx, int depth, int total) {
        
        if (depth == 3) {
            if (this.sieve[total]) this.answer += 1;
            return;
        }

        if (depth > 3 || idx == nums.length) return;

        dfs(nums, idx+1, depth+1, total+nums[idx]);
        dfs(nums, idx+1, depth, total);
    }
}
