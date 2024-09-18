import java.util.ArrayList;

public class P181861 {
    public int[] solution(int[] arr) {
        ArrayList<Integer> al = new ArrayList<>();
        for (int num : arr) {
            for (int i=0; i<num; i++) al.add(num);
        }
        int[] answer = new int[al.size()];
        for (int i=0; i<al.size(); i++) answer[i] = al.get(i);
        return answer;
    }
}