class P12922 {
    public String solution(int n) {
        String answer = "수박"/* .repeat(n/2) 왜 안되지*/;
        if (n%2 == 1) answer += "수";
        return answer;
    }
}