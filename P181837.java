class P181837 {
    public int solution(String[] order) {
        int answer = 0;
        for (String o : order) {
            if (o.contains("americano")) answer += 4500;
            else if (o.contains("latte")) answer += 5000;
            else if (o.contains("anything")) answer += 4500;
        }
        return answer;
    }
}