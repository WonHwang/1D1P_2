import java.util.*;

class P17682 {
    public int solution(String dartResult) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (int i=0; i<dartResult.length(); i++) {
            char digit = dartResult.charAt(i);

            if (digit == '*') {
                int x = stack.pop();
                if (stack.size() >= 1) {
                    int y = stack.pop();
                    stack.push(2*y);
                }
                stack.push(2*x);
            }
            
            else if (digit == '#') {
                int x = stack.pop();
                stack.push(-1*x);
            }
            
            else if (digit == 'S' || digit == 'D' || digit == 'T') {
                int value = Character.getNumericValue(dartResult.charAt(i-1));
                if (value == 0) {
                    if (i-2 >= 0 && dartResult.charAt(i-2) == '1') value = 10;
                }
                
                switch (digit) {
                    case 'S' -> stack.push(value);
                    case 'D' -> stack.push(value*value);
                    case 'T' -> stack.push(value*value*value);
                }
            }
        }
        for (int i=0; i<stack.size(); i++) answer += stack.get(i);
        return answer;
    }
}