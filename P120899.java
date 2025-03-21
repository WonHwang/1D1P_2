public class P120899 {
    public int max(int[] array) {
        int res = 0;
        for (int num : array) {
            if (num > res) res = num;
        }
        return res;
    }
    public int indexOf(int[] array, int target) {
        int res = -1;
        for (int i=0; i<array.length; i++) {
            if (array[i] == target) {
                res = i;
                break;
            }
        }
        return res;
    }
    public int[] solution(int[] array) {
        return new int[] {max(array), indexOf(array, max(array))};
    }
}
