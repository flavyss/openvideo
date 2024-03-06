import webbrowser

class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        webbrowser.open(self.path)

class VideoMP4(Video):
    type = "MP4"

movie = VideoMP4("file:///home/flavyss/Downloads/lacucaracha/lacucarachaaa.mp4")
movie.play()
