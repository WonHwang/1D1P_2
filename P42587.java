public class P42587 {
    public int getPriority(int[] priorities) {
        int max = priorities[0];
        for (int i=1; i<priorities.length; i++) {
            if (max < priorities[i]) max = priorities[i];
        }
        return max;
    }
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        int priority = getPriority(priorities);
        
        while (true) {
            if (priorities[0] >= priority) {
                answer += 1;
                if (location == 0) break;
                else location -= 1;
                int[] tmp = new int[priorities.length-1];
                for (int i=0; i<tmp.length; i++) tmp[i] = priorities[i+1];
                priorities = tmp;
                priority = getPriority(priorities);
            }
            else {
                int num = priorities[0];
                int[] tmp = new int[priorities.length];
                for (int i=0; i<tmp.length-1; i++) tmp[i] = priorities[i+1];
                tmp[tmp.length-1] = num;
                priorities = tmp;
                if (location == 0) location = priorities.length-1;
                else location -= 1;
            }
        }
        return answer;
    }
}