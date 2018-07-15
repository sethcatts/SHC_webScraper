# TODO: Allow for keywords in initalization of scraper
    # TODO: Fix the way the array is returned in getKeywords function
    # TODO: Add error checking for unfound file or an empty file/array
# TODO: Save distinct reports
    #Date and time
# TODO: Run daily
    #...?
# TODO: Text on new news report about keywords supplied
    #Module?
import os
import csv
import urllib.request
from bs4 import BeautifulSoup

#Take a file path and return the contents of the file as a keyword array
def saveReport(returnedContentArray, folderPath):
    pass
def getFileContents(filePath):
    contentArray = []
    with open(filePath, "r") as f:
        r = csv.reader(f, delimiter = ",")
        for x in r:
            contentArray.append(x)
    print("Created content array:", contentArray[0])
    return contentArray[0]
class Scraper:
    def __init__(self, sitesFile, keywordsFile):
        self.sites = getFileContents(sitesFile)
        self.keys = getFileContents(keywordsFile)
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
                    self.returnedContent.append(url)
        print(self.returnedContent)
Scraper("websites.csv", "keywords.csv").scrapeSites()
