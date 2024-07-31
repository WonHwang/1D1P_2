public class P68936 {
    public int[] dfs(int x, int y, int size, int[][] arr) {
        int zero = 0;
        int one = 0;
        for (int i=x; i<x+size; i++) {
            for (int j=y; j<y+size; j++) {
                if (arr[i][j] == 1) one += 1;
                else zero += 1;
            }
        }
        
        if (zero == 0) return new int[] {0, 1};
        else if (one == 0) return new int[] {1, 0};
        
        int resO = 0;
        int resZ = 0;
        
        int[] tmp = dfs(x, y, size/2, arr);
        int a = tmp[0];
        int b = tmp[1];
        resZ += a;
        resO += b;
        
        tmp = dfs(x+(size/2), y, size/2, arr);
        a = tmp[0];
        b = tmp[1];
        resZ += a;
        resO += b;
        
        tmp = dfs(x, y+(size/2), size/2, arr);
        a = tmp[0];
        b = tmp[1];
        resZ += a;
        resO += b;
        
        tmp = dfs(x+(size/2), y+(size/2), size/2, arr);
        a = tmp[0];
        b = tmp[1];
        resZ += a;
        resO += b;
        
        return new int[] {resZ, resO};
    }
    public int[] solution(int[][] arr) {
        int[] answer = dfs(0, 0, arr.length, arr);
        return answer;
    }
}
