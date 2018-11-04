from bs4 import BeautifulSoup as BS
import re

class ImgurDownloader:
    def __init__(self, url):
        self.url = url

    def testUrl(self, url):
        return re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", url)