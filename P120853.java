import java.util.Stack;

class P120853 {
    public int solution(String s) {
        Stack<Integer> stack = new Stack<>();
        String[] ss = s.split(" ");
        for (String c : ss) {
            if ("Z".equals(c)) stack.pop();
            else stack.push(Integer.valueOf(c));
        }

        int answer = 0;
        for (int i=0; i<stack.size(); i++) {
            answer += stack.get(i);
        }

        return answer;
    }
}