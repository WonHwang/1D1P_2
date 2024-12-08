import java.util.ArrayList;

public class P181836 {
        public String[] solution(String[] picture, int k) {
        ArrayList<String> arr = new ArrayList<>();
        for (String line : picture) {
            String target = "";
            for (int i=0; i<line.length(); i++) {
                char digit = line.charAt(i);
                for (int j=0; j<k; j++) target += digit;
            }
            for (int i=0; i<k; i++) {
                arr.add(target);
            }
        }
        String[] answer = new String[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        return answer;
    }
}
