from bs4 import BeautifulSoup as BS
import re, os, math
import requests as req
from ImgurExceptions import ImgurURLException, ImgurConnectionException


class ImgurDownloader:
    def __init__(self, url, albumName=None, albumKeyInName = False, imageKeyInName = False, overWrite = True):
        if self.testURL(url):
            self.rawURL = url
            self.albumName = albumName
            self.albumKey = None
            self.albumKeyInName = albumKeyInName
            self.imageKeyInName = imageKeyInName
            self.imageIDs = []
            self.getImageURLs()
        else:
            raise ImgurURLException("URL not recognised")

    def testURL(self, url):
        return re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", url)

    def getImageURLs(self):
        self.albumKey = re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", self.rawURL).group(4)
        fullURL = "http://imgur.com/a/"+self.albumKey+"/layout/blog"

        try:
            source = req.get(fullURL).content
        except Exception as e:
            raise ImgurConnectionException(e)
        soup = BS(source, "lxml")
        self.imageIDs = re.findall('.*?{"hash":"([a-zA-Z0-9]+)".*?"ext":"(\.[a-zA-Z0-9]+)".*?', soup.prettify())
        self.imageIDs = self.imageIDs[:int(len(self.imageIDs)/2)] #Since the above regex finds every Id twice

        if self.albumName is None:
            self.albumName = str(soup.find("h1", attrs={"class": "post-title"}).string)
            print(self.albumName)

    def iterImageURLs(self):
        for image in tuple(self.imageIDs):
            yield "http://i.imgur.com/"+image[0]+image[1]

    def printImageURLs(self):
        for image in self.iterImageURLs():
            print(image)

    def saveImages(self):
        #Create directory if none exists
        if self.albumKeyInName:
            self.albumName = self.albumKey + " - " + self.albumName
        if not os.path.isdir(self.albumName):
            os.mkdir(self.albumName)

        counter = 0
        for image in self.imageIDs:
            # Creates a string for the images position and pads with zeros
            name = str(counter+1).zfill(math.ceil(math.log(len(self.imageIDs) + 1, 10)))
            if self.imageKeyInName:
                name += " - "
                name += self.imageIDs[counter][0]
            print(name)
            counter+=1
