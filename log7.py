tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]


for j in range(4):
    for i in range(3):
        print(tableData[i][j],end=" ")
    print("")