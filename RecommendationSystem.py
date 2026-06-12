# recommendation.py

movies = {
    "action": ["John Wick", "The Dark Knight"],
    "comedy": ["Free Guy", "Mr. Bean"],
    "sci-fi": ["Interstellar", "The Matrix"]
}

genre = input("Enter your favorite genre: ").lower()

if genre in movies:
    print("Recommended movies:")
    for movie in movies[genre]:
        print(movie)
else:
    print("No recommendations found.")
