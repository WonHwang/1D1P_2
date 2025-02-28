import java.util.ArrayDeque;
import java.util.ArrayList;

class P49189 {
    public int solution(int n, int[][] edge) {
        
        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] info = new ArrayList[n+1];
        for (int i=0; i<n+1; i++) {
            info[i] = new ArrayList<>();
        }
        
        for (int[] e : edge) {
            int x = e[0];
            int y = e[1];
            info[x].add(y);
            info[y].add(x);
        }
        
        int[] visited = new int[n+1];
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.offer(1);
        visited[1] = 1;
        
        while (!queue.isEmpty()) {
            int node = queue.poll();
            int step = visited[node];
            
            for (int i=0; i<info[node].size(); i++) {
                int v = info[node].get(i);
                if (visited[v] == 0) {
                    queue.offer(v);
                    visited[v] = step + 1;
                }
            }
        }
        
        int max = 0;
        for (int i=0; i<n+1; i++) {
            if (visited[i] > max) max = visited[i];
        }
        int answer = 0;
        for (int v : visited) if (v == max) answer += 1;
        
        return answer;
    }
}