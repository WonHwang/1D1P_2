public class P340213 {
    public int getMinToSec(String m) {
        int res = 0;
        String[] splited = m.split(":");
        res += 60 * Integer.parseInt(splited[0]);
        res += Integer.parseInt(splited[1]);
        return res;
    }
    
    public String getSecToMin(int s) {
        String pre = "";
        pre += Integer.toString(s/60);
        if (pre.length() < 2) pre = "0" + pre;
        String pos = "";
        pos += Integer.toString(s%60);
        if (pos.length() < 2) pos = "0" + pos;
        return pre + ":" + pos;
    }
    
    public int min(int a, int b) {
        return b >= a ? a : b;
    }
    
    public int max(int a, int b) {
        return a >= b ? a : b;
    }
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int result = getMinToSec(pos);
        int videoLength = getMinToSec(video_len);
        int opStart = getMinToSec(op_start);
        int opEnd = getMinToSec(op_end);
        
        if (opStart <= result && result <= opEnd) result = opEnd;
        
        for (String command : commands) {
            if (command.equals("next")) result = min(result+10, videoLength);
            else if (command.equals("prev")) result = max(result-10, 0);
            
            if (opStart <= result && result <= opEnd) result = opEnd;
        }
        
        return getSecToMin(result);
    }
}
