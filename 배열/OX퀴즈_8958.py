T = int(input())
for i in range(T):
    l = list(input())
    result =0
    cnt = 0
    for j in range(len(l)):
        if l[j]=='O':
            cnt+=1
            result+=cnt
        else :
            cnt = 0
    print(result)