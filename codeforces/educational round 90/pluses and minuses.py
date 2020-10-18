t = int(input())
output = []
for _ in range(t):
    temp = []
    s = list(map(str, input()))

    res = 0
    init = 0
    ok = False
    while ok == False:
        cur = init
        ok = True
        for i in range(1,len(s)):
            res = res + 1
            if s[i]=='+':
                cur = cur + 1
            else:
                cur = cur-1

            if cur < 0:
                ok = False

    output.append(res)

for x in output:
    print(x)