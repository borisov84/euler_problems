def problem4():
    digit = 0
    max_digit = []
    for i in range(100,1000):
        for k in range(100,1000):
            digit = i * k
            if len(str(digit))%2 == 0:
                if str(digit)[:int(len(str(digit))/2):] == str(digit)[len(str(digit)):int(len(str(digit))/2)-1:-1]:
                    max_digit.append(digit)
            else:
                pass
    print(sorted(max_digit)[-1])


if __name__ == '__main__':
    problem4()