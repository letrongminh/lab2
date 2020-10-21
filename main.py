input_age = int(input('How old are you ? \n'))

input_platforms = input('what is your platform? (windows/mac/linux)\n').split(',')


def check_platform():
    if any(platform in row[6].split(';') for platform in input_platforms) or input_platforms == ['']:
        return True
    else:
        return False


input_categories = input('Categories of game: (Multi-player, Online Multi-Player; Local Multi-Player;...)\n').split(',')


def check_category():
    if any(category in row[8].split(';') for category in input_categories) or input_categories == ['']:
        return True
    else:
        return False


input_genres = input('Genres of game: Action, Free to play, Strategy, RPG...\n').split(',')


def check_genre():
    if any(genre in row[9].split(';') for genre in input_genres) or input_genres == ['']:
        return True
    else:
        return False


input_rating = input('The rating important to you? type "yes", if it important \n')
if input_rating == 'yes':
    input_rating = True
else:
    input_rating = False


def check_rating():
    if input_rating is True:
        if row[12].isdigit() and row[13].isdigit():
            if (input_rating is True) and coefficient_rating >= 0:
                return True
            else:
                return False
        else:
            return False
    else:
        print("you don't care about rating")
        return False


input_price = [int(input('price min (dollar)? ')), int(input('price max (dollar)? '))]


def check_price():
    if input_price[0] <= float(row[17]) <= input_price[1]:
        return True
    else:
        return False


with open('steam.csv', encoding='utf-8') as f, open('result_file.txt', 'w', encoding='utf-8') as writing_result:
    writing_result.write('Games for you:\n')
    for row in f:
        row = list(row.split(','))
        if row[12].isdigit() and row[13].isdigit():
            if int(row[12]) > int(row[13]):
                coefficient_rating = int(row[12]) - int(row[13])
        if row[7].isdigit():
            if input_age >= int(row[7]):
                if check_rating() is True and check_category() is True and check_genre() is True \
                        and check_platform() is True and check_price() is True:
                    writing_result.write(row[1] + "\n" + "price: " + row[17] + "\n" + "Category of game: "
                                         + row[9] + "\n" + "coefficient rating = " + str(coefficient_rating)
                                         + "\n-----\n")
                if check_rating() is False and check_category() is True and check_genre() is True \
                        and check_platform() is True and check_price() is True:
                    writing_result.write(row[1] + "\n" + "price: " + row[17] + "\n" + "Category of game: " + row[9] \
                                         + "\n-----\n")
print("the results received in the file result_file.txt")
