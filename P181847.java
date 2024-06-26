class P181847 {
    public String solution(String n_str) {
        String answer = "";
        if (n_str.charAt(0) != '0') return n_str;
        else {
            for (int i=0; i<n_str.length(); i++) {
                if (n_str.charAt(i) != '0') {
                    answer = n_str.substring(i,n_str.length());
                    break;
                }
            }
        }
        return answer;
    }
}