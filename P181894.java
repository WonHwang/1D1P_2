import java.util.Arrays;

public class P181894 {
    public static int[] solution(int[] arr) {
        int start = -1;
        int end = -1;
        boolean flag = false;
        for (int i=0; i<arr.length; i++) {
            if (arr[i] == 2) {
                flag = true;
                if (start == -1) {
                    start = i;
                    end = i;
                    continue;
                }
                end = i;
            }
        }
        int[] answer = new int[end-start+1];
        if (flag) for (int i=0; i<answer.length; i++) answer[i] = arr[i+start];
        else answer = new int[] {-1};
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(solution(new int[] {1, 1, 1})));
    }
}