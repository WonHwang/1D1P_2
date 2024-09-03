public class P181881 {
    public int solution(int[] arr) {
        int answer = 0;
        for (int i=0; i<arr.length; i++) {
            int cnt = 0;
            int num = arr[i];
            while (true) {
                int tmp = num;
                if (tmp >= 50 && tmp%2 == 0) tmp /= 2;
                else if (tmp < 50 && tmp%2 == 1) {
                    tmp *= 2;
                    tmp += 1;
                }
                
                if (tmp == num) break;
                cnt += 1;
                num = tmp;
            }
            if (cnt > answer) answer = cnt;
        }
        return answer;
    }
}
