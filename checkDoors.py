import re # For regexp

file = open("./Sample Mockup Model.ifc","r")

ifcDoorStr = "IFCDOOR("
passed = True
lineMatch = []
lineNumber = []
failedList = []
passedList = []

def findWithProperty(line, propertyNum):
    # print("Searching for property {} in: {}".format(propertyNum, line))
    properties = line.split(",")
    valueToFind = float(re.sub("[^0-9,.]", "", properties[propertyNum - 1])) # Find ifc using regexp and the property number
    return valueToFind

for lineNum, data in enumerate(file, 1):
  line = data.splitlines()

  if any(ifcDoorStr in s for s in line): # Search for ifcDoorStr in line
    tempLine = line[0].upper()
    try:
        ifcNum = int(tempLine[1:tempLine.index(" ")]) # Extract IFC #
    except ValueError:
        ifcNum = "NONE"

    height = findWithProperty(tempLine, 9)

    if height >= 2000:
      print("*PASSED* [LINE = {}] [IFC {}] : Height = {}".format(lineNum, ifcNum, height))
      passedList.append("*PASSED* [LINE = {}] [IFC #{}] Height = {}".format(lineNum, ifcNum, height))
    else:
      print("*FAILED* [LINE = {}] [IFC #{}] : Height = {}".format(lineNum, ifcNum, height))
      passed = False
      failedList.append("[LINE = {}] [IFC #{}] : Height = {}".format(lineNum, ifcNum, height))

# Print Results
if passed:
  print("\r\nRule 8 PASSED with the following:")
  for i, item in enumerate(passedList, 1):
    print("     {}".format(item))
    if i == len(passedList):
      print("}")
  print("\r\nRule 8 PASSED. Scroll up for details.\r\n")
else:
  print("\r\nRule 8 FAILED. These doors PASSED:\r\n{")
  for i, item in enumerate(passedList, 1):
    print("     {}".format(item))
    if i == len(passedList):
      print("}")
  print("\r\nThese doors FAILED:\r\n{")
  for i, item in enumerate(failedList, 1):
    print("     {}".format(item))
    if i == len(failedList):
      print("}")
  print("\r\nRule 8 FAILED. Scroll up for details.\r\n")

# Close the file to free up resources
file.close()