def isValidWord(word, hand):
    dictCopy = hand.copy()

    retval = True

    for i in range(len(word)):
        if dictCopy.has_key(word[i]):
            if dictCopy[word[i]] > 0:
                dictCopy[word[i]] -= 1
            else:
                retval = False
        else:
            retval = False
    
    return retval

hand = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
word = 'hello'

print isValidWord(word,hand)

hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
word = "honey"

print isValidWord(word,hand)

