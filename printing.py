import reports
import pprint


def print_count_games(file_name):
    pprint.pprint(reports.count_games(file_name))


def print_decide(file_name, year):
    pprint.pprint(reports.decide(file_name, year))


def print_get_latest(file_name):
    pprint.pprint(reports.get_latest(file_name))


def print_count_by_genre(file_name, genre):
    pprint.pprint(reports.count_by_genre(file_name, genre))


def print_get_line_number_by_title(file_name, title):
    pprint.pprint(reports.get_line_number_by_title(file_name, title))


def print_sort_abc(file_name):
    pprint.pprint(reports.sort_abc(file_name))


def print_get_genres(file_name):
    pprint.pprint(reports.get_genres(file_name))


def print_when_was_top_sold_fps(file_name):
    pprint.pprint(reports.when_was_top_sold_fps(file_name))


def main():
    print_count_games("game_stat.txt")
    print_decide("game_stat.txt", "2004")
    print_get_latest("game_stat.txt")
    print_count_by_genre("game_stat.txt", "Simulation")
    print_get_line_number_by_title("game_stat.txt", "The Sims")
    print_sort_abc("game_stat.txt")
    print_get_genres("game_stat.txt")
    print_when_was_top_sold_fps("game_stat.txt")

main()
