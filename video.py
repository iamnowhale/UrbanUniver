class Video:
    def __init__(self, title: str, duration: int,
                 adult_mode: bool = False):
        self.time_now = 0
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

