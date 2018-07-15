# TODO: Allow for keywords in initalization of scraper
    # TODO: Fix the way the array is returned in getKeywords function
    # TODO: Add error checking for unfound file or an empty file/array
# TODO: Save distinct reports
    # TODO: Date and Time - Complete
# TODO: Run daily
    #...?
# TODO: Text alert to phone on new news reports about keywords supplied
    #texting module?
import os
import csv
import time
import urllib.request
from bs4 import BeautifulSoup

#Save report to specified directory
def saveReport(returnedContentArray, folderPath):
    reportNumber = time.asctime(time.localtime(time.time())).replace(":", "")
    with open(folderPath + reportNumber + '.txt', "w") as f:
        f.write("\n".join(returnedContentArray))

#Take a file path and return the contents of the file as a keyword array
def getFileContents(filePath):
    contentArray = []
    with open(filePath, "r") as f:
        r = csv.reader(f, delimiter = ",")
        for x in r:
            contentArray.append(x)
    return contentArray[0]

class Scraper:
    def __init__(self, sitesFile, keywordsFile, reportPath):
        self.sites = getFileContents(sitesFile)
        self.keys = getFileContents(keywordsFile)
        self.reportPath = reportPath
        self.returnedContent = []

    def scrapeSites(self):
        for x in range(len(self.sites)):
            print(self.sites[x])
            response = urllib.request.urlopen(self.sites[x])
            html = response.read()
            bfsp = BeautifulSoup(html, "html.parser")
            for tag in bfsp.find_all('a'):
                url = tag.get('href')
                if url and 'html' and self.keys[4] in url:
                    self.returnedContent.append(self.sites[x] + url)
        print(self.returnedContent)
        saveReport(self.returnedContent, self.reportPath)
Scraper("websites.csv", "keywords.csv", "reports/").scrapeSites()
