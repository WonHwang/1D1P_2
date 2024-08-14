import java.util.ArrayList;

public class P181919 {
    public int[] solution(int n) {
        int[] answer;
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(n);
        while (n != 1) {
            n = n%2 == 1 ? 3*n+1 : n/2;
            arr.add(n);
        }
        answer = new int[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        return answer;
    }
}
