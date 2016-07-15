animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['e'] = ['flamingo']
animals['e'].append('fly')
animals['e'].append('f')

big = []
for k, v in animals.items():
    big.append([len(v),k])

m = max(big)
big.sort()
s = ''
for l in big:
    if l[0]==m[0]:
        s= s+l[1]+' '
print s