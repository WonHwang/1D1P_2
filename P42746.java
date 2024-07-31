import java.util.Arrays;

public class P42746 {
    public int compare(String a, String b) {
        
        int tmp1 = Integer.parseInt(a+b);
        int tmp2 = Integer.parseInt(b+a);
        
        if (tmp1 < tmp2) return 1;
        else if (tmp1 == tmp2) return 0;
        return -1;
    }
    public String solution(int[] numbers) {
        String[] nums = new String[numbers.length];
        for (int i=0; i<numbers.length; i++) nums[i] = Integer.toString(numbers[i]);
        Arrays.sort(nums, (a, b) -> compare(a, b));
        String answer = "";
        for (String num : nums) answer += num;
        boolean flag = true;
        for (int i=0; i<answer.length(); i++) {
            if (answer.charAt(i) != '0') {
                flag = false;
                break;
            }
        }
        if (flag) answer = "0";
        return answer;
    }
}
