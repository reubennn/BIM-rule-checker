file = open("./Sample Mockup Model.ifc","r")

ifcDoorStr = "IFCDOOR"
passed = True
warning = False
lineMatch = []
lineNumber = []
warningList = []
failedList = []

for lineNum, data in enumerate(file, 1):
  line = data.splitlines()

  if any(ifcDoorStr in s for s in line): # Search for ifcDoorStr in line
    lineNumber.append(int(lineNum))
    lineMatch.append(line[0])

for i, line in enumerate(lineMatch, 1):
  tempLine = line.upper()
  ifcNum = tempLine[0:line.index(" ")]
  try:
    index = tempLine.index(" X ")
  except ValueError: # If not found, return -1
    index = -1

  if index != -1:
    index += 3
    height = int(line[index: index + 4])
    if height >= 2000:
      print("*PASSED* [LINE = {}] [IFC {}] Height = {}".format(lineNumber[i - 1], ifcNum, height))
    else:
      print("*FAILED* [LINE = {}] [IFC {}] Height = {}".format(lineNumber[i - 1], ifcNum, height))
      passed = False
      failedList.append("[LINE = {}] [IFC {}] Height = {}".format(lineNumber[i - 1], ifcNum, height))
  else:
    print("*WARNING* [LINE = {}] [IFC {}] No Height specified".format(lineNumber[i - 1], ifcNum))
    warning = True
    warningList.append("[LINE = {}] [IFC {}] No Height specified".format(lineNumber[i - 1], ifcNum))

# Print Results
if passed and warning:
  print("\r\nRule 8 PASSED, but with the following WARNINGS \r\n{")
  for i, item in enumerate(warningList, 1):
    print("     {}".format(item))
    if i == len(warningList):
      print("}")
elif passed:
  print("\r\nRule 8 PASSED")
else:
  print("\r\nRule 8 FAILED for the following \r\n{")
  for i, item in enumerate(failedList, 1):
    print("     {}".format(item))
    if i == len(failedList):
      print("}")

# Close the file to free up resources
file.close()