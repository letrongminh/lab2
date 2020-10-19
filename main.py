import csv

age = int(input("How old are you ?\t"))

price = [float(input("min price\t")), float(input("max price\t"))]

categories = input("categories of game: (Multi-player, online [row i]...) \t").split(",")


def category_check():
    if any(category_filter.casefold() for category_filter in categories):
        return 1
    else:
        return 0

genres = input("genres: action, free to play, strategy, rpg...\t")
def genres_check():
    if any((genre_filter.casefold()) for genre_filter in genres):
        return 1
    else:
        return 0

tags = input("tag of game: (action; fps; multiplayer....)\t")
def tag_check():
    if any(tag_filter.casefold() for tag_filter in tags):
        return 1
    else:
        return 0

rating = input("need rating of player ?, if you need, type yes:\t")
if rating == "yes":
    rating = True
else:
    rating = False

def check_final():
    if category_check() + genres_check() + tag_check() == 3:
        return True
    else:
        return False

with open("steam.csv", encoding='utf-8') as df, open("result_file.txt", 'w', encoding='utf-8') as final:
    read_file = csv.reader(df)
    result = csv.writer(final)
    next(read_file)

    for row in read_file:
        ratio_rate = int(row[12]) - int(row[13])
        category_filter = row[8].split(";")
        genre_filter = row[9].split(";")
        tag_filter = row[10].split(";")

        if age >= int(row[7]):
            if (price[0] <= float(row[17]) <= price[1]) \
                    and (rating is True and ratio_rate >= 0) \
                    and (check_final() is True):
                final.write(row[1] + "\t" "price:" + row[17] + "\t" + "type " + row[9] + "\n\n")

print("the results received in the file result_file.txt")
