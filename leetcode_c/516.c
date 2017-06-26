int longestPalindromeSubseq(char* s) {

    int n = strlen(s), i, j;
    int dp[n][n];
    memset(dp, 0, sizeof(dp));
    for (i = n-1; i >=0; i--) {
        dp[i][i] = 1;
        for (j = i+1; j < n; j ++) {
            if (s[i] == s[j]) dp[i][j] = dp[i+1][j-1] + 2;
            else dp[i][j] = dp[i+1][j] > dp[i][j-1] ? dp[i+1][j]: dp[i][j-1];
        }
    }
    return dp[0][n-1];
}