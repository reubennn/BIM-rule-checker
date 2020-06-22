// Import file
let fs = require("fs");
let data = fs.readFileSync("./Sample Mockup Model.ifc", "utf8");

// Define variables
let ifcDoorStr = "IFCDOOR";
let passed = true;
let warning = false;
let lineMatch = [];
let lineNumber = [];
let warningArr = [];
let failedArr = [];
let tempArr = data.split(/\r?\n/); // Array element for each line

tempArr.forEach((line, index) => {
    if (line.includes(ifcDoorStr)) {
        lineMatch.push(line);
        lineNumber.push(index + 1);
        // console.log((index + 1) + ":" + line);
    }
});

for (i = 0; i < lineMatch.length; i++) {
    // console.log(lineMatch[i]);
    tempLine = lineMatch[i].toUpperCase(); // Resolve some inconsistencies in the file
    let ifcNum = tempLine.substr(0, tempLine.indexOf(" "));
    let index = tempLine.indexOf(" X "); // Use to locate height

    if (index != -1) { // Returns -1 if not found
        index += 3;
        let height = parseInt(tempLine.substring(index, index + 4));
        if (height >= 2000) {
            console.log("{PASSED} [LINE = " + lineNumber[i] + "] [IFC " + ifcNum + "] Height = " + height);
        } else {
            console.log("{FAILED} [LINE = " + lineNumber[i] + "] [IFC " + ifcNum + "] Height = " + height);
            passed = false;
            failedArr.push("[LINE = " + lineNumber[i] + "] [IFC " + ifcNum + "] Height = " + height);
        }
    } else {
        console.log("{WARNING} [LINE = " + lineNumber[i] + "] [IFC " + ifcNum + "] No height specified");
        warning = true;
        warningArr.push("[LINE = " + lineNumber[i] + "] [IFC " + ifcNum + "] No height specified");
    }
}

if (passed && warning) {
    console.log("\r\nRule 3 PASSED, but with the following WARNINGS \r\n{");
    for (i = 0; i < warningArr.length; i++) {
        console.log("    " + warningArr[i]);
        if (i == warningArr.length - 1) {
            console.log("}");
        }
    }
} else if (passed) {
    console.log("\r\nRule 3 PASSED.");
} else {
    console.log("\r\nRule 3 FAILED for the following \r\n{");
    for (i = 0; i < failedArr.length; i++) {
        console.log("    " + failedArr[i]);
        if (i == failedArr.length - 1) {
            console.log("}");
        }
    }
}