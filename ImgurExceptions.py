class ImgurURLException(Exception):
    def __init__(self, msg=False):
        self.msg = msg

class ImgurConnectionException(Exception):
    def __init__(self, msg=False):
        self.msg = msg