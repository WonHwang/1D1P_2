import java.util.ArrayList;

class P42586 {
    public int[] solution(int[] progresses, int[] speeds) {
        
        int front = 0;
        int end = speeds.length;
        ArrayList<Integer> arr = new ArrayList<>();
        
        while (true) {
            int tmp = 0;
            for (int i=0; i<end; i++) progresses[i] += speeds[i];
            for (int i=front; i<end; i++) {
                if (progresses[i] >= 100) {
                    tmp += 1;
                    front += 1;
                }
                else break;
            }
            
            if (tmp != 0) arr.add(tmp);
            if (front == end) break;
        }
        int[] answer = new int[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        
        return answer;
    }
}