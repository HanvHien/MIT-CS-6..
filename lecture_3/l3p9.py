low = 0
high = 100
ans = 0

str1= "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. " 

str2= 'Sorry, I did not understand your input.'

s = raw_input('Please think of a number between 0 and 100! ')

ans = (high+low)/2
while True:
    print 'Is your secret number '+ str(ans) + '?'
    s = raw_input(str1)
    if s.lower() not in 'lhc':
        print str2
    else:
        if s=='l':
            low = ans
        elif s== 'h':
            high = ans
        elif s=='c':
            print 'Game over. Your secret number was: ' + str(ans)
            break

    ans = (high+low)/2

