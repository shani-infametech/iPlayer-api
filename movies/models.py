class Media(object):
    def __init__(self, pid):
        self.pid = pid


class Image(Media):
    def __init__(self, pid):
        super().__init__(pid)


class Movie(Media):
    def __init__(self, pid, title, duration, first_broadcast_date, image, short_synopsis):
        super().__init__(pid)
        self.title = title
        self.duration = duration
        self.first_broadcast_date = first_broadcast_date
        self.image = image
        self.short_synopsis = short_synopsis
        self.rating = None


class Rating(object):
    def __init__(self, vote_average, vote_count):
        self.vote_average = vote_average
        self.vote_count = vote_count