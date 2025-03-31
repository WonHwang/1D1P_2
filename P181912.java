import java.util.*;

class P181912 {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (String nums : intStrs) {
            String num = nums.substring(s, s+l);
            int n = Integer.parseInt(num);
            if (n > k) arr.add(n);
        }
        int[] answer = new int[arr.size()];
        for (int i=0; i<answer.length; i++) answer[i] = arr.get(i);
        return answer;
    }
}