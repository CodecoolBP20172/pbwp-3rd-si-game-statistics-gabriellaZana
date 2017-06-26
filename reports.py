import csv

'''def open_input_file(file_name):



def iterating_through_stat():'''



def count_games(file_name):
    amount_of_games = 0
    with open(file_name, "r") as input_file:
        for lines in input_file:
            amount_of_games += 1
    return amount_of_games


def decide(file_name, year):
    game_in_that_year_bool = bool
    games_datas_list = []
    with open(file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter='\t')
        for data in reader:
            games_datas_list.append(data)
    for sublist in games_datas_list:
        if year in sublist:
            game_in_that_year_bool = True
    return game_in_that_year_bool


def get_latest(file_name):
    games_datas_list = []
    years = []
    with open(file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter='\t')
        for data in reader:
            games_datas_list.append(data)
    for sublist in games_datas_list:
        for item in sublist:
            if len(item) == 4:
                years.append(item)
    for item in years:
        if "." in item:
            years.remove(item)
    latest_game = str(games_datas_list[years.index(max(years))][0])
    return latest_game


def count_by_genre(file_name, genre):
    games_datas_list = []
    genres = []
    result = 0
    with open(file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter='\t')
        for data in reader:
            games_datas_list.append(data)
    for sublist in games_datas_list:
        for item in sublist:
            if item == sublist[3]:
                genres.append(item)
    for item in genres:
        if item == genre:
            result += 1
    return result


def get_line_number_by_title(file_name, title):
    games_datas_list = []
    megoldas = 0
    line_number = 0
    with open(file_name, "r") as input_file:
        reader = csv.reader(input_file, delimiter='\t')
        for data in reader:
            games_datas_list.append(data)
    for sublist in games_datas_list:
        for item in sublist:
            try:
                if item == title:
                    line_number = games_datas_list.index(sublist)+1
            except:
                raise ValueError
    return line_number


# def sort_abc(file_name):
