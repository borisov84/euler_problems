def problem3():
    digit = 600851475143
    digit_dividers = []
    prime_dividers = []
    # перебираем делители числа
    for i in range(1, int((digit+1)/2)):
        if digit % i == 0:
            # Заносим делители в массив
            if (digit/i or i) not in digit_dividers:
                digit_dividers.append(i)
                digit_dividers.append(int(digit/i))
            else:
                break
    for divs in digit_dividers:
        if isprime(divs):
            prime_dividers.append(divs)
    print(prime_dividers[-1])


def isprime(div):
    count_divs = 0
    for i in range(1, div+1):
        if div % i == 0:
            count_divs += 1
            if count_divs > 2:
                break
    if count_divs > 2:
        return False
    else:
        return True


if __name__ == '__main__':
    problem3()
