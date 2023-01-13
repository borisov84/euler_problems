def problem9():
    stop = False
    for a in range(1000):
        if not stop:
            for b in range(1000):
                if not stop:
                    for c in range(1000):
                        if a + b + c == 1000 and a < b < c and a**2 + b**2 == c**2:
                            print(a*b*c)
                            stop = True
                            break


if __name__ == "__main__":
    problem9()
