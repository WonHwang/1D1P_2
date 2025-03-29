import java.util.Arrays;

public class P120911 {
        public String solution(String my_string) {
        String answer = "";
        my_string = my_string.toLowerCase();
        String[] arr = new String[my_string.length()];
        for (int i=0; i<arr.length; i++) arr[i] = Character.toString(my_string.charAt(i));
        Arrays.sort(arr);
        for (String str : arr) answer += str;
        return answer;
    }
}
