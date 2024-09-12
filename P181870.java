import java.util.ArrayList;

public class P181870 {
        public String[] solution(String[] strArr) {
        String[] answer = {};
        ArrayList<String> arr = new ArrayList<>();
        for (String str : strArr) {
            if (str.indexOf("ad") == -1) arr.add(str);
        }
        answer = new String[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        return answer;
    }
}
