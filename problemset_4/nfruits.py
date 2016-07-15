def nfruits(dFruits, sConsumed):
    """
    dFruits -> a Dict containing type of fruit and its initial quantity
    sConsumed -> as string pattern of the fruits eaten

    returns the Max value of the different types of fruit """
    for i in range(len(sConsumed)):
        if sConsumed[i] in dFruits:
                                            # consuming fruit: subtract 1 from specific fruit
            dFruits[sConsumed[i]] -= 1
            if i < len(sConsumed) - 1:        # has not reached campus
                                            # buy all others
                for j in dFruits:
                    if j != sConsumed[i]:   # if not consumed
                        dFruits[j] += 1
    return max(dFruits.values())
