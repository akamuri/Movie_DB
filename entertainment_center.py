import media
import fresh_tomatoes
# Creating the Movie objects with all their variables
toy_story = media.Movie("Toy Story",
	"A Story of a Boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc",
	"http://www.imdb.com/title/tt0114709/")

avatar = media.Movie("Avatar",
	"A Marine on an Alien planet",
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=cX0R3mXaod8",
 	"http://www.imdb.com/title/tt0499549/")


school_of_rock = media.Movie("School of rock",
	"jack black teaches kids to Rock out ",
	"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=XCwy6lW5Ixc",
	"http://www.imdb.com/title/tt0332379/")

ratatouille = media.Movie("Ratatouille",
	"A Rat is a Chef in Paris",
	"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk",
	"http://www.imdb.com/title/tt0382932/")

midnight_in_paris = media.Movie("Midnight in Paris",
	"Going back in time to meet authors",
	"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
	"https://www.youtube.com/watch?v=FAfR8omt-CY",
	"http://www.imdb.com/title/tt1605783/")

hunger_games = media.Movie("Hunger Games",
	"A really Real Reality show",
	"https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
	"https://www.youtube.com/watch?v=4S9a5V9ODuY",
    "http://www.imdb.com/title/tt1392170/")


dark_knight = media.Movie("Dark Knight",
	"Christopher Nolan's Batman deals with the Joker",
	"https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
	"https://www.youtube.com/watch?v=EXeTwQWrcwY",
	"http://www.imdb.com/title/tt0468569/")

snatch = media.Movie("Snatch",
	"British gangsters chasing after a Diamond and daggs(dogs)",
	"https://upload.wikimedia.org/wikipedia/en/a/a7/Snatch_ver4.jpg",
	"https://www.youtube.com/watch?v=nd7df-Yv_Z4",
	"http://www.imdb.com/title/tt0208092/")

inception = media.Movie("Inception",
	"Dreams inside dreams inside dreams",
	"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
	"https://www.youtube.com/watch?v=66TuSJo4dZM",
	"http://www.imdb.com/title/tt1375666/")


#placing all the movie objects into an Array
movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games,dark_knight,snatch,inception]

#Running the open_movies_page function that takes in a Array of Movie objects.
fresh_tomatoes.open_movies_page(movies)
