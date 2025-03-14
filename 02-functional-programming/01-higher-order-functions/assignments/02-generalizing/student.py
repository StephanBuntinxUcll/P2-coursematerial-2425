from movie import *


def count_movies_from_year(movies, year):
    counter = 0
    for movie in movies:
        if movie.year == year:
            counter += 1
    return counter

# print(count_movies_from_year(movies, 2010))


def select_movies_with_actor(movies,actor):
    result_movies = []
    for movie in movies:
        if actor in movie.actors:
            result_movies.append(movie)
    return result_movies

# print(select_movies_with_tom_hanks(movies, "Christian Bale"))

def sum_movie_duration_from_period(movies, from_date, till_date):
    total_duration = 0
    for movie in movies:
        if movie.year >= from_date and movie.year < till_date:
            total_duration += movie.runtime
    return total_duration

# print(sum_movie_duration_from_period(movies, 2010, 2010))

def get_directors_for_actor(movies, direct):
    directors = []
    for movie in movies:
        if direct in movie.actors:
            directors.append(movie.director)
    return directors

# print(get_directors_for_actor(movies, "Christian Bale"))


def find_string_starting_with(strings, letter):
    for string in strings:
        if len(string) != 0 and string[0].lower() == letter:
            return string
    return None

# print(find_string_starting_with_a(["greek", "pantera", "fantastic", "achilles", "brave", "cook", "a-train" ], "c"))


def find_number_greater_than(numbers, threshold):
    for number in numbers:
        if number > threshold:
            return number
    return None

# print(find_number_greater_than([15, 25,41, 1, 89, 99, 55, 200, 360 , 5, 84, 150], 15))