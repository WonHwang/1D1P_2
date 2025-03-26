class P120908 {
    public int solution(String str1, String str2) {
        return new int[]{2, 1}[str1.contains(str2)?1:0];
    }
}