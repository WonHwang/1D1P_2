import java.util.HashMap;

public class P120883 {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "";
        String ID = id_pw[0];
        String PW = id_pw[1];
        
        HashMap<String, String> database = new HashMap<>();
        for (String[] st : db) {
            database.put(st[0], st[1]);
        }
        
        if (database.containsKey(ID)) {
            if (database.get(ID).equals(PW)) answer = "login";
            else answer = "wrong pw";
        }
        else answer = "fail";
        
        return answer;
    }
}
