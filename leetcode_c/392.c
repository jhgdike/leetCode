// It's faster than most answers, but the python code is slow. Try to find why.
bool isSubsequence(char* s, char* t) {
    if (s[0] == '\0') return true;
    int i = 0, j = 0;
    while (t[j] != '\0') {
        if (s[i] == t[j]) {
            i++, j++;
            if (s[i] == '\0') return true;
        } else j++;
    }
    return false;
}
