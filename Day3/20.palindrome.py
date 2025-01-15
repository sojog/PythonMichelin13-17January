
def is_palindrome_v1(s):
    list_s = list(s)
    reversed_s = list(s)
    reversed_s.reverse()
    return list_s == reversed_s
    

def is_palindrome_v2(s):
    revered_string = "".join(reversed(s))
    return revered_string == s

def is_palindrome(s):
    return s == s[::-1]


print(is_palindrome("kaiak"))


