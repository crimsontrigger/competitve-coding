t = int(input())
output = []
for _ in range(t):
    temp = []
    a = list(map(int, input()))
    count = 0
    val = True
    while val==True:
        initLen = len(a)
        for i in range(0, len(a)-1, 1):

            if a[i] != a[i+1]:
                count += 1
                a.pop(i)
                a.pop(i)
                if len(a)==0:
                    val=False
                break
        finLen = len(a)
        if initLen == finLen:
            val = False

    if count % 2 == 0:
        output.append("NET")
    else:
        output.append("DA")

for x in output:
    print(x)