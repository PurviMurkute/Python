s = "23546568"

n = len(s)

print(n)

def largestOdSub(s):
    for i in range(n-1, -1, -1):
        if int(s[i]) % 2 != 0:
            return s[:i+1]

    return ""

print(largestOdSub(s))