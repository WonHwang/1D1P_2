import java.util.ArrayDeque;

public class P250136 {
    int[] dx = new int[] {1, -1, 0, 0};
    int[] dy = new int[] {0, 0, 1, -1};
    
    public int solution(int[][] land) {
        
        int n = land.length;
        int m = land[0].length;
        int[] answer = new int[m];
        int[][] visited = new int[n][m];
        for (int j=0; j<m; j++) {
            for (int i=0; i<n; i++) {
                if (land[i][j] != 0 && visited[i][j] == 0) {
                    ArrayDeque<int[]> queue = new ArrayDeque<>();
                    queue.add(new int[] {i, j});
                    visited[i][j] = 1;
                    int cnt = 0;
                    int l = j;
                    int r = j;
                    
                    while (!queue.isEmpty()) {
                        int[] node = queue.pollFirst();
                        cnt += 1;
                        int a = node[0];
                        int b = node[1];
                        if (b < l) l = b;
                        if (b > r) r = b;
                        
                        for (int k=0; k<4; k++) {
                            int x = a + this.dx[k];
                            int y = b + this.dy[k];
                            
                            if (0 <= x && x < n && 0 <= y && y < m && visited[x][y] == 0 && land[x][y] != 0) {
                                visited[x][y] = 1;
                                queue.add(new int[] {x, y});
                            }
                        }
                    }
                    for (int k=l; k<r+1; k++) answer[k] += cnt;
                }
            }
        }
        int Max = 0;
        for (int i=0; i<answer.length; i++) if (answer[i] > Max) Max = answer[i];
        return Max;
    }
}
