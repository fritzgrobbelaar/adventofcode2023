def buildNumberPyramid(row):
    allRows = [row]
    while set(allRows[-1]) != set([0]):
 #       print('allRows [-1]', allRows[-1])
        row = allRows[-1]
        newRow = []
        for i, value in enumerate(row[1:]):
            newRow.append(row[i + 1] - row[i])
        allRows.append(newRow)
    return allRows

def extrapolatePattern(row):
    pyramid = buildNumberPyramid(row)
    #print("\n\nprocessing:\n", pyramid)
    pyramid.reverse()
    for i, row in enumerate(pyramid):
        if i == 0:
            newNumber = 0
        else:
     #       print('calculate ', row[-1] , ' plus ', pyramid[i-1][-1])
            newNumber = row[-1] + pyramid[i-1][-1]
      #  print("adding new number:", newNumber)
        pyramid[i].append(newNumber)
    return newNumber

def printPyramid(pyramid):
    for row in pyramid:
        print(row)

def extrapolatePatternReversed(row):
    pyramid = buildNumberPyramid(row)
    print("\n\nprocessing:\n", pyramid)
    pyramid.reverse()
    for i, row in enumerate(pyramid):
        if i == 0:
            newNumber = 0
        else:
            print('calculate ', row[0] , ' minus ', pyramid[i-1][0])
            newNumber = row[0] - pyramid[i-1][0]
        #  print("adding new number:", newNumber)
        pyramid[i] = [newNumber] + pyramid[i]
    printPyramid(reversed(pyramid))
    return newNumber


def calculateTotalFromInput(input):
    total = 0
    for row in input:
        total += extrapolatePattern(row)
    return total

def calculateTotalReversedFromInput(input):
    total = 0
    for row in input:
        total += extrapolatePatternReversed(row)
    return total
