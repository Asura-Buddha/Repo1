inp = input().split(" ")
h = int(inp[0])
w = int(inp[1])
pattern = [('.|.'*(2*i+1)).center(w, '-') for i in range(h//2)]
print('\n'.join(pattern + ['WELCOME'.center(w, '-')] + pattern[::-1]))