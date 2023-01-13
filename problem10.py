def problem10():
    sum_of_prime = 0
     maximum = 2000000
    digits = set(range(2, maximum + 1))
    while digits:
        prime = min(digits)
        sum_of_prime += prime
        digits -= set(range(prime, maximum + 1, prime))
    print(sum_of_prime)


if __name__ == "__main__":
    problem10()
