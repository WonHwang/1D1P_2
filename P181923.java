import java.util.ArrayList;

public class P181923 {
    public int[] solution(int[] arr, int[][] queries) {
        ArrayList<Integer> result = new ArrayList<>();
        ArrayList<Integer> arrList = new ArrayList<>();
        for (int[] q : queries) {
            int s = q[0];
            int e = q[1];
            int k = q[2];
            
            for (int i=0; i<arr.length; i++) {
                if (i >= s && i <= e) {
                    if (arr[i] > k) {
                        arrList.add(arr[i]);
                    }
                }
            }
            
            if (arrList.size() == 0) result.add(-1);
            else {
                int min = 1000001;
                for (int i=0; i<arrList.size(); i++) {
                    if (arrList.get(i) < min) min = arrList.get(i);
                }
                result.add(min);
                arrList = new ArrayList<>();
            }
        }
        int[] answer = new int[result.size()];
        for (int i=0; i<result.size(); i++) answer[i] = result.get(i);
        return answer;
    }
}
