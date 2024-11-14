class P12936 {
    public int[] solution(int n, long k) {
        int[] answer = new int[n];
        long[] fac = new long[21];
        fac[1] = 1;
        for (int i=2; i<21; i++) fac[i] = fac[i-1] * i;
        
        int[] nums = new int[n];
        for (int i=0; i<n; i++) nums[i] = i+1;
        
        int idx = 0;
        
        while (nums.length > 0) {
            if (nums.length == 1) {
                answer[idx++] = nums[0];
                break;
            }
            
            long a, b;
            a = fac[nums.length-1];
            b = fac[nums.length];
            
            for (int i=nums.length; i>=0; i--) {
                if (i*a <= k && k <= b) {
                    if (i*a == k) {
                        if (i == 0) {
                            answer[idx++] = nums[nums.length-1];
                            nums[nums.length-1] = -1;
                        }
                        else {
                            answer[idx++] = nums[i-1];
                            nums[i-1] = -1;
                        }
                    }
                    else {
                        answer[idx++] = nums[i];
                        nums[i] = -1;
                    }
                    k -= i*a;
                    int[] newNums = new int[nums.length-1];
                    int j = 0;
                    for (int x=0; x<nums.length; x++) {
                        if (nums[x] != -1) newNums[j++] = nums[x];
                    }
                    nums = newNums;
                    break;
                }
            }
        } 
        return answer;
    }
}