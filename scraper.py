# TODO: Allow for keywords in initalization of scraper
    # TODO: Add error checking for unfound file or an empty file/array
# TODO: Save distinct reports
    # TODO: Date and Time added as header to reports
    # TODO: Add text divide for each site for readability
    # TODO: Add tags/details about why the article was added
    # TODO: Collect headline for report as well as link
    # TODO: What if the folder path is null?
        # TODO: This may have to be site specific depending on tags used
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
        #self._scrapeYahooFinance()
        self._scrapeJobs()
        util.saveReport(self.returnedContent, self.reportPath)

    def _scrapeYahooFinance(self):
        print("Accessing site: ", self.sites[0])
        response = urllib.request.urlopen(self.sites[x])
        html = response.read()
        bfsp = BeautifulSoup(html, "html.parser")
        for tag in bfsp.find_all('a'):
            link = tag.get('href')
            text = re.findall("-->([a-zA-Z].*?)<!--", str(tag))
            for y in range(len(self.keys)):
                if(self.keys[y] in str(text).lower()):
                    reportPiece = str(text) + "\n" + self.sites[x] + link + "\n\n"
                    self.returnedContent.append(reportPiece)
    def _scrapeJobs(self):
		targetTag = '<a>'
        print("Accessing site: ", self.sites[x])
        respose = urllib.request.urlopen(self.sites[0])
        html = response.read()
        bfsp = BeautifulSoup(html, 'html.parser')
        for tag bfsp.find_all(targetTag):
            link = tag.get('href')
            text = '-placeholder-'             
            for i in range(len(self.keys)):
                if(self.keys[i] in str(text).lower())
                    reportPiece = str(text) + "\n" +self.sites[0] + link + "\n"
Scraper("craigslistURL.csv", "keywords.csv", "reports/").scrapeSites()
