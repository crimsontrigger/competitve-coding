t = int(input())
output = []
for _ in range(t):
    a, b, c, n = map(int, input().split())
    sum_val = a + b + c + n
    list_val = [a, b, c]
    list_val.sort()
    total_diff = (list_val[2] - list_val[0]) + (list_val[2] - list_val[1])
    if (n - total_diff) % 3 == 0 and total_diff <= n:
        output.append('YES')
    else:
        output.append('NO')

for x in output:
    print(x)

t = int(input())
output = []
for _ in range(t):
    n = int(input())
    list_val = [[0, 0]]
    for _ in range(n):
        x_y = list(map(int, input().split()))
        list_val.append(x_y)

    list_val.sort()
    ini_x = list_val[0][0]
    ini_y = list_val[0][1]
    fin_list = []
    for val in list_val:
        if val[0] < ini_x or val[1] < ini_y:
            flag = 0
            break
        else:
            flag = 1
            if val[1] == ini_y:
                diif_val = val[0] - ini_x
                for _ in range(diif_val):
                    fin_list.append('R')
                ini_x = val[0]
            elif val[0] == ini_x:
                diif_val = val[1] - ini_y
                for _ in range(diif_val):
                    fin_list.append('U')
                ini_y = val[1]
            else:
                diif_val_x = (val[0] - ini_x)
                diif_val_y = (val[1] - ini_y)
                for _ in range(diif_val_x):
                    fin_list.append('R')
                for _ in range(diif_val_y):
                    fin_list.append('U')
                ini_x = val[0]
                ini_y = val[1]
    if flag == 1:
        output.append(['YES', fin_list])
    else:
        output.append('NO')

for x in output:
    if x == 'NO':
        print(x)
    else:
        print(x[0])
        str_val = ''
        print(str_val.join(x[1]))
