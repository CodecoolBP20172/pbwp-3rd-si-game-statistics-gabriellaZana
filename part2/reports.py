import math
import operator


def get_most_played(file_name):
    games_datas_list = []
    title_copies_sold_dict = dict()
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        title_copies_sold_dict[sublist[0]] = float(sublist[1])
    result = max(title_copies_sold_dict, key=title_copies_sold_dict.get)
    return result


def sum_sold(file_name):
    games_datas_list = []
    sold_total = 0
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        sold_total += float(sublist[1])
    return sold_total


def get_selling_avg(file_name):
    games_datas_list = []
    sold_copies = []
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        sold_copies.append(float(sublist[1]))
    return (sum(sold_copies)/len(sold_copies))


def count_longest_title(file_name):
    games_datas_list = []
    titles = []
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        titles.append(sublist[0])
    longest = max(titles, key=len)
    return len(longest)


def get_date_avg(file_name):
    games_datas_list = []
    years = []
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        years.append(int(sublist[2]))
    return (math.ceil(sum(years)/len(years)))


def get_game(file_name, title):
    games_datas_list = []
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        if title == sublist[0]:
            sublist[1] = float(sublist[1])
            sublist[2] = int(sublist[2])
            return sublist


def count_grouped_by_genre(file_name):
    games_datas_list = []
    genres = []
    genre_count_dict = dict()
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        genres.append(sublist[3])
    for item in genres:
        if item not in genre_count_dict.keys():
            genre_count_dict[item] = 1
        elif item in genre_count_dict.keys():
            genre_count_dict[item] += 1
    return genre_count_dict


def get_date_ordered(file_name):
    games_datas_list = []
    title_date_dict = dict()
    with open(file_name) as input_file:
        for line in input_file:
            games_datas_list.append(line.strip().split('\t'))
    for sublist in games_datas_list:
        title_date_dict[sublist[0]] = sublist[2]
    ordered_dict = sorted(title_date_dict.items(), key=operator.itemgetter(0))
    ordered_final = sorted(ordered_dict, key=operator.itemgetter(1), reverse=True)
    result_list = [item[0] for item in ordered_final]
    return result_list
