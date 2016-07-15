def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    global f
    a = 2
    b = 3
    if f(a, b) == 5:
        newdict = { d: d1[d] + d2[d] for d in d1 if d in d2}

        d3 = { d: d1[d] for d in d1 if d not in d2 }
        d4 = { d: d2[d] for d in d2 if d not in d1 }
        d3.update(d4)

        return (newdict, d3)
    if f(a, b) == (a>b):
        newdict = {d: False for d in d1 if d1[d] != d2[2]}
        return (newdict, {})


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}


print dict_interdiff(d1, d2)

print dict_interdiff({}, {})
