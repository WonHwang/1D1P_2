public class P181893 {
    public int[] getSub(int[] arr, int start, int end) {
        int[] result = new int [end - start];
        for (int i=0; i<result.length; i++) result[i] = arr[i+start];
        return result;
    }
    public int[] solution(int[] arr, int[] query) {
        int[] answer = {};
        for (int i=0; i<query.length; i++) {
            if (i%2 == 1) arr = getSub(arr, query[i], arr.length);
            else arr = getSub(arr, 0, query[i]+1);
        }
        answer = arr;
        return answer;
    }
}
