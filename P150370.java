import java.util.*;

public class P150370 {
    public int getDaysFromDate(String day) {
        String[] target = day.split("[.]");
        return Integer.parseInt(target[2]) + 28*(Integer.parseInt(target[1]) + 12*Integer.parseInt(target[0]));
    }
    public Integer[] solution(String today, String[] terms, String[] privacies) {
        LinkedList<Integer> result = new LinkedList<>();
        int tday = getDaysFromDate(today);
        
        HashMap<String, Integer> term = new HashMap<>();
        
        for (String t:terms) {
            String[] target = t.split(" ");
            String dst = target[0];
            int duration = Integer.parseInt(target[1]);
            term.put(dst, 28*duration);
        }
        
        for (int i=0; i<privacies.length; i++) {
            String privacy = privacies[i];
            String[] target = privacy.split(" ");
            String date = target[0];
            String dst = target[1];
            int days = getDaysFromDate(date);
            
            if (days + term.get(dst) <= tday) result.add(i+1);
        }

        Integer[] answer = new Integer[result.size()];
        result.toArray(answer);
        
        return answer;
    }
}