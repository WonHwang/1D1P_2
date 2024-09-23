public class P181855 {
    public int solution(String[] strArr) {
        int answer = 0;
        for (int i=1; i<31; i++) {
            int cnt = 0;
            for (String s : strArr) {
                if (s.length() == i) cnt += 1;
            }
            if (cnt > answer) answer = cnt;
        }
        return answer;
    }    
}