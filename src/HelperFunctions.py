# updates the list (add new number at beginning)
# calculated the average of the non-zero elements
# returns the average in last entry of list

def CalcAverage(list, NewEntry):
    list.insert(0, NewEntry)
    list.pop() # removes last element

    CleanedList = [item for item in list if item != 0]

    average = sum(CleanedList) / len(CleanedList)

    list[-1] = average # replace lat element by average

    return list