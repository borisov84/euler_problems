def problem2():
    sum = 0
    first_dig = 1
    sec_dig = 0
    f_dig = 0
    fibonachi = []
    while(True):
        f_dig = first_dig + sec_dig
        if f_dig > 4000000: break
        fibonachi.append(f_dig)
        if f_dig%2 == 0:
            sum += f_dig
        sec_dig = first_dig
        first_dig = f_dig

    print(sum)

if __name__ == '__main__':
    problem2()
