class P181925 {
    public String solution(int[] numLog) {
        String answer = "";
        for (int i=1; i<numLog.length; i++) {
            int n = numLog[i-1];
            int r = numLog[i];
            if (n+1 == r) answer += "w";
            else if (n-1 == r) answer += "s";
            else if (n+10 == r) answer += "d";
            else if (n-10 == r) answer += "a";
        }
        return answer;
    }
}