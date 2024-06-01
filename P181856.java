public class P181856 {
    public int solution(int[] arr1, int[] arr2) {
        if (arr1.length > arr2.length) return 1;
        else if (arr2.length > arr1.length) return -1;
        
        int sum1, sum2;
        sum1 = 0;
        sum2 = 0;
        for (int i=0; i<arr1.length; i++) {
            sum1 += arr1[i];
            sum2 += arr2[i];
        }
        
        if (sum1 > sum2) return 1;
        else if (sum2 > sum1) return -1;
        
        return 0;
    }
}
