import java.util.*;

class P138476 {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        HashMap<Integer, Integer> tang = new HashMap<>();
        HashMap<Integer, Integer> visited = new HashMap<>();
        
        for (int t : tangerine) {
            if (tang.containsKey(t)) tang.put(t, tang.get(t)+1);
            else tang.put(t, 1);
        }
        for (int t : tang.keySet()) {
            visited.put(t, 0);
        }

        List<Integer> keySet = new ArrayList<>(tang.keySet());
        keySet.sort((o1, o2) -> tang.get(o2).compareTo(tang.get(o1)));
        
        while (k > 0) {
            for (int t : keySet) {
                if (k == 0) break;
                
                if (visited.get(t) == 0) {
                    visited.put(t, 1);
                    if (tang.get(t) >= k) {
                        k = 0;
                        answer += 1;
                    }
                    else {
                        k -= tang.get(t);
                        answer += 1;
                    }
                }
            }
        }
        return answer;
    }
}