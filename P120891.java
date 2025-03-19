class P120891 {
    public int solution(int order) {
        int answer = 0;
        String strOrder = Integer.toString(order);
        for (int i=0; i<strOrder.length(); i++) {
            int c = Character.getNumericValue(strOrder.charAt(i));
            if (c > 0 && c%3 == 0) answer += 1;
        }
        return answer;
    }
}