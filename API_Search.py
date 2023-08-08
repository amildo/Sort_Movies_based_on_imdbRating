import requests


def get_movie_data(movie_id):
    """

    :param movie_id : you must enter the movie id. you can find it in IMDB website.
    :return: Information such as Title,ImdbRating,Year, ...
    NOTE: if you want to use omdbapi you must sign up in their website and get your free apikey.
    """
    param_d = {"i": movie_id, "r": "json", "apikey": "Enter Your Key Here"}
    url = "https://www.omdbapi.com/"
    data = requests.get(url=url, params=param_d)
    print(data.url)
    return data.json()
