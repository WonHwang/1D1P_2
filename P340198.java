class P340198 {
    public boolean isPossible(int mat, String[][] park) {
        int N = park.length;
        int M = park[0].length;
        
        for (int i=0; i<N-mat+1; i++) {
            for (int j=0; j<M-mat+1; j++) {
                if (park[i][j].equals("-1")) {
                    boolean res = true;
                    for (int x=0; x<mat; x++) {
                        for (int y=0; y<mat; y++) {
                            if (!park[i+x][j+y].equals("-1")) {
                                res = false;
                                break;
                            }
                        }
                        if (!res) break;
                    }
                    if (res) return true;
                }
            }
        }
        return false;
    }
    
    public int solution(int[] mats, String[][] park) {
        int answer = 0;
        for (int mat : mats) {
            if (isPossible(mat, park)) {
                if (mat > answer) answer = mat;
            }
        }
        
        return answer > 0 ? answer : -1;
    }
}
