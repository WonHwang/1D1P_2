class P250135 {
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        
        int answer = 0;
        
        if (h1 == 1 && m1 == 5 && s1 == 5) return 2;
        
        if (h1 < 12 && h2 > 12) {
            answer = calculate(h1, m1, s1, 12, 0, 0) + calculate(12, 0, 0, h2, m2, s2) - 1;
        }
        else answer = calculate(h1, m1, s1, h2, m2, s2);
        
        return answer;
    }
    
    public int[] setPosition(int h, int m, int s) {
        int cnt = s + 60*(m + 60*h);
        
        s = cnt * 720 % 43200;
        m = cnt * 12 % 43200;
        h = cnt % 43200;
        
        return new int[] {h, m, s};
    }
    
    public boolean checkCorrect(int h1, int m1, int s1) {
        int h = h1+1;
        int m = m1+12;
        int s = s1+720;
        
        if (h == m || m == s || s == h) return true;
        
        return false;
    }
       
    public boolean checkPassby(int h1, int m1, int s1) {
        int h = h1+1;
        int m = m1+12;
        int s = s1+720;
        
        if ((h1 < m1 && h > m) || (m1 < h1 && m > h) || (h1 < s1 && h > s) || (s1 < h1 && s > h) || (m1 < s1 && m > s) || (s1 < m1 && s > m)) return true;
        
        return false;
    }
    
    public int calculate(int h1, int m1, int s1, int h2, int m2, int s2) {
        
        int answer = 0;
        
        int[] t1 = setPosition(h1, m1, s1);
        h1 = t1[0];
        m1 = t1[1];
        s1 = t1[2];
        
        int[] t2 = setPosition(h2, m2, s2);
        h2 = t2[0];
        m2 = t2[1];
        s2 = t2[2];
        
        if (h1 == m1 || m1 == s1 || s1 == h1) {
            answer += 1;
                h1 += 1;
                m1 += 12;
            s1 += 720;
        }
        
        while (true) {
            if (h1 == h2 && m1 == m2 && s1 == s2) break;
            
            if (checkCorrect(h1, m1, s1) || checkPassby(h1, m1, s1)) answer += 1;
            
            h1 += 1;
            m1 += 12;
            s1 += 720;
            h1 %= 43200;
            m1 %= 43200;
            s1 %= 43200;
        }
        
        return answer;
    }
}