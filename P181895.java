class P181895 {
    public int[] solution(int[] arr, int[][] intervals) {
        int[] answer = new int[intervals[0][1]-intervals[0][0]+intervals[1][1]-intervals[1][0]+2];
        int idx = 0;
        for (int k=0; k<=1; k++) {
            for (int i=intervals[k][0]; i<=intervals[k][1]; i++) {
                answer[idx++] = arr[i];
            }
        }
        return answer;
    }
}