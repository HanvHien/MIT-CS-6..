from ps4b import *
def comptest(hand, wordList,n):
    maxVal = 0
    # Create a new variable to store the best word seen so far (initially None) 
    bestWord = '' 
    for w in wordList:
        copyHand = hand.copy()
        retval = True
        for i in range(len(w)):
            if copyHand.has_key(w[i]):
                if copyHand[w[i]] > 0:
                    copyHand[w[i]] -= 1
                else:
                    retval = False
            else:
                retval = False

        if retval == True:
            val = getWordScore(w, n)
            if val > maxVal:
                maxVal = val
                bestWord = w
    return bestWord

wordList = loadWords()

print compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
print compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
print compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)