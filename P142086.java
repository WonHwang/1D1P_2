public class P142086 {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        for (int i=0; i<answer.length; i++) answer[i] = -1;
        for (int j='a'; j<='z'; j++) {
            char c = (char) j;
            int idx = -1;
            for (int i=0; i<answer.length; i++) {
                if (c == s.charAt(i)) {
                    if (idx == -1) idx = i;
                    else {
                        answer[i] = i - idx;
                        idx = i;
                    }
                }
            }
        }
        return answer;
    }
}
