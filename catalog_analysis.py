import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors":
         ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    all_rat = sum(movie["rating"] for movie in movies)

    return round(all_rat / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    ages = [current_year - movie["year"] for movie in movies]

    return (
        max(ages),
        min(ages),
        math.ceil(sum(ages) / len(ages)),
    )


def duration_in_hours(minutes):
    hours = minutes // 60
    rest_minutes = minutes % 60

    return f"{hours}ч {rest_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "недавние"


def find_non_comedy_movies(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def find_first_masterpiece(movies):
    i = 0

    while i < len(movies):
        movie = movies[i]

        if movie["rating"] > 9.0:
            print(movie["title"])
            break

        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title):
    words = title.split()
    normalized_words = []
    
    for word in words:
        normalized_words.append(word[0].upper()
        + word[1:])

    return " ".join(normalized_words)


def make_slug(title):
    normalized_title = normalize_title(title)
    return normalized_title.lower().replace(' ', '-')


def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))

    return (
        f'"{title}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: '
        f'{genres}'
    )


def titles_sorted_by_rating(movies):
    sorted_movies = sorted(
        movies, key=lambda movie: movie["rating"],
        reverse=True
    )

    return [movie["title"] for movie in sorted_movies]


def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(
        movies, key=lambda movie: movie["rating"],
        reverse=True
    )
    return [
        (movie["title"], movie["rating"])
        for movie in sorted_movies[:n]
    ]


def count_by_genre(movies):
    genre_counts = {}

    for movie in movies:
        for genre in movie["genres"]:
            genre_counts[genre] = (
                    genre_counts.get(genre, 0) + 1)

    return genre_counts


def actor_filmography(movies):
    filmography = {}

    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []

            filmography[actor].append(movie["title"])

    return filmography


def dict_comprehension_title_rating(movies):
    average = average_rating(movies)
    above_average_ratings = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

    return above_average_ratings

if __name__ == "__main__":
    print(average_rating(movies))
    print(catalog_age_stats(movies))
    print(duration_in_hours(155))

    print(rating_tier(9.0))
    print(rating_tier(8.9))
    print(rating_tier(7.0))
    print(rating_tier(6.9))
    print(rating_tier(5.0))
    print(rating_tier(4.9))
    print(decade_label(2021))
    print(decade_label(2020))
    print(decade_label(2015))
    print(decade_label(2014))

    print("Фильмы без жанра comedy:")
    find_non_comedy_movies(movies)
    print("\nПервый фильм с рейтингом выше 9.0:")
    find_first_masterpiece(movies)
    print("\nПроверка случая без шедевров:")
    movies_without_masterpieces = [
        movie for movie in movies if movie["rating"] <= 9.0
    ]
    find_first_masterpiece(movies_without_masterpieces)
    print("\nКоличество фильмов длиннее 120 минут:")
    count_long_movies(movies, threshold=120)
    print(count_long_movies(movies))

    print(normalize_title("silent hours"))
    print(make_slug("Silent Hours"))
    print(format_report_line(movies[7]))

    print(titles_sorted_by_rating(movies))
    print(top_n_by_rating(movies, 3))

    print(count_by_genre(movies))
    print(actor_filmography(movies))
    print(dict_comprehension_title_rating(movies))