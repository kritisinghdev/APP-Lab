def lcs(X, Y):
    m, n = len(X), len(Y)
    
    # dp[i][j] = length of LCS of X[0..i-1] and Y[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Backtrack to reconstruct the actual LCS string
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    lcs_str.reverse()
    return "".join(lcs_str), dp[m][n]


# --- Driver code ---
if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCABA"
    
    subsequence, length = lcs(X, Y)
    
    print(f"Sequence X = \"{X}\"")
    print(f"Sequence Y = \"{Y}\"")
    print(f"Longest Common Subsequence = \"{subsequence}\"")
    print(f"Length of LCS = {length}")