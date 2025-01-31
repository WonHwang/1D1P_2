import java.util.HashMap;

public class P120861 {
    int[] dx = new int[] {-1, 1, 0, 0};
    int[] dy = new int[] {0, 0, 1, -1};
    
    public int[] solution(String[] keyinput, int[] board) {
        
        HashMap<String, Integer> direc = new HashMap<>();
        direc.put("left", 0);
        direc.put("right", 1);
        direc.put("up", 2);
        direc.put("down", 3);
        
        int N = board[0]/2;
        int M = board[1]/2;
        
        int a = 0;
        int b = 0;
        
        for (String k : keyinput) {
            int x = a + this.dx[direc.get(k)];
            int y = b + this.dy[direc.get(k)];
            
            if (-N <= x && x <= N && -M <= y && y <= M) {
                a = x;
                b = y;
            }
        }
        return new int[] {a, b};
    }
}
