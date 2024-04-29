public class P140108 {
    public int solution(String s) {
        int answer = 0;
        
        while (s.length() > 0) {
            int cntX = 1;
            int noX = 0;
            char target = s.charAt(0);
            
            for (int i=1; i<s.length(); i++) {
                if (s.charAt(i) == target) cntX += 1;
                else noX += 1;
                
                if (cntX == noX) {
                    answer += 1;
                    s = s.substring(i+1);
                    break;
                }
            }
            
            if (cntX != noX) {
                answer += 1;
                break;   
            }
        }
        return answer;
    }
}
