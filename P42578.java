import java.util.HashMap;

public class P42578 {
    public int solution(String[][] clothes) {
        
        HashMap<String, Integer> dict = new HashMap<>();
        
        for (int i=0; i<clothes.length; i++) {
            String c = clothes[i][1];
            if (dict.containsKey(c)) dict.put(c, dict.get(c) + 1);
            else dict.put(c, 1);
        }

        int answer = 1;
        for (String key : dict.keySet()) {
            answer *= dict.get(key) + 1;
        }
        answer -= 1;
        
        return answer;
    }
}
