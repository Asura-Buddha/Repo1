def minion_game(string):
    cnt1 = 0
    cnt2 = 0
    for i in range(0,len(string)):
        if string[i] in ("A","E","I","O","U"):
            cnt2 += len(string) - i
        else:
            cnt1 += len(string) - i
    if cnt1 > cnt2:
        print("Stuart " + str(cnt1))
    elif cnt1 < cnt2:
        print("Kevin " + str(cnt2))
    else:
        print("Draw")
        

