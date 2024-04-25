import java.util.*;
import java.io.*;

public class B1012 {
    public static void main (String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t=0; t<T; t++) {
            int M, N, K;
            String[] input = br.readLine().split(" ");
            M = Integer.parseInt(input[0]);
            N = Integer.parseInt(input[1]);
            K = Integer.parseInt(input[2]);
            
            int[][] grid = new int[N][M];
            
            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) grid[i][j] = 0;
            }

            for (int i=0; i<K; i++) {
                int x, y;
                input = br.readLine().split(" ");
                x = Integer.parseInt(input[0]);
                y = Integer.parseInt(input[1]);
                grid[y][x] = 1;
            }
            System.out.println(bfs(grid, N, M));
        }
    }

    public static int bfs (int[][] grid, int N, int M) {

        int[] dx = new int[] {1, -1, 0, 0};
        int[] dy = new int[] {0, 0, 1, -1};

        int cnt = 0;

        int[][] visited = new int[N][M];
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) visited[i][j] = 0;
        }

        ArrayDeque<int[]> queue = new ArrayDeque<>();

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (visited[i][j] == 0 && grid[i][j] == 1) {
                    cnt += 1;
                    visited[i][j] = cnt;
                    queue.add(new int[] {i, j});

                    while (!queue.isEmpty()) {

                        int[] node = queue.pollFirst();
                        int a = node[0];
                        int b = node[1];

                        for (int k=0; k<4; k++) {
                            int x = a + dx[k];
                            int y = b + dy[k];

                            if (0 <= x && x < N && 0 <= y && y < M && visited[x][y] == 0 && grid[x][y] == 1) {
                                visited[x][y] = cnt;
                                queue.add(new int[] {x, y});
                            }
                        }

                    }
                }
            }
        }

        return cnt;
    }
}
