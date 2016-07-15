def SimpleDivide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0  

def FancyDivide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [SimpleDivide(item, denom)
               for item in list_of_numbers]

print FancyDivide([0, 2, 4], 0)