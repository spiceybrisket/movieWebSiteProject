import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

deadpool = media.Movie("Deadpool",
                     "Wade Wilson is a dishonorably discharged special forces operative working as a mercenary when he meets prostitute Vanessa. They become romantically involved, and a year later she accepts his marriage proposal; however, after Wilson is diagnosed with terminal cancer, he leaves Vanessa without warning so she will not have to watch him die.",
                     "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                     "https://www.youtube.com/watch?v=ONHBaC-pfsk")

school_of_rock = media.Movie("School of Rock",
                     u"No Vacancy, a rock band, performs at a nightclub three weeks before auditioning for the Battle of the Bands. Guitarist Dewey Finn creates on-stage antics, including a failed stage dive that abruptly ends the performance. The next morning, Dewey wakes in the apartment he lives in with Ned Schneebly and his girlfriend, Patty Di Marco. They inform him he must make up for his share of the rent or move out. When Dewey meets No Vacancy at a rehearsal session, he finds out that he has been replaced by another guitarist named Spider. Later, while attempting to sell some of his equipment for rent money, Dewey answers a phone call from Rosalie Mullins, the principal of the Horace Green prep school, inquiring for Ned about a short-term position as a substitute teacher. Desperate for money, Dewey impersonates Ned and is hired. On his first day at the school, Dewey adopts the name \"Mr. S\" and spends his first day behaving erratically, much to the class's confusion.",
                     "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "In 2010, Gil Pender, a successful but creatively unfulfilled Hollywood screenwriter, and his fiance Inez, are in Paris vacationing with Inez's wealthy, conservative parents.",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                           "As punishment for a past rebellion, the 12 districts of the nation of Panem are forced by the Capitol to select two tributes, one boy and one girl between 12 and 18, to fight to the death in the annual Hunger Games until there is only one survivor. In District 12, after her younger sister Primrose is chosen, Katniss Everdeen volunteers to take her place. She and fellow tribute Peeta Mellark are escorted to the Capitol by chaperone Effie Trinket and mentor Haymitch Abernathy, a past victor. Haymitch stresses the importance of gaining sponsors, as they can provide gifts during the Games. While training, Katniss observes the \"Careers\" (Marvel, Glimmer, Cato and Clove), volunteers from Districts 1 and 2, who have trained for the Games from an early age. During a televised interview with Caesar Flickerman, Peeta expresses his love for Katniss, which she initially sees as an attempt to attract sponsors; she later learns his admission is genuine.",
                           "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, deadpool, school_of_rock,
          midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)


