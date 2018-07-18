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
           #first term of each line - fix
    # TODO: Remove rubberducky comments

#Note to self: It is the year of our lord 2018, it's
#okay to add some forloops
#Just not this many...

import re
import urllib.request
from bs4 import BeautifulSoup
import util as util

class Scraper:
    def __init__(self, sitesFile, keywordsFile, reportPath):
        self.sites = util.getFileContents(sitesFile)
        self.keys = util.getFileContents(keywordsFile)
        self.reportPath = reportPath
        self.returnedContent = []

    def scrapeSites(self):
        for x in range(len(self.sites)):
            print("Accessing site: ", self.sites[x])
            response = urllib.request.urlopen(self.sites[x])
            html = response.read()
            bfsp = BeautifulSoup(html, "html.parser")
            for tag in bfsp.find_all('a'):
                link = tag.get('href')
                text = re.findall("-->([a-zA-Z].*?)<!--", str(tag))
                for y in range(len(self.keys)):
                    #print(link, text, self.keys[y])
                    if(self.keys[y] in str(text).lower()):
                        reportPiece = str(text) + "\n" + self.sites[x] + link + "\n\n"
                        self.returnedContent.append(reportPiece)

        util.saveReport(self.returnedContent, self.reportPath)
Scraper("websites.csv", "keywords.csv", "reports/").scrapeSites()
