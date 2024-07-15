class P181882 {
    public int[] solution(int[] arr) {
        int[] answer = new int[arr.length];
        for (int i=0; i<arr.length; i++) {
            int x = arr[i];
            if (x%2 == 0 && x >= 50) answer[i] = x/2;
            else if (x%2 == 1 && x < 50) answer[i] = x*2;
            else answer[i] = x;
        }
        return answer;
    }
}