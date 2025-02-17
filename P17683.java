import java.util.ArrayList;

public class P17683 {
    public int getTimeGap(String time) {
        String[] hm = time.split(":");
        int hour = Integer.parseInt(hm[0]);
        int minute = Integer.parseInt(hm[1]);
        
        return hour*60 + minute;
    }
        
    public String getChord(String chord) {
        chord = chord.replace("C#", "c");
        chord = chord.replace("D#", "d");
        chord = chord.replace("F#", "f");
        chord = chord.replace("G#", "g");
        chord = chord.replace("A#", "a");
        chord = chord.replace("B#", "b");
        
        return chord;
    }
    
    public class Music {
        
        private final int gap;
        private final String chord;
        private final String word;
        
        public Music(int gap, String chord, String word) {
            this.gap = gap;
            this.chord = chord;
            this.word = word;
        }
        
        public int getGap() {
            return this.gap;
        }
        
        public String getChord() {
            return this.chord;
        }
        
        public String getWord() {
            return this.word;
        }
        
        public String get() {
            return "[" + Integer.toString(this.gap) + ", " + this.chord + ", " + this.word + "]";
        }
    }
    
    public String solution(String m, String[] musicinfos) {
        String answer = "";
        m = getChord(m);
        
        ArrayList<Music> musics = new ArrayList<>();
        
        for (String music : musicinfos) {
            String[] splitedMusic = music.split(",");
            String start = splitedMusic[0];
            String end = splitedMusic[1];
            String word = splitedMusic[2];
            String chord = splitedMusic[3];
            
            int gap = getTimeGap(end) - getTimeGap(start);
            chord = getChord(chord);
            
            while (chord.length() < gap) {
                chord += chord;
            }
            if (chord.length() >= gap) chord = chord.substring(0, gap);
            musics.add(new Music(gap, chord, word));
        }
        
        musics.sort((m1, m2) -> 
            m2.getGap() - m1.getGap()
        );
            
        for (Music music : musics) {
            String chord = music.getChord();
            String word = music.getWord();
            
            if (chord.contains(m)) {
                answer = word;
                break;
            }
        }
        
        return answer.equals("") ? "(None)" : answer;
    }
}
