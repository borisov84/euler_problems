def problem7():
    count = 0
    dig = 1
    while(count != 10001):
        dig += 1
        if isprime(dig):
            count += 1
    print(dig)
def isprime(div):
    count_divs = 0
    for i in range(1, div + 1):
        if div % i == 0:
            count_divs += 1
            if count_divs > 2:
                break
    if count_divs > 2:
        return False
    else:
        return True


if __name__ == '__main__':
    problem7()
