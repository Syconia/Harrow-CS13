def insertionSort(ARRAYlist):
    for i in range(len(ARRAYlist)):
        currentValue = ARRAYlist[i]
        pos = i
        while all([pos>0, ARRAYlist[pos - 1] > currentValue]):
            ARRAYlist[pos] = ARRAYlist[pos - 1]
            pos -= 1
        ARRAYlist[pos] = currentValue
    return ARRAYlist


def binarySearch(ARRAYlist, ITEMtarget):
    start = 0
    end = len(ARRAYlist)-1
    mid = (end + start)//2
    while end >= start:
        if ARRAYlist[mid] == ITEMtarget:
            return True, ITEMtarget
        elif ITEMtarget > ARRAYlist[mid]:
            start = mid + 1
        else:
            end = mid - 1
        mid = (end + start)//2
    return False, ITEMtarget


def makeNumerical(ITEMitem):
    itemType = type(ITEMitem)
    returnArray = []
    failed = False
    returnItem = False
    if itemType == list:
        for i in ITEMitem:
            if type(i) == str:
                try:
                    if (float(i) - int(float(i))) != 0.0:
                        returnArray.append(float(i))
                    else:
                        returnArray.append(int(i))
                except ValueError:
                    failed = True
                    break
            else:
                returnArray.append(i)

        if failed:
            return False
        else:
            return returnArray
    elif itemType == float:
        return ITEMitem
    else:
        try:
            returnItem = int(ITEMitem)
        except ValueError:
            try:
                returnItem = float(ITEMitem)
            except ValueError:
                failed = True
        if failed:
            return False
        else:
            return returnItem


listA = [12,444,33,6,8,99,3,23,4,5,"50.4", "50","-34","-3.12",6666,6666,6666,224,890,5432,2445,6,8,990,75445,67864,2113,4332,6789,9900,6.7,6322,98,-111,-1.1,-111]
listA = makeNumerical(listA)
listA = insertionSort(listA)
print(listA)
print(binarySearch(listA, 50.4))
