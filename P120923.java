import java.util.*;

class P120923 {
    public int[] solution(int num, int total) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i=-1000; i<=1000; i++) {
            int tmp = 0;
            for (int j=i; j<i+num; j++) {
                tmp += j;
            }
            if (tmp == total) {
                for (int j=i; j<i+num; j++) arr.add(j);
                break;
            }
        }
        int[] answer = new int[arr.size()];
        for (int i=0; i<answer.length; i++) answer[i] = arr.get(i);
        return answer;
    }
}