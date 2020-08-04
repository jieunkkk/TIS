T = int(input())
for i in range(T):
    N = int(input())
    ai_li = list(map(int, input().split()))
    
    result = max(ai_li)-min(ai_li)



    print('#{} {}'.format(i+1, result))
