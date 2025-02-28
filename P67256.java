import java.util.ArrayDeque;
import java.util.HashMap;

public class P67256 {
    int[] dx = new int[] {1, -1, 0, 0};
    int[] dy = new int[] {0, 0, 1, -1};
    String[] leftSide = new String[] {"1", "4", "7"};
    String[] rightSide = new String[] {"3", "6", "9"};
    
    HashMap<String, int[]> target = new HashMap<>();
    public void setTarget() {
        this.target.put("0", new int[] {3, 1});
        this.target.put("1", new int[] {0, 0});
        this.target.put("2", new int[] {0, 1});
        this.target.put("3", new int[] {0, 2});
        this.target.put("4", new int[] {1, 0});
        this.target.put("5", new int[] {1, 1});
        this.target.put("6", new int[] {1, 2});
        this.target.put("7", new int[] {2, 0});
        this.target.put("8", new int[] {2, 1});
        this.target.put("9", new int[] {2, 2});
        this.target.put("*", new int[] {3, 0});
        this.target.put("#", new int[] {3, 2});
        
    }
    
    public int bfs(String start, String end) {
        int[] t = this.target.get(start);
        int x = t[0];
        int y = t[1];
        int[] T = this.target.get(end);
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        int[][] visited = new int[4][3];
        visited[x][y] = 1;
        queue.add(new int[] {x, y});
        
        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int a = node[0];
            int b = node[1];
            int step = visited[a][b];
            
            if (a == T[0] && b == T[1]) return step;
            
            for (int i=0; i<4; i++) {
                x = a + this.dx[i];
                y = b + this.dy[i];
                
                if (0 <= x && x <= 3 && 0 <= y && y <= 2 && visited[x][y] == 0) {
                    visited[x][y] = step+1;
                    queue.add(new int[] {x, y});
                }
            }
        }

        return 0;
    }
    
    public boolean contains(String[] arr, String t) {
        for (String s : arr) {
            if (s.equals(t)) return true;
        }
        return false;
    }
    public String solution(int[] numbers, String hand) {
        String answer = "";
        setTarget();
        String left = "*";
        String right = "#";
        
        for (int n : numbers) {
            String num = Integer.toString(n);
            if (contains(this.leftSide, num)) {
                left = num;
                answer += "L";
                continue;
            }
                
            else if (contains(this.rightSide, num)) {
                right = num;
                answer += "R";
                continue;
            }
                
            int leftStep = bfs(left, num);
            int rightStep = bfs(right, num);
            
            if (leftStep < rightStep) {
                left = num;
                answer += "L";
            }
            
            else if (rightStep < leftStep) {
                right = num;
                answer += "R";
            }
            
            else {
                if ("left".equals(hand)) {
                    left = num;
                    answer += "L";
                }
                else {
                    right = num;
                    answer += "R";
                }
            }
        }
        return answer;
    }

    public void main(String[] args) {
        System.out.println(solution(new int[] {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2}, "left"));
    }
}
