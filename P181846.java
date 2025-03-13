class P181846 {
    public String getReverse(String s) {
        String result = "";
        for (int i=0; i<s.length(); i++) result = s.charAt(i) + result;
        return result;
    }
    public String solution(String a, String b) {
        String answer = "";
        if (b.length() > a.length()) {
            String tmp = a;
            a = b;
            b = tmp;
        }
        
        if (b.length() < a.length()) {
            while (b.length() != a.length()) b = "0" + b;
        }
        
        a = getReverse(a);
        b = getReverse(b);
        int z = 0;
        
        for (int i=0; i<a.length(); i++) {
            int x = Character.getNumericValue(a.charAt(i));
            int y = Character.getNumericValue(b.charAt(i));
            int tmp = x + y + z;
            answer += Integer.toString(tmp%10);
            z = tmp / 10;
        }
        
        if (z > 0) answer += Integer.toString(z);
        
        return getReverse(answer);
    }
}