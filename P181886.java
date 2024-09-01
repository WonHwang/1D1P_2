import java.util.ArrayList;

public class P181886 {
    public String[] solution(String[] names) {
        ArrayList<String> arr = new ArrayList<>();
        for (int i=0; i<names.length; i+=5) arr.add(names[i]);
        String[] answer = new String[arr.size()];
        for (int i=0; i<arr.size(); i++) answer[i] = arr.get(i);
        return answer;
    }
}
