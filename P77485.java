import java.util.ArrayList;

public class P77485 {
    public int rotation(int N, int M, int[][] matrix, int[] query) {

        int x1 = query[0];
        int y1 = query[1];
        int x2 = query[2];
        int y2 = query[3];
        x1 -= 1;
        y1 -= 1;
        x2 -= 1;
        y2 -= 1;

        int[] points = new int[] {matrix[x1][y1], matrix[x2][y1], matrix[x1][y2], matrix[x2][y2]};
        int Min = N*M;

        for (int i=y2; i>y1; i--) {
            matrix[x1][i] = matrix[x1][i-1];
            if (matrix[x1][i] < Min) Min = matrix[x1][i];
        }

        for (int i=x2; i>x1+1; i--) {
            matrix[i][y2] = matrix[i-1][y2];
            if (matrix[i][y2] < Min) Min = matrix[i][y2];
        }
        matrix[x1+1][y2] = points[2];
        if (points[2] < Min) Min = points[2];

        for (int i=y1; i<y2-1; i++) {
            matrix[x2][i] = matrix[x2][i+1];
            if (matrix[x2][i] < Min) Min = matrix[x2][i];
        }
        matrix[x2][y2-1] = points[3];
        if (points[3] < Min) Min = points[3];

        for (int i=x1; i<x2-1; i++) {
            matrix[i][y1] = matrix[i+1][y1];
            if (matrix[i][y1] < Min) Min = matrix[i][y1];
        }
        matrix[x2-1][y1] = points[1];
        if (points[1] < Min) Min = points[1];

        return Min;
    }
    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] matrix = new int[rows][columns];
        int cnt = 1;

        for (int i=0; i<rows; i++) {
            for (int j=0; j<columns; j++) {
                matrix[i][j] = cnt;
                cnt += 1;
            }
        }

        ArrayList<Integer> arr = new ArrayList<>();
        for (int[] query : queries) {
            int Min = rotation(rows, columns, matrix, query);
            arr.add(Min);
        }
        int[] answer = new int[arr.size()];
        for (int i=0; i<answer.length; i++) answer[i] = arr.get(i);
        return answer;
    }
}
