public class P181928 {
    public int solution(int[] num_list) {
        String odd = "";
        String even = "";
        for (int num : num_list) {
            if (num % 2 == 1) odd += Integer.toString(num);
            else even += Integer.toString(num);
        }
        return Integer.parseInt(odd)+Integer.parseInt(even);
    }
}
