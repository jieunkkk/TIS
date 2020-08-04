T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    ai_li = list(map(int, input().split()))
    sum_li = []

    for j in range(N-M+1):
        total = 0
        for k in range(j, j+M):
            total += ai_li[k]
        sum_li += [total]
    
    print('#{} {}'.format(i+1, max(sum_li)-min(sum_li)))
