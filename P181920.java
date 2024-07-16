public class P181920 {
    public int[] solution(int x, int y) {
        int[] answer = new int[y-x+1];
        for (int i=0; i<=y-x; i++) answer[i] = i+x;
        return answer;
    }
}
