import java.util.ArrayList;

public class P181857 {
        public boolean isTwoSquare(int N) {
        int tmp = 1;
        while (tmp <= 1024) {
            if (tmp == N) return true;
            tmp *= 2;
        }
        return false;
    }
    public int[] solution(int[] arr) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int num : arr) list.add(num);
        while (!isTwoSquare(list.size())) list.add(0);
        int[] answer = new int[list.size()];
        for (int i=0; i<answer.length; i++) answer[i] = list.get(i);
        return answer;
    }
}
