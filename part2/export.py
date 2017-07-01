import reports


def export_the_reports(export_file_name, file_name, title):
    results = [reports.get_most_played(file_name), reports.sum_sold(file_name), reports.get_selling_avg(file_name),
               reports.count_longest_title(file_name), reports.get_date_avg(file_name),
               reports.get_game(file_name, title),
               reports.count_grouped_by_genre(file_name), reports.get_date_ordered(file_name)]
    with open(export_file_name, "w") as export_file:
        for item in results:
            export_file.write("%s\n" % item)


export_the_reports("results.txt", "game_stat.txt", "The Sims")
