import fresh_tomatoes
import media

toy_story=media.Movie("TOY STORY",
                      "A story of a boys and his toys that come to life",
                      "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
                      "https://www.youtube.com/watch?v=4KPTXpQehio")
#print (toy_story.storyline)

avatar= media.Movie("Avatar",
                    "A marine on an elien planet",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

movies=[toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
