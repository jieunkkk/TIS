T = int(input())
for i in range(T):
    K, N, M = map(int, input().split())
    busstop_li = list(map(int, input().split()))
    bs = [0]*N
    for j in busstop_li:
        bs[j] = 1
    
    cnt = 1
    m = 0

    for b in range(len(busstop_li)-1):
        if busstop_li[b+1] - busstop_li[b] > K:
            cnt = 0
    
    if cnt == 1:
        cnt = 0
        m += K
        while m < N:
            if bs[m] == 1:
                cnt += 1
                m += K
            else:
                m -= 1

    print('#{} {}'.format(i+1, cnt))
                


