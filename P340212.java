class P340212 {
    public long getTime(long mid, int[] diffs, int[] times) {
        long time = 0;
        for (int i=0; i<diffs.length; i++) {
            if (diffs[i] <= mid) time += times[i];
            else time += (times[i-1] + times[i]) * (diffs[i] - mid) + times[i];
        }
        return time;
    }
    public long solution(int[] diffs, int[] times, long limit) {
        
        long start = 1;
        long end = 1000000000000000L;
        long mid = 0;
        
        while (start <= end) {
            mid = (start + end) / 2;
            long time = getTime(mid, diffs, times);
            
            if (limit < time) start = mid+1;
            else end = mid - 1;
        }
        
        if (getTime(mid, diffs, times) > limit) mid += 1;
        return mid;
    }
}