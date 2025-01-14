import java.util.ArrayList;

class P181844 {
    public int[] solution(int[] arr, int[] delete_list) {
        ArrayList<Integer> list = new ArrayList<>();
        for (int num : arr) {
            boolean flag = true;
            for (int del : delete_list) {
                if (num == del) {
                    flag = false;
                    break;
                }
            }
            if (flag) list.add(num);
        }
        int[] answer = new int[list.size()];
        for (int i=0; i<list.size(); i++) answer[i] = list.get(i);
        return answer;
    }
}