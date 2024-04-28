import java.util.*;

class P133502 {
    public int solution(int[] ingredient) {
        int answer = 0;
        
        Stack<Integer> stack = new Stack<>();
        for (int i=0; i<ingredient.length; i++) {
            int ing = ingredient[i];
            
            stack.add(ing);
            
            if (stack.size() >= 4) {
                int lastIdx = stack.size()-1;
                if (stack.get(lastIdx) == 1 && stack.get(lastIdx-1) == 3 && stack.get(lastIdx-2) == 2 && stack.get(lastIdx-3) == 1) {
                    stack.pop();
                    stack.pop();
                    stack.pop();
                    stack.pop();
                    answer += 1;
                }
            }
        } 
        return answer;
    }
}