movies = {
    "Action": ["Mad Max: Fury Road", "John Wick", "Die Hard", "Gladiator"],
    "Comedy": ["Superbad", "Step Brothers", "The Big Lebowski", "Dumb and Dumber"],
    "Drama": ["Forrest Gump", "The Shawshank Redemption", "Titanic", "The Green Mile"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix", "Blade Runner 2049"],
    "Horror": ["The Conjuring", "A Nightmare on Elm Street", "Get Out", "The Exorcist"]
}

import random

print("Welcome to the Movie Night Recommender!")
print("Available genres: Action, Comedy, Drama, Sci-Fi, Horror")
genre = input("Enter a genre: ")

if genre in movies.keys():
    random_number = random.randint(0, len(movies[genre]) - 1)
    print(f"You should watch: {movies[genre][random_number]}")
else:
    print("Sorry, that genre is not avialable. Try again!")
