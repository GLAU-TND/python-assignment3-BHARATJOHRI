def is_palindrome(s):
    return bool(s) and s == s[::-1]


def make_palindrome(s, num_delete):
    if is_palindrome(s):
        return True
    if not num_delete:
        return False

    for i, _ in enumerate(s):
        s1 = s[:i] + s[i+1:]
        if make_palindrome(s1, num_delete - 1):
            return True

    return False

s=input()
num_delete=int(input())
print(is_palindrome(s))
print(make_palindrome(s,num_delete))
