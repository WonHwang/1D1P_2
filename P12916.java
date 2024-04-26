class P12916 {
    boolean solution(String s) {
        int cntp = 0;
        int cnty = 0;
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == 'p' || s.charAt(i) == 'P') cntp += 1;
            if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') cnty += 1;
        }
        
        if (cntp == cnty) return true;
        return false;
    }
}