import java.util.HashMap;

public class P118666 {
    public String reverse(String x) {
        String result = "";
        for (int i=0; i<x.length(); i++) result = x.charAt(i) + result;
        return result;
    }
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        HashMap<String, Integer> dict = new HashMap<>();
        dict.put("RT", 0);
        dict.put("CF", 0);
        dict.put("JM", 0);
        dict.put("AN", 0);

        for (int i=0; i<survey.length; i++) {
            String surv = survey[i];
            int score = choices[i];

            if (!dict.containsKey(surv)) {
                surv = reverse(surv);
                score = 8 - score;
            }

            score -= 4;

            dict.put(surv, dict.get(surv) + score);
        }

        for (String key : dict.keySet()) {
            if (dict.get(key) <= 0) answer += key.charAt(0);
            else answer += key.charAt(1);
        }

        return answer;
    }
}
