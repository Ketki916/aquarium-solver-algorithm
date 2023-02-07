# When changing square to "filled", make sure it was "unfilled" first before updating row or column sum
# You can use count function to find number of already filled squares before filling all of them 

rowMatrix = [[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"]]]

columnMatrix = [[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled", "unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"]]]


rowSums = [2, 4, 4, 3, 3, 5]

columnSums = [3, 4, 1, 4, 5, 4]


rowBlockLengths = []

columnBlockLengths = []

for row in rowMatrix:
    newLengths = []
    for block in row:
        newLengths.append(len(block))
    rowBlockLengths.append(newLengths)

for column in columnMatrix:
    newLengths = []
    for block in column:
        newLengths.append(len(block))
    columnBlockLengths.append(newLengths)


def rowToColumn(rowIndex, rowBlockIndex, blockItemIndex):
    columnIndex = sum(rowBlockLengths[rowIndex][0: rowBlockIndex]) + blockItemIndex
    columnItem = rowIndex + 1
    totalSum = 0
    columnBlockIndex = 0
    for blockLength in columnBlockLengths[columnIndex]:
        if (blockLength + totalSum) < columnItem:
            totalSum = totalSum + blockLength
        elif (blockLength + totalSum) == columnItem:
            columnBlockItemIndex = -1
            break
        else:
            columnBlockItemIndex = columnItem - totalSum - 1
            break
        columnBlockIndex = columnBlockIndex + 1
    return [columnIndex, columnBlockIndex, columnBlockItemIndex]

def columnToRow(columnIndex, columnBlockIndex, blockItemIndex):
    rowIndex = sum(columnBlockLengths[columnIndex][0: columnBlockIndex]) + blockItemIndex
    rowItem = columnIndex + 1
    totalSum = 0
    rowBlockIndex = 0
    for blockLength in rowBlockLengths[rowIndex]:
        if (blockLength + totalSum) < rowItem:
            totalSum = totalSum + blockLength
        elif (blockLength + totalSum) == rowItem:
            rowBlockItemIndex = -1
            break
        else:
            rowBlockItemIndex = rowItem - totalSum - 1
            break
        rowBlockIndex = rowBlockIndex + 1
    return [rowIndex, rowBlockIndex, rowBlockItemIndex]

# Use more test cases for below function
# Below function returns all the possible combinations of blocks that
# when filled will reach the desired sum for a given row, as well as
# the indices for those blocks in the row

def rowBlockCombinations(blockList, indexList, desiredSum):
    possibleCombinations = []
    possibleCombinationsIndex = []
    if len(blockList) == 1:
        if len(blockList[0]) == desiredSum:
            possibleCombinations.append([blockList[0]])
            possibleCombinationsIndex.append([indexList[0]])
        else:
            return None
    else:
        counter = 0
        while counter < len(blockList):
            if len(blockList[counter]) == desiredSum:
                possibleCombinations.append([blockList[counter]])
                possibleCombinationsIndex.append([indexList[counter]])
            elif len(blockList[counter]) < desiredSum and counter != len(blockList) - 1:
                possibleCombination = rowBlockCombinations(blockList[counter + 1:], indexList[counter + 1:], desiredSum - len(blockList[counter]))
                if not (possibleCombination == None):
                    for i in range(0, len(possibleCombination[0])):
                        answer = [blockList[counter]]
                        answerIndex = [indexList[counter]]
                        if type(possibleCombination[0][i][0]) == list:
                            for j in range(0, len(possibleCombination[0][i])):
                                answer.append(possibleCombination[0][i][j])
                                answerIndex.append(possibleCombination[1][i][j])
                        else:
                            answer.append(possibleCombination[0][i])
                            answerIndex.append(possibleCombination[1][i])
                        possibleCombinations.append(answer)
                        possibleCombinationsIndex.append(answerIndex)
            counter = counter + 1
    if len(possibleCombinations) == 0:
        return None
    else:
        return [possibleCombinations, possibleCombinationsIndex]


# check code for column and row conversions
# use more test cases

rowIndex = 0
for row in rowMatrix:
    extractedBlocks = []
    extractedBlocksIndex = []
    for index in range(0, len(row)):
        if "unfilled" in row[index]:
            extractedBlocks.append(row[index])
            extractedBlocksIndex.append(index)
    combinations = rowBlockCombinations(extractedBlocks, extractedBlocksIndex, rowSums[rowIndex])
    if len(combinations[0]) == 1:
        blockIndex = 0
        for block in combinations[0][0]:
            rowMatrix[rowIndex][combinations[1][0][blockIndex]] = ["filled"] * len(block)
            rowSums[rowIndex] = rowSums[rowIndex] - len(block)
            for blockItemIndex in range(0, len(block)):
                columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                if columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                    columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                    columnSums[columnIndices[0]] = columnSums[columnIndices[0]] - 1
            blockIndex = blockIndex + 1
    else:
        tracker = [0] * len(row)
        currentCombinationIndex = 0
        for currentCombination in combinations[0]:
            blockIndex = 0
            for block in currentCombination:
                tracker[combinations[1][currentCombinationIndex][blockIndex]] = tracker[combinations[1][currentCombinationIndex][blockIndex]] + 1
                blockIndex = blockIndex + 1
            currentCombinationIndex = currentCombinationIndex + 1
        trackerIndex = 0
        for item in tracker:
            if item == len(combinations[0]):
                rowMatrix[rowIndex][trackerIndex] = ["filled"] * len(rowMatrix[rowIndex][trackerIndex])
                rowSums[rowIndex] = rowSums[rowIndex] - len(rowMatrix[rowIndex][trackerIndex])
                for blockItemIndex in range(0, len(rowMatrix[rowIndex][trackerIndex])):
                    columnIndices = rowToColumn(rowIndex, trackerIndex, blockItemIndex)
                    if columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                        columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                        columnSums[columnIndices[0]] = columnSums[columnIndices[0]] - 1
            if item == 0:
                rowMatrix[rowIndex][trackerIndex] = ["x"] *len(rowMatrix[rowIndex][trackerIndex])
                for blockItemIndex in range(0, len(rowMatrix[rowIndex][trackerIndex])):
                    columnIndices = rowToColumn(rowIndex, trackerIndex, blockItemIndex)
                    columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
            trackerIndex = trackerIndex + 1
    rowIndex = rowIndex + 1


rowIndex = 0
for row in rowMatrix:
    blockIndex = 0
    for block in row:
        if len(block) > rowSums[rowIndex]:
            rowMatrix[rowIndex][blockIndex] = ["x"] * len(block)
            for blockItemIndex in range(0, len(rowMatrix[rowIndex][blockIndex])):
                columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
        blockIndex = blockIndex + 1
    rowIndex = rowIndex + 1



columnIndex = 0
for column in columnMatrix:
    blockIndex = 0
    for block in column:
        previousSquareFilled = False
        blockItemIndex = 0
        for blockItem in block:
            if blockItem == "unfilled" and previousSquareFilled == True:
                alreadyFilled = columnMatrix[columnIndex][blockIndex][blockItemIndex: ].count("filled")
                columnMatrix[columnIndex][blockIndex][blockItemIndex: ] = ["filled"] * len(columnMatrix[columnIndex][blockIndex][blockItemIndex: ])
                columnSums[columnIndex] = columnSums[columnIndex] - len(columnMatrix[columnIndex][blockIndex][blockItemIndex: ]) + alreadyFilled
                for secondBlockItemIndex in range(0, len(columnMatrix[columnIndex][blockIndex][blockItemIndex: ])):
                    rowIndices = columnToRow(columnIndex, blockIndex, secondBlockItemIndex)
                    if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "unfilled":
                        rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "filled"
                        rowSums[rowIndices[0]] = rowSums[rowIndices[0]] - 1
            if blockItem == "filled":
                previousSquareFilled = True
            blockItemIndex = blockItemIndex + 1
        blockIndex = blockIndex + 1
    columnIndex = columnIndex + 1