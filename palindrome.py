
def isKPalRec(str1, str2, m, n):

    if not m: return n

    if not n: return m

    if str1[m - 1] == str2[n - 1]:
        return isKPalRec(str1, str2, m - 1, n - 1)


    res = 1 + min(isKPalRec(str1, str2, m - 1, n),  # Remove from str1
                  (isKPalRec(str1, str2, m, n - 1)))  # Remove from str2

    return res


def isKPal(string, k):
    revStr = string[::-1]
    l = len(string)

    return (isKPalRec(string, revStr, l, l) <= k * 2)


string = "acdcb"
k = 2

print("Yes" if isKPal(string, k) else "No")
