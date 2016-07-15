s = 'azcboboboegghakl'
substr = 'bob'
count = 0
i = 0

while (s.find(substr, i) != -1):
        count += 1
        i = s.find(substr, i) + 1

print 'Number of times bob occurs is: ' + str(count)
