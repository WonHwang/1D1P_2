import java.util.ArrayList;

public class P181854 {
    public int[] solution(int[] arr, int n) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int i=0; i<arr.length; i++) {
            int a = arr[i];
            int[] tmp = arr.length%2 == 1 ? new int[] {n, 0} : new int[] {0, n};
            list.add(a + tmp[i%2]);
        }
        
        int[] answer = new int[list.size()];
        for (int i=0; i<answer.length; i++) answer[i] = list.get(i);
        return answer;
    }
}
