import java.util.ArrayList;

public class P181918 {
    public int[] solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList<>();
        int i=0;
        while (true) {
            if (i >= arr.length) break;
            if (stk.size() == 0) {
                stk.add(arr[i]);
                i += 1;
            }
            if (stk.size() > 0) {
                if (stk.get(stk.size()-1) < arr[i]) {
                    stk.add(arr[i]);
                    i += 1;
                }
                else {
                    stk.remove(stk.size()-1);
                }
            }
        }
        int[] answer = new int[stk.size()];
        for (i=0; i<answer.length; i++) answer[i] = stk.get(i);
        return answer;
    }
}
