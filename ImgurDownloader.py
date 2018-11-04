from bs4 import BeautifulSoup as BS
import re
import requests as req
from ImgurExceptions import ImgurURLException


class ImgurDownloader:
    def __init__(self, url, albumName=None, albumKeyInName = False, imageKeyInName = False, ):
        if self.testURL(self, url):
            self.url = url
            self.albumName = albumName
            self.albumKeyInName = albumKeyInName
            self.imageKeyInName = imageKeyInName
        else:
            raise ImgurURLException("URL not recognised")

    def testURL(self, url):
        return re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", url)

    def download(self):
        albumKey = re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", self.url).group(4)
        fullURL = "http://imgur.com/a/"+albumKey+"/layout/blog"
        print(fullURL)