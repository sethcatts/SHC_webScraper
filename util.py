    #Save report to specified directory
    def saveReport(returnedContentArray, folderPath):
        reportNumber = time.asctime(time.localtime(time.time())).replace(":", "")
        with open(folderPath + reportNumber + '.txt', "w") as f:
            f.write("\n".join(returnedContentArray))

    #Take a CSV file and return the contents of the file as a content array
    #(File must be one piece of content per line)
    def getFileContents(filePath):
        fileContents = []
        contentArray = []
        with open(filePath, "r") as f:
            r = csv.reader(f, delimiter = ",")
            for x in r:
                fileContents.append(x)
            for x in range(len(fileContents)):
                contentArray.append(fileContents[x][0])
        return contentArray
