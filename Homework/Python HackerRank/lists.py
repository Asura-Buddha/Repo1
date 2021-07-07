if __name__ == '__main__':
    n = []
    num = int(input())
    for i in range(0,num):
        inp = input().split(" ")
        if inp[0] == "append":
            n.append(int(inp[1]))
        elif inp[0] == "print":
            print(n)
        elif inp[0] == "sort":
            n.sort()
        elif inp[0] == "pop":
            n.pop()
        elif inp[0] == "reverse":
            n.reverse()
        elif inp[0] == "remove":
            n.remove(int(inp[1])) 
        elif inp[0] == "insert":
            n.insert(int(inp[1]),int(inp[2]))       
