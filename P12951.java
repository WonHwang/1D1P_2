class P12951 {
    public String solution(String s) {
        String answer = "";
        int status = 1;
        
        for (int i=0; i<s.length(); i++) {
            String tmp = "";
            String c = Character.toString(s.charAt(i));
            
            if (" ".equals(c)) {
                status = 1;
                tmp = c;
            }
            
            else if (status == 1) {
                status = 0;
                tmp = c.toUpperCase();
            }
            
            else tmp = c.toLowerCase();
            
            answer += tmp;
        }
        return answer;
    }
}