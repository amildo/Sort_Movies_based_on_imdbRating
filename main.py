import random
from API_Search import get_movie_data
import time
import json

# Import Movies Id
with open("MoviesIMDB_Id.txt") as myfile:
    data = [item.strip() for item in myfile.readlines()]
# Select 5 ids randomly without replacement
data_Id = random.sample(data, k=5)

# Fetch every movie data by calling get_movie_data and storing in DataSet
# Every 1 sec we fetch new data
DataSet = []
for id in data_Id:
    DataSet.append(get_movie_data(id))
    time.sleep(1)

# Sort movies based on imdbRating
soretd_DataSet = list(map(lambda data: (data.get('Title'), data.get('imdbRating')),
                          sorted(DataSet, key=lambda data: eval(data.get('imdbRating')), reverse=True)))

for film in soretd_DataSet:
    print(film)

# save sorted movies in IMDB_Sorted_based_on_imdbRating.txt
with open("IMDB_Sorted_based_on_imdbRating.txt", "a") as myfile:
    myfile.write(json.dumps(soretd_DataSet))
    myfile.write("\n<===================================================>\n")
