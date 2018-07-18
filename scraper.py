# TODO: Allow for keywords in initalization of scraper
    # TODO: Add error checking for unfound file or an empty file/array
# TODO: Save distinct reports
    # TODO: Date and Time added as header to reports
    # TODO: Add text divide for each site for readability
    # TODO: Add tags/details about why the article was added
    # TODO: Collect headline for report as well as link
    # TODO: What if the folder path is null?
        # TODO: This may have to be site specific depending on tags used
# TODO: Run daily
    #...?
# TODO: Text alert to phone on new news reports about keywords supplied
    # TODO: research texting module?
# TODO: Create a robust site list and keyword list for testing
    # TODO: Create keyword list
    # TODO: Create site list
    # TODO: Test lists for speed and accuracy
# TODO: Refactoring
    # TODO: getFileContents is just f***ing terrible
    # TODO: Convert functions to class methods
    # TODO: When reading CSV files the reader only reads the
           #first term of each line
    # TODO: Remove rubberducky comments

#Note to self: It is the year of our lord 2018, it's
#okay to add some forloops

#Just not this many...

import csv
import time
import urllib.request
from bs4 import BeautifulSoup

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

class Scraper:
    def __init__(self, sitesFile, keywordsFile, reportPath):
        self.sites = getFileContents(sitesFile)
        self.keys = getFileContents(keywordsFile)
        self.reportPath = reportPath
        self.returnedContent = []
    def scrapeSites(self):
        for x in range(len(self.sites)):
            #DBG
            print("Accessing site: ", self.sites[x])

            #Make responce equal to site data
            response = urllib.request.urlopen(self.sites[x])

            #Make the file into one text string for parsing
            html = response.read()

            #parse the string using bfsp html parser
            bfsp = BeautifulSoup(html, "html.parser")

            #For all the link tagged parts of the object do x
            #find_all is returning an array of link tags to loop over
            for tag in bfsp.find_all('a'):

                #Make a variable equal to the value of the href subtag
                url = tag.get('href')
                #for all keys in the keyterm list
                for y in range(len(self.keys)):

                    #if the url is an actuall HTML doc and
                    #contains a key it is added
                    if url and 'html' and self.keys[y] in url:

                        #Append the full url to the returnedContentArray
                        #to be saved after all the requests have been made
                        self.returnedContent.append(self.sites[x] + url)
        print(self.returnedContent)
        saveReport(self.returnedContent, self.reportPath)
Scraper("websites.csv", "keywords.csv", "reports/").scrapeSites()
