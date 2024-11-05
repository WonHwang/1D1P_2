class P340199 {
    public int max(int[] a) {
        int res = a[0];
        for (int i=0; i<a.length; i++) {
            if (a[i] > res) res = a[i];
        }
        return res;
    }
    public int min(int[] a) {
        int res = a[0];
        for (int i=0; i<a.length; i++) {
            if (a[i] < res) res = a[i];
        }
        return res;
    }
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        while (min(bill) > min(wallet) || max(bill) > max(wallet)) {
            bill = new int[] {max(bill)/2, min(bill)};
            answer += 1;
        }
        return answer;
    }
}
