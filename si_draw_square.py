import fresh_tomatoes
import media

toy_story=media.Movie("TOY STORY",
                      "A story of a boys and his toys that come to life",
                      "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=4KPTXpQehio")
#print (toy_story.storyline)

avatar= media.Movie("Avatar",
                    "A marine on an elien planet",
                    "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
