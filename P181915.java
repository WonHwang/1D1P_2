public class P181915 {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        for (int x : index_list) answer += my_string.charAt(x);
        return answer;
    }
}
