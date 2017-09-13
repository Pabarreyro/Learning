#  Call class from separate file
import fresh_tomatoes
import media

# Access class Movie and pass value for attributes...
blade_runner = media.Movie("Blade Runner",
                           "In the 21st century, a corporation develops human clones "
                           "to be used as slaves in colonies outside the Earth, identified as replicants."
                           "In 2019, a former police officer is hired to hunt down a fugitive group "
                           "living undercover in Los Angeles.",
                           "https://upload.wikimedia.org/wikipedia/en/5/53/Blade_Runner_poster.jpg",
                           "https://youtu.be/eogpIG53Cis")

#  The above code allows the following
#  1. Calls Movies.__init__
#  2. self = blade_runner
#  3. title = "Blade Runner"
#  4. synopsis = "In the 21st century..."
#  5. poster_img_url = "<poster link>"
#  6. trailer_url = "<youtube link>"


alien = media.Movie("Alien",
                    "After a space merchant vessel perceives an unknown transmission as a distress call,"
                    "its landing on the source moon finds one of the crew attacked by a mysterious life-form,"
                    "and they soon realize that its life cycle has merely begun.",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                    "https://youtu.be/jQ5lPt9edzQ")


fargo = media.Movie("Fargo",
                    "Jerry Lundegaard's inept crime falls apart due to his and his henchmen's bungling "
                    "and the persistent police work of the quite pregnant Marge Gunderson.",
                    "https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg",
                    "https://youtu.be/h2tY82z3xXU")


third_man = media.Movie("The Third Man",
                        "Pulp novelist Holly Martins travels to shadowy, postwar Vienna, only to find "
                        "himself investigating the mysterious death of an old friend, Harry Lime.",
                        "https://upload.wikimedia.org/wikipedia/en/2/21/ThirdManUSPoster.jpg",
                        "https://youtu.be/F-QWLAndD1E")


il_conformista = media.Movie("Il Conformista",
                              "A weak-willed Italian man becomes a fascist flunky who goes abroad to arrange "
                              "the assassination of his old teacher, now a political dissident.",
                              "https://upload.wikimedia.org/wikipedia/en/9/9a/Original_movie_poster_for_"
                              "the_film_The_Conformist.jpg",
                              "https://youtu.be/QWZO1GLMD2Y")

movies = [blade_runner, alien, fargo, third_man, il_conformista]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)