class P12950 {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int[][] answer = {};
        int n, m;
        n = arr1.length;
        m = arr1[0].length;
        answer = new int[n][m];
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) answer[i][j] = arr1[i][j] + arr2[i][j];
        }
        return answer;
    }
}