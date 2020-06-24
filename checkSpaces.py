import re # For regexp

file = open("./Sample Mockup Model.ifc","r")

ifcSpaceStr = "IFCSPACE"
ifcSpaceTypeStr = "IFCSPACETYPE"
passed = True
warning = False
lines = []
ifcNums = []
lineMatch = []
lineNumber = []
passedList = []
warningList = []
failedList = []

def getLineIndex(ifcNum):
    for i, item in enumerate(ifcNums, 1):
       if item == ifcNum:
          return i - 1


def findWithProperty(line, propertyNum, val):
    # print("Searching for property {} in: {}".format(propertyNum, line))
    properties = line.split(",")
    valueToFind = float(re.sub("[^0-9,.]", "", properties[propertyNum - 1])) # Find ifc using regexp and the property number
    if val == "LINE":
        return lines[getLineIndex(valueToFind)][0] # Return the string only
    elif val == "VAL":
        return valueToFind

for lineNum, data in enumerate(file, 1):
    line = data.splitlines()
    lines.append(line)
    tempLine = line[0]
    try:
        ifcNums.append(int(tempLine[1:tempLine.index(" ")])) # Extract IFC #
        # print(tempLine[1:tempLine.index(" ")])
    except ValueError:
        ifcNums.append(0)

    if any(ifcSpaceStr in s for s in line):
        if not any(ifcSpaceTypeStr in s for s in line): # Makes sure it is only looking in IFCSPACE
            foundLine = findWithProperty(tempLine, 7, "LINE")
            foundLine = findWithProperty(foundLine, 3, "LINE")
            foundLine = findWithProperty(foundLine, 4, "LINE")
            height = findWithProperty(foundLine, 4, "VAL")

            if height >= 2000:
                print("*PASSED* [LINE = {}] [IFC #{}] Height = {}".format(lineNum, ifcNums[lineNum - 1], height))
                passedList.append("*PASSED* [LINE = {}] [IFC #{}] Height = {}".format(lineNum, ifcNums[lineNum - 1], height))
            else:
                print("*FAILED* [LINE = {}] [IFC #{}] Height = {}".format(lineNum, ifcNums[lineNum - 1], height))
                passed = False
                failedList.append("*FAILED* [LINE = {}] [IFC #{}] Height = {}".format(lineNum, ifcNums[lineNum - 1], height))

# Print results
if passed:
  print("\r\nRule 8 PASSED, with the following:")
  for i, item in enumerate(passedList, 1):
    print("     {}".format(item))
    if i == len(passedList):
      print("}")
  print("\r\nRule 8 PASSED. Scroll up for details.\r\n")
else:
  print("\r\nRule 8 FAILED. These spaces PASSED: \r\n{")
  for i, item in enumerate(passedList, 1):
    print("     {}".format(item))
    if i == len(passedList):
      print("}")
  print("\r\nThese spaces FAILED:\r\n{")
  for i, item in enumerate(failedList, 1):
    print("     {}".format(item))
    if i == len(failedList):
      print("}")
  print("\r\nRule 8 FAILED. Scroll up for details.\r\n")
# Close the file to free up resources
file.close()