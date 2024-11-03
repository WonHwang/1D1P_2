class P250137 {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;
        int time = 0;
        int[] attackTime = new int[1001];
        int last = 0;
        
        for (int[] attack : attacks) {
            attackTime[attack[0]] = attack[1];
            if (attack[0] > last) last = attack[0];
        }
        
        int hp = health;
        int continous = 0;
        
        while (true) {
            time += 1;
            
            if (time > last) {
                answer = hp;
                break;
            }
            
            if (attackTime[time] > 0) {
                continous = 0;
                hp = hp - attackTime[time] > 0 ? hp-attackTime[time] : 0;
            }
            
            if (hp == 0) {
                answer = -1;
                break;
            }
            
            if (attackTime[time] == 0) {
                hp += bandage[1];
                continous += 1;
                
                if (continous == bandage[0]) {
                    hp += bandage[2];
                    continous = 0;
                }
                
                hp = hp < health ? hp : health;
            }
        }
        return answer;
    }
}