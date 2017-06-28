import reports


def export_the_reports(export_file_name, file_name, year, genre, title):
    results = [reports.count_games(file_name), reports.decide(file_name, year), reports.get_latest(file_name),
               reports.count_by_genre(file_name, genre), reports.get_line_number_by_title(file_name, title),
               reports.sort_abc(file_name), reports.get_genres(file_name), reports.when_was_top_sold_fps(file_name)]
    with open(export_file_name, "w") as export_file:
        for item in results:
            export_file.write("%s\n" % item)


export_the_reports("results.txt", "game_stat.txt", "2004", "Simulation", "The Sims")
