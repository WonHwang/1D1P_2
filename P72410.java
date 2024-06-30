public class P72410 {
    public Boolean contains(char[] arr, char x) {
        for (int i=0; i<arr.length; i++) {
            if (arr[i] == x) return true;
        }
        return false;
    }
    
    public String solution(String new_id) {
        
        char[] spc = new char[] {'-', '_', '.'};
        String answer = "";
        
        for (int i=0; i<new_id.length(); i++) {
            char digit = new_id.charAt(i);
            if (('a' <= digit && digit <= 'z') || ('0' <= digit && digit <= '9')) answer += digit;
            else if ('A' <= digit && digit <= 'Z') answer += Character.toLowerCase(digit);
            else if (contains(spc, digit)) answer += digit; 
        }
        
        boolean flag = true;
        while (true) {
            flag = true;
            for (int i=0; i<answer.length()-1; i++) {
                if (answer.charAt(i) == '.' && answer.charAt(i) == answer.charAt(i+1)) {
                    answer = answer.substring(0, i) + answer.substring(i+1, answer.length());
                    flag = false;
                    break;
                }
            }
            if (flag) break;
        }
        
        if (answer.length() > 0 && answer.charAt(0) == '.') answer = answer.substring(1, answer.length());
        
        if (answer.length() > 0 && answer.charAt(answer.length()-1) == '.') answer = answer.substring(0, answer.length()-1);
        
        if (answer.length() == 0) answer += 'a';
        
        if (answer.length() >= 16) answer = answer.substring(0, 15);
        
        if (answer.length() > 0 && answer.charAt(answer.length()-1) == '.') answer = answer.substring(0, answer.length()-1);
        
        if (answer.length() > 0) {
            while (answer.length() <= 2) {
                answer += answer.charAt(answer.length()-1);
            }
        }
        
        return answer;
    }
}
