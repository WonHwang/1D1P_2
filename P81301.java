import java.util.HashMap;

class P81301 {
    public int solution(String s) {
        String answer = "";
        HashMap<String, String> hashmap = new HashMap<>() {{
            put("one", "1");
            put("two", "2");
            put("three", "3");
            put("four", "4");
            put("five", "5");
            put("six", "6");
            put("seven", "7");
            put("eight", "8");
            put("nine", "9");
            put("zero", "0");
        }};
        
        int idx = 0;
        String tmp = "";
        
        while (idx < s.length()) {
            
            if ('0' <= s.charAt(idx) && s.charAt(idx) <= '9') {
                answer += s.charAt(idx);
                idx += 1;
            }
            
            else {
                tmp += s.charAt(idx);
                idx += 1;
                
                if (hashmap.containsKey(tmp)) {
                    answer += hashmap.get(tmp);
                    tmp = "";
                }
            }
        }
        return Integer.parseInt(answer);
    }
}