def swap_case(s):
    s = list(s)
    for i in range(0,len(s)):
        if s[i].isupper():
            s[i] = s[i].lower()
        elif s[i].islower():
            s[i] = s[i].upper()
    fin = ""
    for i in s:
        fin += i
    return fin

