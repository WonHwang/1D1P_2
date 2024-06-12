class P120824 {
    public int[] solution(int[] num_list) {
        int odd = 0;
        int even = 0;
        for (int num : num_list) {
            if (num%2 == 0) even += 1;
            else odd += 1;
        }
        return new int[] {even, odd};
    }
}