class P120894 {
    public long solution(String numbers) {
        String[] words = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

        for (int i = 0; i < 10; i++) {
            numbers = numbers.replace(words[i], String.valueOf(i));
        }
        return Long.parseLong(numbers);
        
    }
}
