from itertools import product
a = map(int, input().split(" "))
b = map(int, input().split(" "))
fin = list(product(a,b))
for i in fin:
    print(i, end =" ")
