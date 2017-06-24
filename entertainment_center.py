import fresh_tomatoes
import media

'''
Add your movies below in the following format:

movie_title = media.Movie("Movie Title",
                            "Summary",
                            "Direct link to poster",
                            "Direct link to trailer")

'''

wrath_of_khan = media.Movie("Wrath of Khan",
                            "Revenge is a dish best served cold.",
                            "https://goo.gl/5HdCXM",
                            "https://www.youtube.com/watch?v=IhYhNyFZqus")

esb = media.Movie("The Empire Strikes Back",
                  "Go to Dagobah, you must.",
                  "https://goo.gl/TRMhsC",
                  "https://www.youtube.com/watch?v=xESiohGGP7g")

brunner = media.Movie("Blade Runner",
                      "Do androids dream of electric sheep?",
                      "https://goo.gl/3RsPH2",
                      "www.youtube.com/watch?v=iYhJ7Mf2Oxs")

the_rocketeer = media.Movie("The Rocketeer",
                            "Spys, rockets, Nazis!",
                            "https://goo.gl/63BN2R",
                            "https://www.youtube.com/watch?v=Gi0Et31E7s4")

hackers = media.Movie("Hackers",
                      "Hack the Planet!",
                      "https://goo.gl/UG3zMB",
                      "https://www.youtube.com/watch?v=Ah7Mx38Sguo")

the_fall = media.Movie("The Fall",
                       "But it's my story! Mine, too.",
                       "https://goo.gl/VTBX8U",
                       "https://www.youtube.com/watch?v=IwsYyRc9j4g")

movies = [wrath_of_khan, esb,
          brunner, the_rocketeer, hackers,
          the_fall]

fresh_tomatoes.open_movies_page(movies)
