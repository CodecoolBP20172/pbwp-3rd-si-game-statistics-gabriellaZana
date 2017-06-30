import reports
import pprint


def print_get_most_played(file_name):
    pprint.pprint(reports.get_most_played(file_name))


def print_sum_sold(file_name):
    pprint.pprint(reports.sum_sold(file_name))


def print_get_selling_avg(file_name):
    pprint.pprint(reports.get_selling_avg(file_name))


def print_count_longest_title(file_name):
    pprint.pprint(reports.count_longest_title(file_name))


def print_get_date_avg(file_name):
    pprint.pprint(reports.get_date_avg(file_name))


def print_get_game(file_name, title):
    pprint.pprint(reports.get_game(file_name, title))


print_get_most_played("game_stat.txt")
print_sum_sold("game_stat.txt")
print_get_selling_avg("game_stat.txt")
print_count_longest_title("game_stat.txt")
print_get_date_avg("game_stat.txt")
print_get_game("game_stat.txt", "The Sims")
