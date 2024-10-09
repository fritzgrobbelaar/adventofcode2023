import cleaninput
listOfText_Puzzle = cleaninput.getfileInputLinesAsList('input12.txt')


input_sample = '''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.split('\n')

#input_sample='''?###???????? 3,2,1'''.split('\n')

answers = [1, 4, 1, 1, 4, 10]

rows = input_sample
#rows= listOfText_Puzzle

def getRemainingStrings(id, row):
    id = int(id)
    searchString = '#'*id
    print('\nsearching for id', id,' in ', row)
    idsAndStrings = []
    length = len(row)
    for i in range(length):
        print("entered for-loop", i, length)
        if '.' not in row[i:i+len(searchString)]:
            if len(searchString) + i == length:
                print("Last string matched", i, length, searchString, len(searchString))
                if len(row) > id:
                    lookBefore = row[i-1]
                    if lookBefore != '#':
                        print("appending at the end 2 because good", i + len(searchString))
                        idsAndStrings.append('')
                    else:
                        pass
                        print("Look before disqualifies this ", i)
                else:
                    print("appending at the end")
                    idsAndStrings.append('')
            elif len(searchString)+i < length:
                print('index: ', i+len(searchString),  row[i + len(searchString)])
                if (row[i + len(searchString)] in ['?', '.']):
                    if i == 0 or (row[i-1] in ['?', '.']):
                        print("appending", i, 'because ahead is good', row[i + len(searchString)],
                              'and behind is good',row[i-1], 'remaining row', row[i + len(searchString):])
                        idsAndStrings.append(row[i + len(searchString)+1:])
    print("returning", idsAndStrings)
    return idsAndStrings

assert [''] == getRemainingStrings(1, '#')
assert [] == getRemainingStrings(1, '##')
assert [''] == getRemainingStrings(1, '#?')
assert ['', ''] == getRemainingStrings(1, '??')
assert [''] == getRemainingStrings(1, '?#')
assert ['?', ''] == getRemainingStrings(1, '?.?')
assert ['.?',''] == getRemainingStrings(1, '#?.?')
assert ['..??...?##.', '.??...?##.', '...?##.', '..?##.'] == getRemainingStrings(1, '.??..??...?##.')
assert [''] == getRemainingStrings(3, '...?##.')
#print("passed all unit tests")

def calculateRemainingCombinations(row, remainingIds):
    print('processing row', row, remainingIds)
    consumingID = remainingIds[0]
    newRemainingIds = remainingIds[1:]
    remainingStrings = getRemainingStrings(consumingID, row)
    count = 0
    for remaining in remainingStrings:
        if len(newRemainingIds) == 0:
            print("Found no ids remaining! returning", len(remainingStrings), 'string remaining',
                  remainingStrings, 'started with', row)
            return len(remainingStrings)
        else:
            count += calculateRemainingCombinations(remaining, newRemainingIds)
            print("received", count)
    print("returning counts added ", count )
    return count

#assert 1 == calculateRemainingCombinations('#', [1])
#assert 2 == calculateRemainingCombinations('??', [1])
#print('passed')

finalTotal = 0
for i,row in enumerate(rows):
    row, ids = row.split(' ')
    row = row
    ids = ids.split(',')
    result = calculateRemainingCombinations(row, ids)
    print("received result", result)
    #print('comparing, ', result, ' and', answers[i], row, i)
    #assert answers[i] == result
    finalTotal += result
    print('row', i, 'of', len(rows))
#total: 6827
print('finalTotal', finalTotal)

