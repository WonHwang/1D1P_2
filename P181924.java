public class P181924 {
    public int[] solution(int[] arr, int[][] queries) {
        for (int[] q : queries) {
            int x = q[0];
            int y = q[1];
            int tmp = arr[x];
            arr[x] = arr[y];
            arr[y] = tmp;
        }
        return arr;
    }
}
