import fresh_tomatoes
import media

iron_giant = media.Movie("Iron Giant",
                        "A young boy discovers a robot",
                        "https://bit.ly/2JDpXVp",
                        "https://www.youtube.com/watch?v=fq2FZdvQXXg")

inception = media.Movie("Inception",
                        "Venture through dreams with Mr. Cobb",
                        "https://bit.ly/2Wa5oGH",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

aladdin = media.Movie("Aladdin",
                     "Genie grants Aladdins wishes",
                     "https://bit.ly/2HuZLdi",
                     "https://www.youtube.com/watch?v=foyufD52aog")

captain_marvel = media.Movie("Captain Marvel",
                             "Intergalatic warrior is put to the test",
                             "https://bit.ly/2TnmLCw",
                             "https://www.youtube.com/watch?v=Z1BCujX3pw8")


wall_e = media.Movie("WALL-E",
                     "A lonely robot finds his juliet and adventure",
                     "https://bit.ly/2kf4PpP",
                     "https://www.youtube.com/watch?v=qGBZWbg_26A")

schoolofrock = media.Movie("School Of Rock",
                             "Underdog rocker Dewey, becomes the teacher",
                             "https://bit.ly/2JMYuRc",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")


movies = [iron_giant, inception, aladdin, captain_marvel, wall_e, schoolofrock]
fresh_tomatoes.open_movies_page(movies)
