import java.util.HashMap;

public class P258712 {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        HashMap<String, HashMap<String, Integer>> dic = new HashMap<>();
        HashMap<String, Integer> score = new HashMap<>();
        HashMap<String, Integer> answer_list = new HashMap<>();
        for (String friend : friends) {
            dic.put(friend, new HashMap<>());
            score.put(friend, 0);
            answer_list.put(friend, 0);

            for (String friend_ : friends) {
                if (!friend.equals(friend_)) dic.get(friend).put(friend_, 0);
            }
        }

        for (String gift : gifts) {
            String[] splitedGift = gift.split(" ");
            String give = splitedGift[0];
            String take = splitedGift[1];
            dic.get(give).put(take, dic.get(give).get(take)+1);
            score.put(give, score.get(give)+1);
            score.put(take, score.get(take)-1);
        }

        for (String x : friends) {
            for (String y : friends) {
                if (!x.equals(y)) {
                    if (dic.get(x).get(y) == dic.get(y).get(x).intValue()) {
                        if (score.get(x) == score.get(y).intValue()) {
                        } else if (score.get(x) > score.get(y)) answer_list.put(x, answer_list.get(x)+1);
                    }

                    else if (dic.get(x).get(y) > dic.get(y).get(x)) answer_list.put(x, answer_list.get(x)+1);
                }
            }
        }

        for (String friend : friends) {
            if (answer_list.get(friend) > answer) answer = answer_list.get(friend);
        }
        return answer;
    }
}
