class P120956 {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] says = new String[] {"aya", "ye", "woo", "ma"};
        for (String str : babbling) {
            String cut = str;
            
            for (String say : says) {
                if (str.contains(say)) {
                    cut = cut.replace(say, " ");
                }
            }
            
            if (cut.trim().length() == 0) answer += 1;
        }
        return answer;
    }
}