import java.util.*;

class P120863 {
    public String solution(String polynomial) {
        String answer = "";
        
        String[] tmpLine = polynomial.split(" ");
        ArrayList<String> arr = new ArrayList<>();
        for (String tmp : tmpLine) {
            if (!tmp.contains("+")) arr.add(tmp);
        }
        String[] line = new String[arr.size()];
        for (int i=0; i<line.length; i++) line[i] = arr.get(i);
        
        int x = 0;
        int c = 0;
        for (String d : line) {
            if (d.charAt(d.length()-1) == 'x') {
                if (d.charAt(0) == 'x') x += 1;
                else x += Integer.parseInt(d.substring(0, d.length()-1));
            }
            else c += Integer.parseInt(d);
        }
        
        if (x > 0) {
            if (x > 1) answer += x + "x";
            else answer += "x";
        }
        if (c > 0) {
            if (answer != "") answer += " + " + c;
            else answer += c;
        }
        return answer;
    }
}