import java.util.Arrays;

public class P133499 {

    String[] word2 = new String[] {"ye", "ma"};
    String[] word3 = new String[] {"aya", "woo"};
    
    public int solution(String[] babbling) {
        
        int answer = 0;
        
        for (String word : babbling) {
            String past = "";
            int result = 1;
            
            while (word.length() > 0) {
                if (word.length() < 2) {
                    result = 0;
                    break;
                }
                
                if (Arrays.asList(word2).contains(word.substring(0, 2))) {
                    if (word.substring(0, 2).equals(past)) {
                        result = 0;
                        break;
                    }
                    past = word.substring(0, 2);
                    word = word.substring(2, word.length());
                    continue;
                }
                
                if (word.length() < 3) {
                    result = 0;
                    break;
                }
                
                if (Arrays.asList(word3).contains(word.substring(0, 3))) {
                    if (word.substring(0, 3).equals(past)) {
                        result = 0;
                        break;
                    }
                    past = word.substring(0, 3);
                    word = word.substring(3, word.length());
                    continue;
                }
                
                result = 0;
                break;
            }
            
            if (result > 0) answer += 1;
        }
        return answer;
    }
}
