class P120912 {
    public int solution(int[] array) {
        int answer = 0;
        for (int i=0; i<array.length; i++) {
            int x = array[i];
            String y = Integer.toString(x);
            for (int j=0; j<y.length(); j++) {
                if (y.charAt(j) == '7') answer += 1;
            }
        }
        return answer;
    }
}