n = input()
def p(s1):
    s2 = s1[::-1]
    if s1 == s2:
        print("palindrome")
    else:
        print("not palindrome")
p(n)
