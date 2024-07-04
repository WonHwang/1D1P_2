import java.util.*;

public class P250121 {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        LinkedList<int[]> result = new LinkedList<>();
        HashMap<String, Integer> dst = new HashMap<>();
        dst.put("code", 0);
        dst.put("date", 1);
        dst.put("maximum", 2);
        dst.put("remain", 3);
        
        for (int[] d:data) {
            if (d[dst.get(ext)] < val_ext) {
                result.add(d);
            }
        }
        Collections.sort(result, (o1, o2) -> o1[dst.get(sort_by)] - o2[dst.get(sort_by)]);
        int[][] answer = new int[result.size()][];
        for (int i=0; i<result.size(); i++) {
            answer[i] = result.get(i);
        }
        return answer;
    }
}
