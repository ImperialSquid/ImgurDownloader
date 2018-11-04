from ImgurDownloader import ImgurDownloader

test = ImgurDownloader("https://imgur.com/gallery/8EAFpTn", imageKeyInName=True, albumKeyInName=False)
test.printImageURLs()