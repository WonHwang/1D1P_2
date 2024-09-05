public class P181879 {
    public int solution(int[] num_list) {
        int sum = 0;
        int prod = 1;
        for (int num : num_list) {
            sum += num;
            prod *= num;
        }
        return num_list.length > 10 ? sum : prod;
    }
}
