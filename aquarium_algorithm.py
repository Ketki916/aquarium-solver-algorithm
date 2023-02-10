
import copy

''' rowMatrix = [[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled"], ["unfilled"]],
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


originalRowSums = [2, 4, 4, 3, 3, 5]

originalColumnSums = [3, 4, 1, 4, 5, 4] '''

''' rowMatrix = [[["unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled"]],
[["unfilled", "unfilled", "unfilled", "unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled", "unfilled"]]]

columnMatrix = [[["unfilled", "unfilled"], ["unfilled", "unfilled", "unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"]]] 


originalRowSums = [5, 5, 4, 1, 2, 1]

originalColumnSums = [2, 3, 2, 2, 5, 4] '''

rowMatrix = [[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"], ["unfilled"]]]

columnMatrix = [[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled"]],
[["unfilled", "unfilled"], ["unfilled", "unfilled"], ["unfilled", "unfilled"]]]


originalRowSums = [2, 2, 3, 1, 1, 4]

originalColumnSums = [3, 3, 1, 1, 4, 1]

rowFinished = []
columnFinished = []

for item in originalRowSums:
    if item > 0:
        rowFinished.append(False)

for item in originalColumnSums:
    if item > 0:
        columnFinished.append(False)

rowSums = copy.deepcopy(originalRowSums)

columnSums = copy.deepcopy(originalColumnSums)


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



stop = False   

changes = 0    

while ((False in rowFinished) or (False in columnFinished)) and stop == False:  

    originalChanges = changes 

    rowIndex = 0
    for row in rowMatrix:
        extractedBlocks = []
        extractedBlocksIndex = []
        for index in range(0, len(row)):
            if row[index].count("unfilled") == len(row[index]):    
                extractedBlocks.append(row[index])
                extractedBlocksIndex.append(index)
        combinations = rowBlockCombinations(extractedBlocks, extractedBlocksIndex, rowSums[rowIndex])
        if combinations != None:                                    
            if len(combinations[0]) == 1:
                blockIndex = 0
                for block in combinations[0][0]:
                    rowMatrix[rowIndex][combinations[1][0][blockIndex]] = ["filled"] * len(block)
                    rowSums[rowIndex] = rowSums[rowIndex] - len(block)
                    changes = changes + 1                              
                    for blockItemIndex in range(0, len(block)):
                        columnIndices = rowToColumn(rowIndex, combinations[1][0][blockIndex], blockItemIndex)
                        if columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                            columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                            columnSums[columnIndices[0]] = columnSums[columnIndices[0]] - 1
                            changes = changes + 1                       
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
                        changes = changes + 1                        
                        for blockItemIndex in range(0, len(rowMatrix[rowIndex][trackerIndex])):
                            columnIndices = rowToColumn(rowIndex, trackerIndex, blockItemIndex)
                            if columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                                columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                                columnSums[columnIndices[0]] = columnSums[columnIndices[0]] - 1
                                changes = changes + 1               
                    if item == 0 and ("filled" not in rowMatrix[rowIndex][trackerIndex]):
                        if ("x" not in rowMatrix[rowIndex][trackerIndex]): 
                            changes = changes + 2
                        rowMatrix[rowIndex][trackerIndex] = ["x"] * len(rowMatrix[rowIndex][trackerIndex])
                        for blockItemIndex in range(0, len(rowMatrix[rowIndex][trackerIndex])):
                            columnIndices = rowToColumn(rowIndex, trackerIndex, blockItemIndex)
                            columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                    trackerIndex = trackerIndex + 1
        rowIndex = rowIndex + 1


    rowIndex = 0
    for row in rowMatrix:
        blockIndex = 0
        for block in row:
            if (len(block) > originalRowSums[rowIndex]) and ("x" not in block):   
                rowMatrix[rowIndex][blockIndex] = ["x"] * len(block)
                changes = changes + 1                                   
                for blockItemIndex in range(0, len(rowMatrix[rowIndex][blockIndex])):
                    columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                    columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                    changes = changes + 1                              
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
                    changes = changes + 1                               
                    for secondBlockItemIndex in range(blockItemIndex, len(columnMatrix[columnIndex][blockIndex])): 
                        rowIndices = columnToRow(columnIndex, blockIndex, secondBlockItemIndex)
                        if rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "unfilled":
                            rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "filled"
                            rowSums[rowIndices[0]] = rowSums[rowIndices[0]] - 1
                            changes = changes + 1                    
                    break                                            
                if blockItem == "filled":
                    previousSquareFilled = True
                blockItemIndex = blockItemIndex + 1
            blockIndex = blockIndex + 1
        columnIndex = columnIndex + 1


    rowIndex = 0
    for row in rowMatrix:
        blockIndex = 0
        for block in row:
            alreadyFilled = block.count("filled")
            alreadyExed = block.count("x")         
            if (alreadyFilled > 0) and (alreadyFilled < len(block)):
                rowMatrix[rowIndex][blockIndex] = ["filled"] * len(block)
                rowSums[rowIndex] = rowSums[rowIndex] - (len(block) - alreadyFilled)
                changes = changes + 1                
                for blockItemIndex in range(0, len(rowMatrix[rowIndex][blockIndex])):
                    columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                    if columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                            columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                            columnSums[columnIndices[0]] = columnSums[columnIndices[0]] - 1
                            changes = changes + 1                  
            if (alreadyExed > 0) and (alreadyExed < len(block)):     
                rowMatrix[rowIndex][blockIndex] = ["x"] * len(block)
                changes = changes + 1                               
                for blockItemIndex in range(0, len(rowMatrix[rowIndex][blockIndex])):
                    columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                    columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                    changes = changes + 1                           
            blockIndex = blockIndex + 1
        rowIndex = rowIndex + 1


    rowIndex = 0
    for row in rowMatrix:
        if rowSums[rowIndex] == 0:
            blockIndex = 0
            for block in row:
                if "unfilled" in block:
                    rowMatrix[rowIndex][blockIndex] = ["x"] * len(block)
                    changes = changes + 1                        
                    for blockItemIndex in range(0, len(rowMatrix[rowIndex][blockIndex])):
                        columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                        columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                        changes = changes + 1                     
                blockIndex = blockIndex + 1
        rowIndex = rowIndex + 1


    columnIndex = 0
    for column in columnMatrix:
        if columnSums[columnIndex] == 0:
            blockIndex = 0
            for block in column:
                if "unfilled" in block:
                    blockItemIndex = 0
                    for blockItem in block:
                        if blockItem == "unfilled":
                            columnMatrix[columnIndex][blockIndex][blockItemIndex] = "x"
                            changes = changes + 1                
                            rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                            rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "x"
                            changes = changes + 1                 
                        blockItemIndex = blockItemIndex + 1
                blockIndex = blockIndex + 1
        columnIndex = columnIndex + 1



    columnIndex = 0
    for column in columnMatrix:
        blockIndex = 0
        for block in column:
            if "x" in block:
                for blockItemIndex in range(len(block)-1, -1, -1):
                    if (columnMatrix[columnIndex][blockIndex][blockItemIndex] == "x") and ("unfilled" in columnMatrix[columnIndex][blockIndex][0: blockItemIndex]):   
                        columnMatrix[columnIndex][blockIndex][0: blockItemIndex] = ["x"] * len(columnMatrix[columnIndex][blockIndex][0: blockItemIndex])
                        changes = changes + 1                  
                        for secondBlockItemIndex in range(0, blockItemIndex):
                            rowIndices = columnToRow(columnIndex, blockIndex, secondBlockItemIndex)
                            rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "x"
                            changes = changes + 1               
            blockIndex = blockIndex + 1
        columnIndex = columnIndex + 1



    columnIndex = 0
    for column in columnMatrix:
        blockIndex = 0
        for block in column:
            if len(block) > originalColumnSums[columnIndex]:   
                blockItemIndex = 0
                for blockItem in block:
                    if (blockItem == "unfilled") and (len(block[blockItemIndex:]) > originalColumnSums[columnIndex]): 
                        columnMatrix[columnIndex][blockIndex][blockItemIndex] = "x"
                        changes = changes + 1               
                        rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                        rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "x"
                        changes = changes + 1                 
                    blockItemIndex = blockItemIndex + 1
            blockIndex = blockIndex + 1
        columnIndex = columnIndex + 1



    columnIndex = 0
    for column in columnMatrix:
        numberUnfilled = 0
        for block in column:
            numberUnfilled = numberUnfilled + block.count("unfilled")
        blockIndex = 0
        for block in column:
            if numberUnfilled - block.count("unfilled") < columnSums[columnIndex]:
                for blockItemIndex in range(len(block) - 1, -1, -1):
                    if columnMatrix[columnIndex][blockIndex][blockItemIndex] == "unfilled":  
                        columnMatrix[columnIndex][blockIndex][blockItemIndex] = "filled"
                        columnSums[columnIndex] = columnSums[columnIndex] - 1
                        rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                        rowMatrix[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "filled"
                        rowSums[rowIndices[0]] = rowSums[rowIndices[0]] - 1
                        numberUnfilled = numberUnfilled - 1
                        changes = changes + 2
                    if columnSums[columnIndex] == numberUnfilled - columnMatrix[columnIndex][blockIndex].count("unfilled"):
                        break
            blockIndex = blockIndex + 1
        columnIndex = columnIndex + 1


    rowIndex = 0
    for remainingSum in rowSums:
        if remainingSum == 0:
            rowFinished[rowIndex] = True
        rowIndex = rowIndex + 1

    columnIndex = 0
    for remainingSums in columnSums:
        if remainingSum == 0:
            columnFinished[columnIndex] = True
        columnIndex = columnIndex + 1

    if originalChanges == changes:
        stop = True


guessedSquares = []
guessedValues = []
refillGuesses = True
oneMoreGuess = True



while ((False in rowFinished) or (False in columnFinished)):

    rowReplica = copy.deepcopy(rowMatrix)
    columnReplica = copy.deepcopy(columnMatrix)
    rowSumsReplica = copy.deepcopy(rowSums)
    columnSumsReplica = copy.deepcopy(columnSums)
    rowFinishedReplica = copy.deepcopy(rowFinished)
    columnFinishedReplica = copy.deepcopy(columnFinished)


    if oneMoreGuess == True:
        rowIndex = 0
        breakLoop = False
        for row in rowMatrix:
            blockIndex = 0
            for block in row:
                blockItemIndex = 0
                for blockItem in block:
                    if blockItem == "unfilled" and ([rowIndex, blockIndex, blockItemIndex] not in guessedSquares):
                        guessedSquares.append([rowIndex, blockIndex, blockItemIndex])
                        guessedValues.append("filled")
                        breakLoop = True
                        break
                    blockItemIndex = blockItemIndex + 1
                if breakLoop == True:
                    break
                blockIndex = blockIndex + 1
            if breakLoop == True:
                break
            rowIndex = rowIndex + 1
    

    if oneMoreGuess == True or refillGuesses == True:
        for squareIndex in range(0, len(guessedSquares)):
            rowReplica[guessedSquares[squareIndex][0]][guessedSquares[squareIndex][1]][guessedSquares[squareIndex][2]] = guessedValues[squareIndex]
            if guessedValues[squareIndex] == "filled":
                rowSumsReplica[guessedSquares[squareIndex][0]] = rowSumsReplica[guessedSquares[squareIndex][0]] - 1
            if rowSumsReplica[guessedSquares[squareIndex][0]] == 0:
                rowFinishedReplica[guessedSquares[squareIndex][0]] = True
            columnIndices = rowToColumn(guessedSquares[squareIndex][0], guessedSquares[squareIndex][1], guessedSquares[squareIndex][2])
            columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = guessedValues[squareIndex]
            if guessedValues[squareIndex] == "filled":
                columnSumsReplica[columnIndices[0]] = columnSumsReplica[columnIndices[0]] - 1
            if columnSumsReplica[columnIndices[0]] == 0:
                columnFinishedReplica[columnIndices[0]] = True


    error = False
    noMoreChanges = False
    changes = 0
    refillGuesses = False
    oneMoreGuess = False

    while (error == False) and (noMoreChanges == False) and (False in rowFinishedReplica or False in columnFinishedReplica):

        originalChanges = changes   

        rowIndex = 0
        for row in rowReplica:
            extractedBlocks = []
            extractedBlocksIndex = []
            for index in range(0, len(row)):
                if row[index].count("unfilled") == len(row[index]):     
                    extractedBlocks.append(row[index])
                    extractedBlocksIndex.append(index)
            combinations = rowBlockCombinations(extractedBlocks, extractedBlocksIndex, rowSums[rowIndex])
            if combinations != None:                                  
                if len(combinations[0]) == 1:
                    blockIndex = 0
                    for block in combinations[0][0]:
                        rowReplica[rowIndex][combinations[1][0][blockIndex]] = ["filled"] * len(block)
                        rowSumsReplica[rowIndex] = rowSumsReplica[rowIndex] - len(block)
                        changes = changes + 1                              
                        for blockItemIndex in range(0, len(block)):
                            columnIndices = rowToColumn(rowIndex, combinations[1][0][blockIndex], blockItemIndex)
                            if columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                                columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                                columnSumsReplica[columnIndices[0]] = columnSumsReplica[columnIndices[0]] - 1
                                changes = changes + 1                      
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
                            rowReplica[rowIndex][trackerIndex] = ["filled"] * len(rowReplica[rowIndex][trackerIndex])
                            rowSumsReplica[rowIndex] = rowSumsReplica[rowIndex] - len(rowReplica[rowIndex][trackerIndex])
                            changes = changes + 1                       
                            for blockItemIndex in range(0, len(rowReplica[rowIndex][trackerIndex])):
                                columnIndices = rowToColumn(rowIndex, trackerIndex, blockItemIndex)
                                if columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                                    columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                                    columnSumsReplica[columnIndices[0]] = columnSumsReplica[columnIndices[0]] - 1
                                    changes = changes + 1                
                        if item == 0 and ("filled" not in rowReplica[rowIndex][trackerIndex]):
                            if ("x" not in rowReplica[rowIndex][trackerIndex]):  
                                changes = changes + 2
                            rowReplica[rowIndex][trackerIndex] = ["x"] * len(rowReplica[rowIndex][trackerIndex])
                            for blockItemIndex in range(0, len(rowReplica[rowIndex][trackerIndex])):
                                columnIndices = rowToColumn(rowIndex, trackerIndex, blockItemIndex)
                                columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                        trackerIndex = trackerIndex + 1
            rowIndex = rowIndex + 1


        rowIndex = 0
        for row in rowReplica:
            blockIndex = 0
            for block in row:
                if (len(block) > originalRowSums[rowIndex]) and ("x" not in block):   
                    rowReplica[rowIndex][blockIndex] = ["x"] * len(block)
                    changes = changes + 1                                   
                    for blockItemIndex in range(0, len(rowReplica[rowIndex][blockIndex])):
                        columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                        columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                        changes = changes + 1                              
                blockIndex = blockIndex + 1
            rowIndex = rowIndex + 1



        columnIndex = 0
        for column in columnReplica:
            blockIndex = 0
            for block in column:
                previousSquareFilled = False
                blockItemIndex = 0
                for blockItem in block:
                    if blockItem == "unfilled" and previousSquareFilled == True:
                        alreadyFilled = columnReplica[columnIndex][blockIndex][blockItemIndex: ].count("filled")
                        columnReplica[columnIndex][blockIndex][blockItemIndex: ] = ["filled"] * len(columnReplica[columnIndex][blockIndex][blockItemIndex: ])
                        columnSumsReplica[columnIndex] = columnSumsReplica[columnIndex] - len(columnReplica[columnIndex][blockIndex][blockItemIndex: ]) + alreadyFilled
                        changes = changes + 1                             
                        for secondBlockItemIndex in range(blockItemIndex, len(columnReplica[columnIndex][blockIndex])): 
                            rowIndices = columnToRow(columnIndex, blockIndex, secondBlockItemIndex)
                            if rowReplica[rowIndices[0]][rowIndices[1]][rowIndices[2]] == "unfilled":
                                rowReplica[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "filled"
                                rowSumsReplica[rowIndices[0]] = rowSumsReplica[rowIndices[0]] - 1
                                changes = changes + 1                     
                        break                                              
                    if blockItem == "filled":
                        previousSquareFilled = True
                    blockItemIndex = blockItemIndex + 1
                blockIndex = blockIndex + 1
            columnIndex = columnIndex + 1



        rowIndex = 0
        for row in rowReplica:
            blockIndex = 0
            for block in row:
                alreadyFilled = block.count("filled")
                alreadyExed = block.count("x")           
                if (alreadyFilled > 0) and (alreadyFilled < len(block)):
                    rowReplica[rowIndex][blockIndex] = ["filled"] * len(block)
                    rowSumsReplica[rowIndex] = rowSumsReplica[rowIndex] - (len(block) - alreadyFilled)
                    changes = changes + 1                 
                    for blockItemIndex in range(0, len(rowReplica[rowIndex][blockIndex])):
                        columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                        if columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] == "unfilled":
                                columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "filled"
                                columnSumsReplica[columnIndices[0]] = columnSumsReplica[columnIndices[0]] - 1
                                changes = changes + 1                    
                if (alreadyExed > 0) and (alreadyExed < len(block)):     
                    rowReplica[rowIndex][blockIndex] = ["x"] * len(block)
                    changes = changes + 1                                
                    for blockItemIndex in range(0, len(rowReplica[rowIndex][blockIndex])):
                        columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                        columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                        changes = changes + 1                            
                blockIndex = blockIndex + 1
            rowIndex = rowIndex + 1



        rowIndex = 0
        for row in rowReplica:
            if rowSumsReplica[rowIndex] == 0:
                blockIndex = 0
                for block in row:
                    if "unfilled" in block:
                        rowReplica[rowIndex][blockIndex] = ["x"] * len(block)
                        changes = changes + 1                        
                        for blockItemIndex in range(0, len(rowReplica[rowIndex][blockIndex])):
                            columnIndices = rowToColumn(rowIndex, blockIndex, blockItemIndex)
                            columnReplica[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                            changes = changes + 1                    
                    blockIndex = blockIndex + 1
            rowIndex = rowIndex + 1


        columnIndex = 0
        for column in columnReplica:
            if columnSumsReplica[columnIndex] == 0:
                blockIndex = 0
                for block in column:
                    if "unfilled" in block:
                        blockItemIndex = 0
                        for blockItem in block:
                            if blockItem == "unfilled":
                                columnReplica[columnIndex][blockIndex][blockItemIndex] = "x"
                                changes = changes + 1                 
                                rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                                rowReplica[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "x"
                                changes = changes + 1                 
                            blockItemIndex = blockItemIndex + 1
                    blockIndex = blockIndex + 1
            columnIndex = columnIndex + 1


        columnIndex = 0
        for column in columnReplica:
            blockIndex = 0
            for block in column:
                if "x" in block:
                    for blockItemIndex in range(len(block)-1, -1, -1):
                        if (columnReplica[columnIndex][blockIndex][blockItemIndex] == "x") and ("unfilled" in columnReplica[columnIndex][blockIndex][0: blockItemIndex]):    # made change here
                            columnReplica[columnIndex][blockIndex][0: blockItemIndex] = ["x"] * len(columnReplica[columnIndex][blockIndex][0: blockItemIndex])
                            changes = changes + 1                   
                            for secondBlockItemIndex in range(0, blockItemIndex):
                                rowIndices = columnToRow(columnIndex, blockIndex, secondBlockItemIndex)
                                rowReplica[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "x"
                                changes = changes + 1            
                blockIndex = blockIndex + 1
            columnIndex = columnIndex + 1


        columnIndex = 0
        for column in columnReplica:
            blockIndex = 0
            for block in column:
                if len(block) > originalColumnSums[columnIndex]: 
                    blockItemIndex = 0
                    for blockItem in block:
                        if (blockItem == "unfilled") and (len(block[blockItemIndex:]) > originalColumnSums[columnIndex]):
                            columnReplica[columnIndex][blockIndex][blockItemIndex] = "x"
                            changes = changes + 1                  
                            rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                            rowReplica[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "x"
                            changes = changes + 1                  
                        blockItemIndex = blockItemIndex + 1
                blockIndex = blockIndex + 1
            columnIndex = columnIndex + 1


        columnIndex = 0
        for column in columnReplica:
            numberUnfilled = 0
            for block in column:
                numberUnfilled = numberUnfilled + block.count("unfilled")
            blockIndex = 0
            for block in column:
                if numberUnfilled - block.count("unfilled") < columnSumsReplica[columnIndex]:
                    for blockItemIndex in range(len(block) - 1, -1, -1):
                        if columnReplica[columnIndex][blockIndex][blockItemIndex] == "unfilled": 
                            columnReplica[columnIndex][blockIndex][blockItemIndex] = "filled"
                            columnSumsReplica[columnIndex] = columnSumsReplica[columnIndex] - 1
                            rowIndices = columnToRow(columnIndex, blockIndex, blockItemIndex)
                            rowReplica[rowIndices[0]][rowIndices[1]][rowIndices[2]] = "filled"
                            rowSumsReplica[rowIndices[0]] = rowSumsReplica[rowIndices[0]] - 1
                            numberUnfilled = numberUnfilled - 1
                            changes = changes + 2
                        if columnSumsReplica[columnIndex] == numberUnfilled - columnReplica[columnIndex][blockIndex].count("unfilled"):
                            break
                blockIndex = blockIndex + 1
            columnIndex = columnIndex + 1

        rowIndex = 0
        for remainingSum in rowSumsReplica:
            if remainingSum == 0:
                rowFinishedReplica[rowIndex] = True
            rowIndex = rowIndex + 1

        columnIndex = 0
        for remainingSums in columnSumsReplica:
            if remainingSum == 0:
                columnFinishedReplica[columnIndex] = True
            columnIndex = columnIndex + 1

        if originalChanges == changes:
            noMoreChanges = True

        
        rowIndex = 0
        for value in rowSumsReplica:
            if value < 0:
                error = True
            numberFilled = 0
            numberUnfilled = 0
            for block in rowReplica[rowIndex]:
                numberFilled = numberFilled + block.count("filled")
                numberUnfilled = numberUnfilled + block.count("unfilled")
            if numberFilled != (originalRowSums[rowIndex] - value):
                error = True
            if numberUnfilled < value:
                error = True
            blockIndex = 0
            for block in rowReplica[rowIndex]:
                if ("filled" in rowReplica[rowIndex][blockIndex]) and ("x" in rowReplica[rowIndex][blockIndex]):
                    error = True
                blockIndex = blockIndex + 1
            rowIndex = rowIndex + 1
     

        columnIndex = 0
        for value in columnSumsReplica:
            if value < 0:
                error = True
            numberFilled = 0
            numberUnfilled = 0
            for block in columnReplica[columnIndex]:
                numberFilled = numberFilled + block.count("filled")
                numberUnfilled = numberUnfilled + block.count("unfilled")
            if numberFilled != (originalColumnSums[columnIndex] - value):
                error = True
            if numberUnfilled < value:
                error = True
            blockIndex = 0
            for block in columnReplica[columnIndex]:
                for blockItemIndex in range(len(block) - 1, -1, -1):
                    if (columnReplica[columnIndex][blockIndex][blockItemIndex] == "x") and ("filled" in columnReplica[columnIndex][blockIndex][0:blockItemIndex]):
                        error = True
                blockIndex = blockIndex + 1
            columnIndex = columnIndex + 1

        if (False not in rowFinishedReplica) and (False not in columnFinishedReplica) and error == False:
            rowFinished = [True] * len(rowFinished)
            columnFinished = [True] * len(columnFinished)
            rowMatrix = copy.deepcopy(rowReplica)
            columnMatrix = copy.deepcopy(columnReplica)
            rowSums = copy.deepcopy(rowSumsReplica)
            columnSums = copy.deepcopy(columnSumsReplica)


    if noMoreChanges == True and error == False:
        oneMoreGuess = True

    
    if error == True:
        if (len(guessedValues) != 1) and (guessedValues[-1] == "filled"):
            guessedValues[-1] = "x"
            refillGuesses = True
            continue
        if (len(guessedValues) != 1) and (guessedValues[-1] == "x"):
            if len(guessedValues) == 2:
                guessedValues.pop()
                guessedSquares.pop()
                rowMatrix[guessedSquares[0][0]][guessedSquares[0][1]][guessedSquares[0][2]] = "x"
                columnIndices = rowToColumn(guessedSquares[0][0], guessedSquares[0][1], guessedSquares[0][2])
                columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
                guessedValues.pop()
                guessedSquares.pop()
            else:
                guessedValues.pop()
                guessedSquares.pop()
                guessedValues[-1] = "x"
        if (len(guessedValues) == 1):
            rowMatrix[guessedSquares[0][0]][guessedSquares[0][1]][guessedSquares[0][2]] = "x"
            columnIndices = rowToColumn(guessedSquares[0][0], guessedSquares[0][1], guessedSquares[0][2])
            columnMatrix[columnIndices[0]][columnIndices[1]][columnIndices[2]] = "x"
            guessedValues.pop()
            guessedSquares.pop()


print(rowMatrix)