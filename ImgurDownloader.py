from bs4 import BeautifulSoup as BS
import re
import requests as req
from ImgurExceptions import ImgurURLException


class ImgurDownloader:
    def __init__(self, url, albumName=None, albumKeyInName = False, imageKeyInName = False, ):
        if self.testURL(url):
            self.rawURL = url
            self.albumName = albumName
            self.albumKeyInName = albumKeyInName
            self.imageKeyInName = imageKeyInName
            self.imageIDs = []
            self.getImageURLs()
        else:
            raise ImgurURLException("URL not recognised")

    def testURL(self, url):
        return re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", url)

    def getImageURLs(self):
        albumKey = re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", self.rawURL).group(4)
        fullURL = "http://imgur.com/a/"+albumKey+"/layout/blog"

        source = req.get(fullURL).content
        soup = BS(source, "lxml")
        self.imageIDs = re.findall('.*?{"hash":"([a-zA-Z0-9]+)".*?"ext":"(\.[a-zA-Z0-9]+)".*?', soup.prettify())

    def iterImageURLs(self):
        for image in tuple(self.imageIDs):
            yield "http://i.imgur.com/"+image[0]+image[1]

    def printImageURLs(self):
        for image in self.iterImageURLs():
            print(image)

    def saveImages(self):
        pass
