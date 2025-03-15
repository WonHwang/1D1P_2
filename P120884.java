public class P120884 {
    public int solution(int chicken) {
        int answer = 0;
        while (chicken > 0) {
            int service = chicken / 10;
            answer += service;
            chicken %= 10;
            chicken += service;
            
            if (service == 0) break;
        }
        return answer;
    }
}
