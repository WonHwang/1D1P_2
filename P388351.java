class P388351 {
    
    public int getMinFromTime(int time) {
        int h = time / 100;
        int m = time % 100;
        
        return 60*h + m;
    }
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        
        for (int i=0; i<timelogs.length; i++) {
            int day = startday - 1;
            int target = getMinFromTime(schedules[i]);
            boolean res = true;
            
            for (int j=0; j<timelogs[i].length; j++) {
                day += 1;
                day %= 7;
                
                if (!(day == 0 || day == 6)) {
                    int pres = getMinFromTime(timelogs[i][j]);
                    if (target+10 < pres) {
                        res = false;
                        break;
                    }
                }
            }
            
            if (res) answer += 1;
        }
        return answer;
    }
}