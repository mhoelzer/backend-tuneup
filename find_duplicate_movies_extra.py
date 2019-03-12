    # WAY 1 --> 1st place
    return set(movies)

    # WAY 3 --> 4th place
    dupes = [x for n, x in enumerate(movies) if x not in movies[:n]]
    return dupes
    
    # WAY 4 --> 2nd place
    duplicates = []
    movies_dict = {}
    for movie in movies:
        if movie in movies_dict:
            movies_dict[movie] += 1
        else:
            movies_dict[movie] = 1
        if movies_dict[movie] > 1 and movie not in duplicates:
            duplicates.append(movie)
    return duplicates

    """defunct funct"""
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates