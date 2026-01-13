def is_valid_walk(walk):

    x = y = 0

    for i in walk:
        if i == 'n':
            total += 1
        elif i == 's':
            total -= 1
        elif i == 'e':
            total += 1
        else:
            total -= 1

        print(i)

    if  len(walk) == 10 and x == 0 and y == 0:
        return True
    else:
        return False
