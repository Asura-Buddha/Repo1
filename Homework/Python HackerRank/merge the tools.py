def merge_the_tools(string, k):
    split = [string[i:i+k] for i in range(0, len(string), k)]
    for i in range(len(split)):
        tmp = []
        for j in split[i]:
            if j not in tmp:
                tmp.append(j)
        split[i] = tmp
    for i in split:
        for j in i:
            print(j, end="")
        print()
        

if __name__ == '__main__':