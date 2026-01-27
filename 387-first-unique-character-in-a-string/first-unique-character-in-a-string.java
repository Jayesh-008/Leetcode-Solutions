class Solution {
    public int firstUniqChar(String s) {
        int len = s.length();
        for (int i = 0; i < len; i++) {
            int c = 0;
            for (int j = 0; j < len; j++) 
            {
                if ( i != j && s.charAt(i) == s.charAt(j)) {
                    c = 1;
                    break;  
                }
            }
            if (c == 0) {
                return i;
            }   
        }
        return -1; 
    }
}