public class P120876 {
    public int solution(int[][] lines) {
        int answer = 0;
        int[] grid = new int[201];
        for (int[] line:lines) {
            int a = line[0];
            int b = line[1];
            for (int i=a; i<b; i++) grid[i+100] += 1;
        }
        for (int i=0; i<201; i++) {
            if (grid[i] >= 2) answer += 1;
        }
        return answer;
    }
}
