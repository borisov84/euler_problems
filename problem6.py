def problem6():
    sum_quot = 0
    quot_sum = 0
    sum = 0
    for i in range(1, 101):
        sum_quot += i ** 2
        sum += i
    quot_sum = sum ** 2
    print(quot_sum - sum_quot)


if __name__ == '__main__':
    problem6()
