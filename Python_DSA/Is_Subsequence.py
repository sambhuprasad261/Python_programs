def isSubsequence(s: str, t: str) -> bool:
    n = len(t)
    a, b = 0, 0

    if s == "" and t == "":
        return True
    elif s == "" and t != "":
        return True
    elif s != "" and t == "":
        return False
    else:
        for i in range(n):
            if s[a] == t[b]:
                a += 1
                b += 1
            else:
                b += 1

        if a == 0:
            return False
        elif a == len(s) - 1:
            return True
        else:
            return False



print(isSubsequence("abc", "ahbgdc"))