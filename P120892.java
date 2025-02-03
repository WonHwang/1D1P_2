class P120892 {
    public String solution(String cipher, int code) {
        String answer = "";
        for (int i=0; i<cipher.length(); i++) {
            char x = cipher.charAt(i);
            if ((i+1)%code == 0) answer += x;
        }
        return answer;
    }
}