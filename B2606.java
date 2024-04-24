import java.util.*;
import java.io.*;

class B2606 {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());

        int[][] grid = new int[N+1][N+1];
        for (int i=0; i<=N; i++) {
            for (int j=0; j<=N; j++) grid[i][j] = 0;
        }

        for (int i=0; i<K; i++) {
            String[] point = br.readLine().split(" ");
            int x, y;
            x = Integer.parseInt(point[0]);
            y = Integer.parseInt(point[1]);
            grid[x][y] = 1;
            grid[y][x] = 1;
        }

        ArrayDeque<Integer> queue = new ArrayDeque<>();
        int[] visited = new int[N+1];
        for (int i=0; i<=N; i++) visited[i] = 0;
        visited[1] = 1;
        queue.add(1);

        while (!queue.isEmpty()) {
            int node = queue.pollFirst();

            for (int i=2; i<=N; i++) {
                if (visited[i] == 0 && grid[node][i] == 1) {
                    visited[i] = 1;
                    queue.add(i);
                }
            }
        }

        int answer = 0;
        for (int i=2; i<=N; i++) {
            if (visited[i] == 1) answer += 1;
        }

        System.out.println(answer);
    }
}