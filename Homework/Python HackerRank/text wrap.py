def wrap(string, max_width):
    for i in range(1,len(string)+1):
        if i % max_width == 0:
            print(string[i-1], end ="")
            print("")
        else:
            print(string[i-1], end ="")
    return ""
