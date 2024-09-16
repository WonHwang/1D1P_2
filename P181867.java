import java.util.ArrayList;

public class P181867 {
    public int[] solution(String myString) {
        ArrayList<Integer> arr = new ArrayList<>();
        int cnt = 0;
        for (int i=0; i<myString.length(); i++) {
            if (myString.charAt(i) == 'x') {
                arr.add(cnt);
                cnt = 0;
            }
            else cnt += 1;
        }
        arr.add(cnt);
        int[] answer = new int[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        return answer;
    }
}
