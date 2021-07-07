if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    dig = False
    lower = False
    upper = False

    for i in s:
        if i.isalnum():
            alnum = i.isalnum()
        if i.isalpha():
            alpha = i.isalpha()
        if i.isdigit():
            dig = i.isdigit()
        if i.islower():
            lower = i.islower()
        if i.isupper():
            upper = i.isupper()
    print(alnum)
    print(alpha)
    print(dig)
    print(lower)
    print(upper)
