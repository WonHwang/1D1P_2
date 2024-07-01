import java.util.Arrays;
import java.util.Comparator;

class P12915 {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String x1, String x2) {
                if (x1.charAt(n) == x2.charAt(n)) {
                    return x1.compareTo(x2);
                }
                return x1.charAt(n) - x2.charAt(n);
            }
        });
        return strings;
    }
}