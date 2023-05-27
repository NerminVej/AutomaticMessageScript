tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tableData):
    colWidths = [0] * len(tableData) # this is a list that stores how long each table list should be
    # colCounter is the index for the coldWidth that we bump up by one each inner loop
    colCounter = 0
    # find the longest string in each list
    for list in tableData:
        # We put longestString after each inner loop to 0 so we have a clean reset which we can work with
        longestString = 0
        for entry in list:
            if len(entry) > longestString:
                longestString = len(entry)
                colWidths[colCounter] = longestString
        colCounter += 1
    # find the largest value in the colWidths which is rightAdjust
    rightAdjust = max(colWidths)
    for list in tableData:
        for entry in list:
            adjusting = entry.rjust(rightAdjust)


    # len(tableData[0]) takes the length of the first list as a reference value for the length of the end result list
    idx = 0
    for x in range (len(tableData[0])):
        # len(list)-1 since the len(list) would be 3 which would be 4 values but we only want 3 values
        for i in range (len(list)-1):
            adjusting = tableData[i][idx].rjust(rightAdjust)
            print(adjusting,end="")
        print()
        idx += 1






printTable(tableData)

