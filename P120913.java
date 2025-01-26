import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

class P120913 {
    public String[] solution(String my_str, int n) {
        ArrayList<String> arr = new ArrayList<>();
        Queue<Character> queue = new LinkedList<>();
        for (int i=0; i<my_str.length(); i++) queue.offer(my_str.charAt(i));
        while (!queue.isEmpty()) {
            String tmp = "";
            for (int i=0; i<n; i++) {
                if (!queue.isEmpty()) {
                    tmp += queue.poll();
                }
            }
            arr.add(tmp);
        }
        String[] answer = new String[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        return answer;
    }
}