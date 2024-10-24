class P120864 {
    public int solution(String my_string) {
        int answer = 0;
        String tmp = "0";
        for (int i=0; i<my_string.length(); i++) {
            char digit = my_string.charAt(i);
            if ('A' <= digit && digit <= 'z') {
                answer += Integer.parseInt(tmp);
                tmp = "0";
            }
            else tmp += digit;
        }
        answer += Integer.parseInt(tmp);
        return answer;
    }
}