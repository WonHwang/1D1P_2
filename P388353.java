import java.util.ArrayDeque;

class P388353 {

    public int[] dx = {1, -1, 0, 0};
    public int[] dy = {0, 0, 1, -1};

    public void bfs(String[][] grid, String target) {
        int N = grid.length;
        int M = grid[0].length;

        ArrayDeque<int[]> queue = new ArrayDeque<>();
        int[][] visited = new int[N][M];

        visited[0][0] = 1;
        queue.add(new int[] {0, 0});

        while (!queue.isEmpty()) {
            int[] node = queue.pollFirst();
            int a = node[0];
            int b = node[1];

            for (int i=0; i<4; i++) {
                int x = a + dx[i];
                int y = b + dy[i];

                if (0 <= x && x < N && 0 <= y && y < M && visited[x][y] == 0 && ("0".equals(grid[x][y]) || target.equals(grid[x][y])))
                    if ("0".equals(grid[x][y])) {
                        visited[x][y] = 1;
                        queue.add(new int[] {x, y});
                    }

                    else visited[x][y] = 2;
            }

            for (int i=0; i<N; i++) {
                for (int j=0; j<M; j++) {
                    if (visited[i][j] == 2) grid[i][j] = "0";
                }
            }
        }
    }

    public void reduce(String[][] grid, String target) {
        int N = grid.length;
        int M  = grid[0].length;

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (target.equals(grid[i][j])) grid[i][j] = "0";
            }
        }
    }
    public int solution(String[] storage, String[] requests) {
        int answer = 0;
        int N = storage.length;
        int M = storage[0].length();
        String[][] grid = new String[N+2][M+2];
        for (String[] grid1 : grid) {
            for (int j = 0; j<grid[0].length; j++) {
                grid1[j] = "0";
            }
        }
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                grid[i+1][j+1] = Character.toString(storage[i].charAt(j));
            }
        }

        for (String request : requests) {
            if (request.length() == 2) reduce(grid, Character.toString(request.charAt(0)));
            else bfs(grid, request);
        }

        for (int i=0; i<N+2; i++) {
            for (int j=0; j<M+2; j++) {
                if (!"0".equals(grid[i][j])) answer += 1;
            }
        }
        return answer;
    }
}