public class P181921 {
    public int[] solution(int l, int r) {
        int[] answer = {};
        int[] num = new int[] {5, 50, 55, 500, 505, 550, 555, 5000, 5005, 5050, 5055, 5500, 5505, 5550, 5555, 50000, 50005, 50050, 50055, 50500, 50505, 50550, 50555, 55000, 55005, 55050, 55055, 55500, 55505, 55550, 55555, 500000, 500005, 500050, 500055, 500500, 500505, 500550, 500555, 505000, 505005, 505050, 505055, 505500, 505505, 505550, 505555, 550000, 550005, 550050, 550055, 550500, 550505, 550550, 550555, 555000, 555005, 555050, 555055, 555500, 555505, 555550, 555555};
        
        if (l == r) {
            for (int n : num) {
                if (l == n) return new int[] {l};
            }
            return new int[] {-1};
        }
        
        int start = 0;
        int end = num.length - 1;
        
        while (start <= end) {
            int mid = (start + end ) / 2;
            if (num[mid] > r) end = mid - 1;
            else start = mid + 1;
        }
        
        int startIdx = -1;
        for (int i=0; i<num.length; i++) {
            if (num[i] >= l) {
                startIdx = i;
                break;
            }
        }
        
        if (startIdx != -1) {
            answer = new int[end-startIdx+1];
            for (int i=0; i<answer.length; i++) answer[i] = num[startIdx+i];
        }
        
        if (answer.length == 0) return new int[] {-1};
        
        return answer;
    }
}