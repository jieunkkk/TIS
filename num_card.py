T = int(input())
for i in range(T):
    N = int(input())
    card_number = list(map(int, input()))
    box = [0]*10
    max_v = 0
    index = 0

    for j in card_number:
        box[j] += 1
    
    for k in range(len(box)):
        if max_v <= box[k]:
            max_v = box[k]
            index = k

    print('#{} {} {}'.format(i+1, index, box[index]))
