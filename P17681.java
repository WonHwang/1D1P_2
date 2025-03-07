import java.util.ArrayList;

public class P17681 {
    public String numToBinary(int n) {
        String result = "";
        while (n > 0) {
            result = Integer.toString(n%2) + result;
            n /= 2;
        }
        return result;
    }

    public String[] numsToBinarys(int n, int[] arr) {
        ArrayList<String> result = new ArrayList<>();
        for (int num : arr) {
            String binary = numToBinary(num);
            while (binary.length() < n) binary = "0" + binary;
            result.add(binary);
        }
        String[] binarys = new String[result.size()];
        for (int i=0; i<binarys.length; i++) binarys[i] = result.get(i);
        return binarys;
    }

    public String[] merge(int n, String[] bin1, String[] bin2) {
        ArrayList<String> arr = new ArrayList<>();
        for (int i=0; i<n; i++) {
            String line = "";
            for (int j=0; j<n; j++) {
                if (bin1[i].charAt(j) == '1' || bin2[i].charAt(j) == '1') line += "#";
                else line += " ";
            }
            arr.add(line);
        }
        String[] result = new String[arr.size()];
        for (int i=0; i<result.length; i++) result[i] = arr.get(i);
        return result;
    }
    
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] bin1 = numsToBinarys(n, arr1);
        String[] bin2 = numsToBinarys(n, arr2);
        String[] answer = merge(n, bin1, bin2);
        return answer;
    }
}