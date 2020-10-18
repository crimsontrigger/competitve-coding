t = int(input())
output = []
for _ in range(t):
    temp = []
    s,n = map(int, input().split())

    for i in range(n+1,2,-2):
        print(i)
        if s == 0:
            break
        else:
            if s%i==0:
                s= s-
