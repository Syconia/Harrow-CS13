import random
import time

# Sorry. Python lists are mutable. This is a bit of a rough workaround.
# Converts a list into a dictionary basically to make it immutable and returns it as a list with the returnValues function.
class constantList():
    def __init__(self, ARRAYlist):
        self.values = {}
        pos = 0
        for i in range(len(ARRAYlist)):
            self.values['v{0}'.format(pos)] = ARRAYlist[i-1]
            pos += 1

    def returnValues(self):
        returnList = []
        pos = 0
        for i in range(len(self.values)):
            returnList.append(self.values['v{0}'.format(pos)])
            pos += 1
        return returnList

    def append(self, other):
        tempList = self.returnValues()
        if type(other) == list:
            for i in other:
                tempList.append(i)
            return constantList(tempList)
        elif type(other) == constantList:
            tempList2 = other.stringValues()
            for i in tempList2:
                tempList.append(i)
            return constantList(tempList)
        else:
            tempList.append(other)
            return constantList(tempList)

# bubble sort, funnily enough
def bubbleSort(ARRAYlist, BOOLascending):
    doneFlag = False
    # while it is not flagged as done, loop
    while not doneFlag:
        # assume it's done...
        doneFlag = True
        # loop through the list beginning from element 0
        for i in range(len(ARRAYlist)-1):
            # if it is bigger than the one to it's right
            if ARRAYlist[i]>ARRAYlist[i+1]:
                # ...until proven it is not
                doneFlag = False
                # store currently value in a temp var
                temp = ARRAYlist[i]
                # make the element i = element i + 1, put the one on the right into the current slot
                ARRAYlist[i] = ARRAYlist[i+1]
                # make element i + 1 = temp var, complete the swap
                ARRAYlist[i+1] = temp
    # just, why not?
    if BOOLascending:
        return (ARRAYlist)
    else:
        returnList = []
        # put everything backwards
        for i in range(len(ARRAYlist)):
            returnList.append(ARRAYlist[-i-1])
        return (returnList)

# generate a random list of numbers
def randomList(INTnumberOfElements, INTlowerBound, INTupperBound):
    returnArray = []
    # loop as many times as there are number of elements
    for i in range(INTnumberOfElements):
        # stick in a random number between the two boundaries (inclusive)
        returnArray.append(random.randint(INTlowerBound, INTupperBound))
    return returnArray

# insertion sort
def insertionSort(ARRAYlist):
    # loop through one less time than as there are elements in a list
    for i in range(len(ARRAYlist)):
        # ignore element 0 as it's already sorted
        currentValue = ARRAYlist[i]
        # have position stored separately
        pos = i
        # if pos is bigger than 0 and the value to the left is bigger than the value being checked, loop
        while all([pos>0, ARRAYlist[pos - 1] > currentValue]):
            # put the one on the left to the current position in list
            ARRAYlist[pos] = ARRAYlist[pos - 1]
            # go one further to the left
            pos -= 1
        # the current value belongs in this position so stick it right in there
        ARRAYlist[pos] = currentValue
    # self explanatory
    return ARRAYlist

# in case you want to stick in a preset list, it comes separate as a procedure
def calcAndPrintResults(ARRAYlist):
    # MAKE THE LIST IMMUTABLE SO PYTHON DOESN'T CHANGE THE SET LIST
    exList = constantList(ARRAYlist)
    #print(exList.values)
    # what's the time at the beginning?
    start = time.time()
    # start the bubble sort and stick the result in a var
    bubbleList = bubbleSort(exList.returnValues(), True)
    # what's the time at the end?
    end = time.time()
    # time taken is final time - start time
    bubbleTime = end - start
    # rinse and repeat with insert sort instead
    start = time.time()
    #print(exList.values)
    insertList = insertionSort(exList.returnValues())
    insertList = insertList
    end = time.time()
    insertTime = end - start
    # make it look halfway presentable while printing results
    print("Bubble sort")
    print(bubbleList)
    print("Time is:", bubbleTime, "seconds")
    print("\nInsert sort")
    print(insertList)
    print("Time is:", insertTime, "seconds")

