class P120868 {
    public boolean isPossible(int[] side) {
        int a = side[0];
        int b = side[1];
        int c = side[2];
        if (a + b > c) return true;
        return false;
    }
    public int solution(int[] sides) {
        int answer = 0;
        int a = sides[0];
        int b = sides[1];
        if (a > b) {
            int tmp = a;
            a = b;
            b = tmp;
        }
        for (int i=1; i<2001; i++) {
            int[] side = new int[] {a, i, b};
            if (i > b) side = new int[] {a, b, i};
            if (isPossible(side)) answer += 1;
        }
        return answer;
    }
}