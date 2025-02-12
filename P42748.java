import java.util.Arrays;
import java.util.ArrayList;

class P42748 {
    public int cutsortnum(int[] array, int i, int j, int k) {
        int[] tmp = new int[j-i+1];
        for (int x=i-1; x<j; x++) tmp[x-i+1] = array[x];
        Arrays.sort(tmp);
        return tmp[k-1]; 
    }
    public int[] solution(int[] array, int[][] commands) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i=0; i<commands.length; i++) {
            int[] tmp = commands[i];
            int value = cutsortnum(array, tmp[0], tmp[1], tmp[2]);
            arr.add(value);
        }
        int[] answer = new int[arr.size()];
        for (int i=0; i<answer.length; i++) answer[i] = arr.get(i); 
        return answer;
    }
}