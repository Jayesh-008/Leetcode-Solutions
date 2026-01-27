int firstUniqChar(char* s) {
        int i, j;
    int n = strlen(s);

    for (i = 0; i < n; i++) {
        int c = 0;
        for (j = 0; j < n; j++) {
            if (i != j && s[i] == s[j]) {
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


        



    




