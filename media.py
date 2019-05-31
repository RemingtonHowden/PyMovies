import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                    trailer_youtube):
                    #initializes process to create new space and memory for the
                    #new instance of movie it is called upon
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        #upon click, the film trailer is displayed and played
        webbrowser.open(self.trailer_youtube_url)
