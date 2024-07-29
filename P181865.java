public class P181865 {
    public int solution(String binomial) {
        if (binomial.contains("+")) {
            String[] tmp = binomial.split("\\+");
            String a = tmp[0].trim();
            String b = tmp[1].trim();
            int x = Integer.parseInt(a);
            int y = Integer.parseInt(b);
            return x+y;
        }
        if (binomial.contains("-")) {
            String[] tmp = binomial.split("\\-");
            String a = tmp[0].trim();
            String b = tmp[1].trim();
            int x = Integer.parseInt(a);
            int y = Integer.parseInt(b);
            return x-y;
        }
        if (binomial.contains("*")) {
            String[] tmp = binomial.split("\\*");
            String a = tmp[0].trim();
            String b = tmp[1].trim();
            int x = Integer.parseInt(a);
            int y = Integer.parseInt(b);
            return x*y;
        }
        return 0;
    }
}
