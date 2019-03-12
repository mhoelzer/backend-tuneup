#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "mhoelzer"

import cProfile
import pstats
import timeit
import collections


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def wrapper_profile(*args, **kwargs):
        c_prof = cProfile.Profile()
        c_prof.enable()
        enabled_func = func(*args, **kwargs)
        c_prof.disable()
        sort_by = "cumulative"
        profile_stats = pstats.Stats(c_prof).sort_stats(sort_by)
        profile_stats.print_stats()
        return enabled_func
    return wrapper_profile


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    # remove duplicates = set(); print dups = collections, enumerate, set:
    # # 3rd place
    movie_collection = collections.Counter(movies).items()
    return [movie for movie, count in movie_collection if count > 1]


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # code snippet to be executed only once
    timeit_setup_import = """from __main__ import find_duplicate_movies"""
    # code snippet whose execution time is to be measured
    timeit_stmt = """find_duplicate_movies("movies.txt")"""
    t = timeit.Timer(stmt=timeit_stmt, setup=timeit_setup_import)
    repeats = 7
    numbers = 3
    result = t.repeat(repeat=repeats, number=numbers)
    print("Best time across {} repeats of {} runs per repeat: {}".format(
        repeats, numbers, min(result)/numbers))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))
    print(timeit_helper())


if __name__ == '__main__':
    main()
