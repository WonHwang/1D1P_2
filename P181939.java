public class P181939 {
    public int solution(int a, int b) {
        String A = Integer.toString(a);
        String B = Integer.toString(b);
        int AB = Integer.parseInt(A+B);
        int BA = Integer.parseInt(B+A);
        return AB >= BA ? AB : BA;
    }
}
