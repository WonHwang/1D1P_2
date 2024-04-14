import java.util.*;

class Solution {
    public String solution(String s) {
        String[] nums = s.split(" ");
        int[] numbers = new int[nums.length];
        for (int i=0; i<nums.length; i++) {
            numbers[i] = Integer.parseInt(nums[i]);
        }
        Arrays.sort(numbers);
        String answer = Integer.toString(numbers[0]) + " " + Integer.toString(numbers[nums.length-1]);
        return answer;
    }
}