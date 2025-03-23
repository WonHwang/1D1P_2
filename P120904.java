public class P120904 {
    public int solution(int num, int k) {
        int answer = -1;
        String nums = Integer.toString(num);
        for (int i=0; i<nums.length(); i++) {
            if (Character.getNumericValue(nums.charAt(i)) == k) {
                answer = i+1;
                break;
            }
        }
        return answer;
    }
}
