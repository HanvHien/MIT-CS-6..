aStr = 'bdlnoppqrtuz'
char = "h"
lo = 0

up = len(aStr)
l = up 
h = (lo+up)/2
count = 10           

while count > 0:

    if (l==1):
        if (char == aStr[h]):
            print 'Found 1'
            
        else:
            print 'not Found 1'
        count = 0

    elif (l > 1):
        h = (lo + up) / 2
        if char == aStr[h]:
            print 'Found 2'
        elif char < aStr[h]:
            print '<' , lo, h, up, aStr[h] 
            up = h-1
        elif char > aStr[h]:
            print '>' , lo, h, up, aStr[h:up] 
            lo = h+1
        else:
            print 'not found'
    else:
        print 'string = 0'
    l=up
    count -=1

