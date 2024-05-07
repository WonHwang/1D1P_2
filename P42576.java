import java.util.*;

public class P42576 {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> dict = new HashMap<>();
        for (int i=0; i<participant.length; i++) {
            String player = participant[i];
            if (dict.containsKey(player)) dict.replace(player, dict.get(player)+1);
            else dict.put(player, 1);
        }
        for (int i=0; i<completion.length; i++) {
            String player = completion[i];
            dict.replace(player, dict.get(player)-1);
        }
        for (int i=0; i<participant.length; i++) {
            String player = participant[i];
            if (dict.get(player) != 0) answer = player;
        }
        return answer;
    }
}
