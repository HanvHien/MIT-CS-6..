def ndigits(i):
    # i is either positive or negative
    # convert to positive
    if abs(i) > 0:
        return 1 + ndigits(abs(i/10))   # recursive call 
    else:
        return 0                        # if i = 0, end of recursion loop


print ndigits(-8726585)