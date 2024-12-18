import java.util.PriorityQueue;

class P12927 {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int work : works) {
            heap.offer(-1 * work);
        }
        
        for (int i=0; i<n; i++) {
            int Max = heap.poll();
            
            if (Max == 0) return 0;
            
            Max += 1;
            heap.offer(Max);
        }
        
        while (!heap.isEmpty()) {
            int num = heap.poll();
            answer += num*num;
        }
        return answer;
    }
}