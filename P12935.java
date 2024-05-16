class P12935 {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length-1];
        int min = arr[0];
        for (int i=1; i<arr.length; i++) {
            if (arr[i] < min) min = arr[i];
        }
        int idx = 0;
        for (int i=0; i<arr.length; i++) {
            if (arr[i] != min) {
                answer[idx++] = arr[i];
            }
        }
        
        if (answer.length == 0) answer = new int[] {-1};
        return answer;
    }
}