import fresh_tomatoes
import media

# Add your movies below.

wrath_of_khan = media.Movie("Wrath of Khan", 
	"Revenge is a dish best served cold.", 
	"https://goo.gl/5HdCXM", 
	"https://goo.gl/1u23gK")

empire_strikes_back = media.Movie("The Empire Strikes Back", 
	"Go to Dagobah, you must.", 
	"https://goo.gl/TRMhsC", 
	"https://goo.gl/b7E95n")

blade_runner = media.Movie("Blade Runner", 
	"Do androids dream of electric sheep?", 
	"https://goo.gl/3RsPH2", 
	"https://goo.gl/Kdd9mK")

movies = [wrath_of_khan, empire_strikes_back, blade_runner]

fresh_tomatoes.open_movies_page(movies)