import csv

def add_movies():
    with open('u.item.csv', encoding='latin_1') as f:
        r = csv.reader(f, delimiter='|')
        #Movie = apps.get_model('ratingsapp', 'Movie')
        for line in r:
            print(line[1][:-7])

add_movies()
