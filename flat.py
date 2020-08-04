for i in range(10):
    d = int(input())
    box_li = list(map(int, input().split()))

    for j in range(d):
        box_li[box_li.index(max(box_li))] -= 1
        box_li[box_li.index(min(box_li))] += 1
    print('#{} {}'.format(i+1, int(max(box_li)-min(box_li))))