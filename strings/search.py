'''
Given a text txt[0..n-1] and a pattern pat[0..m-1],
write a function search(char pat[], char txt[])
that prints all occurrences of pat[] in txt[].
You may assume that n > m.c
'''

def string_search_naive(string, pattern):
    # let's worry about these cases later
    if not string or not pattern:
        return None

    N, M = len(string), len(pattern)
    for i in range(N - M + 1): # offset
        for j in range(M):
            if string[i+j] != pattern[j]:
                break

        if j == M - 1: # this means you've reached the end of pattern, so match
            print 'found at index ' + str(i)

string_search_naive('AABAACAADAABAAABAA', 'AABA')

# time complexity O(N*M)
# b/c run by number of characters for offset and checking the length of pattern
# can get expensive if we've already seen something similar to this before, / string is really long

