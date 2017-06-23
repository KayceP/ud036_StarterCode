import fresh_tomatoes
import media

khan = media.Movie("Wrath of Khan", 
	"Revenge is a dish best served cold.", 
	"http://whysoblu.com/wp-content/uploads/2016/04/Star-Trek-Wrath-Of-Khan-Blu-ray.jpg", 
	"https://www.youtube.com/watch?v=IhYhNyFZqus")

empire = media.Movie("The Empire Strikes Back", "A marine on an alien planet", 
	"http://www.craigerscinemacorner.com/Images/ESBposter.jpg", 
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

blade_runner = media.Movie("Blade Runner", 
	"Do androids dream of electric sheep?", 
	"https://20ui41tp7v127j03rcnp97oh-wpengine.netdna-ssl.com/wp-content/uploads/2013/01/bladerunnerbg.jpg", 
	"https://youtu.be/iYhJ7Mf2Oxs")

movies = [khan, empire, blade_runner]

fresh_tomatoes.open_movies_page(movies)