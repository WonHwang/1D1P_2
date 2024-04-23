class P70129 {
    public String toBinary(int l) {
        String result = "";
        while (l != 0) {
            if (l%2 == 1) result = "1" + result;
            else result = "0" + result;
            l /= 2;
        }
        return result;
    }
    public int[] solution(String s) {
        String tmp = "";
        int cnt = 0;
        int cnt2 = 0;
        while (!s.equals("1")) {              
            cnt2 += s.length();
            for (int i=0; i<s.length(); i++) {
                if (s.charAt(i) == '1') tmp += "1";
            }
            s = tmp;
            tmp = "";
            cnt2 -= s.length();       
            s = toBinary(s.length());
            
            cnt += 1;
        }
        
        return new int[] {cnt, cnt2};
    }
}