import java.util.*;

public class P12981 {
        public int[] solution(int n, String[] words) {
        LinkedList<Integer> result = new LinkedList<>();
        HashSet<String> wordSet = new HashSet<>();
        int[] turns = new int[n];
        String word = words[0];
        int player = 0;
        turns[player] += 1;
        wordSet.add(word);
        for (int i=1; i<words.length; i++) {
            player = i%n;
            turns[player] += 1;
            if (word.charAt(word.length()-1) != words[i].charAt(0) || wordSet.contains(words[i])) {
                result.add(player+1);
                result.add(turns[player]);
                break;
            }
            word = words[i];
            wordSet.add(word);
        }

        int[] answer = new int[result.size()];
        for (int i=0; i<result.size(); i++) answer[i] = result.get(i);

        if (answer.length == 0) answer = new int[] {0, 0};

        return answer;
    }
}
