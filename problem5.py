def problem5():
    min = 20
    count = 0
    while(True):
        for i in range(1, 21):
            if min % i == 0:
                count += 1
        if count == 20:
            break
        count = 0
        min += 20
    print(min)


if __name__ == '__main__':
    problem5()