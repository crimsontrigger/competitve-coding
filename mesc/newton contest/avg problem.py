import math
t = int(input())
s = list(map(int, input().split()))
avg_val = 0
for i in range(0,t):
    avg_val = avg_val + (s[i]/t)


print(math.floor(avg_val))