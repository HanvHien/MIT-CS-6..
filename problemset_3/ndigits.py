def ndigits(i):

    if abs(i) > 0:
        return 1 + ndigits(abs(i / 10))   # i/10 removes 1 digit
    else:
        return 0                        # else branch