# so there's a choice for random?
def bubVSinsRandom():
    # you spin me right round, baby right round
    while True:
        # prepare yourself
        print("Type in 1 for random list")
        toStart = input("> ")
        # really, it's the only choice
        if toStart == "1":
            # like a record baby, right round
            while True:
                # get number of elements to be generated in random list
                print("Type in the number of elements")
                noElements = input("> ")
                # general error catching for all those monsters who like to try to break code
                try:
                    # fist, is it an integer
                    noElements = int(noElements)
                    # Cool
                    isInt = True
                # catch wrong data type
                except ValueError:
                    # seriously, why would you? It should be quite self explanatory
                    print("Try again. You monster.\n")
                    isInt = False
                # now, if the int check passes, did you try to sneak in a negative?
                if isInt:
                    # if not
                    if noElements >= 0:
                        # cool. You are a good person. You can move on
                        break
                    else:
                        # nice try.
                        print("Your number of elements is negative.\n")
            # Don't know how the song goes on, but you get it
            while True:
                # and loop it again
                while True:
                    # get lower bound for random list (inclusive)
                    print("Type in the lower bound")
                    lowerBound = input("> ")
                    # same error checking to make sure it's an integer
                    try:
                        lowerBound = int(lowerBound)
                        isInt = True
                    except ValueError:
                        print("Try again. You monster.\n")
                        isInt = False
                    if isInt:
                        break
                # oh, repeat for upper bound
                while True:
                    # get upper bound (inclusive)
                    print("Type in the upper bound")
                    upperBound = input("> ")
                    # because some people are just persistent
                    try:
                        upperBound = int(upperBound)
                        isInt = True
                    except ValueError:
                        print("Try again. You monster.\n")
                        isInt = False
                    if isInt:
                        break
                # upper bound should be bigger than lower bound.
                if upperBound > lowerBound:
                    break
                else:
                    # Learn 2 maths
                    print("You monster. Your lower bound is bigger than your upper bound.\n")
            # and start the results procedure
            calcAndPrintResults(randomList(noElements, lowerBound, upperBound))
            # oh, and end that loop while you're at it
            break
        else:
            # really? You were only given one option.
            print("\nTry again\n")


# Same old write to file. Just with added string concact
def writeFileFormat(STRINGsortType, STRINGdescription, INTlistSize, FLOATtime):
    stringWrite = STRINGsortType + "," + STRINGdescription + "," + str(INTlistSize) + "," + str(FLOATtime) + "\n"
    with open("sortResults.txt", 'a') as f:
        f.write(stringWrite)
    return True


# Decode the file generated. Can make one big array, or make an array for each sort
def fileDecode(FILEfile, BOOLsplitIntoBubOrIns, BOOLindex):
    returnArray = []
    # Same old read file and append lines into array with split and newline removal
    with open(FILEfile, 'r') as f:
        lines = f.readlines()
    for i in lines:
        returnArray.append(i.rstrip('\n').split(','))
    # Indexing so we can see corresponding values
    if BOOLindex:
        counter = 0
        index = 1
        for i in range(len(returnArray)):
            if counter % 2 == 0:
                returnArray[counter].append(index)
            else:
                returnArray[counter].append(index)
                index += 1
            counter += 1
    # If split into two arrays
    if BOOLsplitIntoBubOrIns:
        # index
        counter = 0
        returnBubbleArray = []
        returnInsArray = []
        for i in range(len(returnArray)):
            # if even then it's bubble sort
            if counter % 2 == 0:
                returnBubbleArray.append(returnArray[counter])
            # else it's an insert sort
            else:
                returnInsArray.append(returnArray[counter])
            counter += 1
        return returnBubbleArray, returnInsArray
    # else just return the big list
    else:
        return returnArray


# P.S. Sorry for all the breaks. Got a bit lazy
# P.S.S. I hope you understand the gist of the comments. Got a bit bored of generic comments. Especially nearer to the end.

print("start")

listA = randomList(3000, -1023, 1024)
listA = bubbleSort(listA, False)
listA = constantList(listA)

print("init done")

start = time.time()
bubbleList = bubbleSort(listA.returnValues(), True)
end = time.time()
bubbleTime = end - start

print("bubble done")

start = time.time()
insertList = insertionSort(listA.returnValues())
end = time.time()
insertTime = end - start

print("insert done\n")

print("To sort:", listA.returnValues())
print("Bubble time =", round(bubbleTime, 5))
print("Insert time =", round(insertTime, 5))

writeFileFormat("BUBBLE", "DESCENDING_LIST", len(listA.returnValues()), round(bubbleTime, 5))
writeFileFormat("INSERT", "DESCENDING_LIST", len(listA.returnValues()), round(insertTime, 5))

#print(fileDecode("sortResults.txt", False))

#bubAr, insAr = fileDecode("sortResults.txt", True, True)
#print(bubAr, insAr)

