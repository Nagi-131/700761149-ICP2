inches = list(map(int, input().split(" ")))
cmList = []
cm_comprehensions = []

# Nested loop method
for each in inches :
    cm  = 2.54 * each
    cmList.append(cm)

print ("Height in cm - Nested Interactive loop method \n", cmList)

# List Comprehension method
cm_comprehensions = [(height * 2.54) for height in inches]

print ("Height in cm - List Comprehension method \n", cm_comprehensions)
