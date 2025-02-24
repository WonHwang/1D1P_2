class P42862 {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        int[] arr = new int[n+2];
        for (int i=1; i<n+1; i++) arr[i] = 1;

        for (int l : lost) arr[l] = 0;
        for (int r : reserve) arr[r] += 1;

        for (int i=1; i<n+1; i++) {
            if (arr[i] == 0) {
                if (arr[i-1] == 2) {
                    arr[i-1] -= 1;
                    arr[i] += 1;
                }
                else if (arr[i+1] == 2) {
                    arr[i+1] -= 1;
                    arr[i] += 1;
                }
            }
        }

        for (int i=1; i<n+1; i++) {
            if (arr[i] != 0) answer += 1;
        }
        return answer;
    }
}