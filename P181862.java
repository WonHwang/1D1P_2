import java.util.ArrayList;

public class P181862 {
    public String[] solution(String myStr) {
        String[] tmp = myStr.split("a");
        ArrayList<String> tmp2 = new ArrayList<>();
        for (String c : tmp) {
            String[] splitC = c.split("b");
            for (String d : splitC) {
                if (!d.equals("")) tmp2.add(d);
            }
        }
        
        ArrayList<String> result = new ArrayList<>();
        for (int i=0; i<tmp2.size(); i++) {
            String c = tmp2.get(i);
            String[] splitC = c.split("c");
            for (String d : splitC) {
                if (!d.equals("")) result.add(d);
            }
        }
        if (result.size() == 0) return new String[] {"EMPTY"};
        String[] answer = new String[result.size()];
        for (int i=0; i<result.size(); i++) answer[i] = result.get(i);
        return answer;   
    }
}
