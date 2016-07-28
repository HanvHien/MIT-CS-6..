def genPrimes():
    i = 2
    while True:
        if prime_test(i):
            yield i 
        i +=1
    yield i 

def prime_test(testnum):
    if testnum <=3:
        return True
    for n in range(2, testnum):
        if testnum % n == 0: 
            return False       
    return True