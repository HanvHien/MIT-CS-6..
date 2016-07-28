def genPrimes():
    current = 1
    while True:
        current += 1
        while True:
            for i in xrange(2, current // 2 + 1):
                if current % i == 0:
                    current += 1
                    break
            else:
                break
        yield current