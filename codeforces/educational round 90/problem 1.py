t = int(input())
output = []
for _ in range(t):
    temp = []
    a, b, c = map(int, input().split())

    if a >= c:
        temp.append(-1)
    else:
        temp.append(1)

    if b*a > c:
        temp.append(b)
    else:
        temp.append(-1)

    output.append(temp)

for x in output:
    for y in x:
        print(y, end=" ")
    print()
