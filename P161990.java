public class P161990 {
    public int[] solution(String[] wallpaper) {
        int l = 50;
        int t = 50;
        int r = 0;
        int b = 0;
        
        for (int i=0; i<wallpaper.length; i++) {
            for (int j=0; j<wallpaper[0].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    if (i < t) t = i;
                    if (i > b) b = i;
                    if (j < l) l = j;
                    if (j > r) r= j;
                }
            }
        }
        return new int[] {t, l, b+1, r+1};
    }
}
