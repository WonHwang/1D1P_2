import java.util.Arrays;

class P120869 {
        public int solution(String[] spell, String[] dic) {
        int answer = 2;
        Arrays.sort(spell);
        String spells = "";
        for (String sp : spell) spells += sp;
        for (String d : dic) {
            String[] tmp = new String[d.length()];
            for (int i=0; i<d.length(); i++) {
                tmp[i] = Character.toString(d.charAt(i));
            }
            Arrays.sort(tmp);
            String tmp2 = "";
            for (String t : tmp) tmp2 += t;
            if (tmp2.equals(spells)) {
                answer = 1;
                break;
            }
        }
        return answer;
    }
}