class Searcher(object):
    def __init__(self):
        self.video = None

    def add_link(self,link):
        self.video = link

    def get_link(self):
        return self.video
