from operator import itemgetter
from collections import namedtuple
# Imports namedtuple from collections

day_entry = namedtuple('day_entry', ['date', 'rainfall'])
year_entry = namedtuple('year_entry', ['year', 'rainfall'])
# Creates tuples for daily and annual rain data


def open_file(file_name):
    # Opens .txt file with rain table...
    with open(file_name, 'r') as rain_table:
        rain_lns = rain_table.readlines()
    return rain_lns


def slice_text(lines):
    # Removes lines of text prior to start of table (> line 11)
    rain_tbl = lines[11:]
    return rain_tbl


def split_daily_total(line):
    # Splits A SINGLE row; keeps date/total and assigns them to variable; changes total to integer
    init_split = line.split('   ')
    daily_total = init_split[:2]
    if daily_total[1].isdigit():
        daily_total[1] = int(daily_total[1])  # We'll need for our math later
    return daily_total


def split_daily_totals(lines):
    # Applies the function above to each row in list
    daily_totals = [split_daily_total(line) for line in lines]
    return daily_totals


def remove_nondata(totals):
    # Returns list of relevant daily totals (i.e., non '0' or '-' values)
    return [row for row in totals if type(row[1]) == int]


def day_tuple(row):
    # Casts A SINGLE row into the namedtuple "day_entry"
    return day_entry(row[0], row[1])


def day_tuples(rows):
    # Applies the function above to each row in list
    return [day_tuple(row) for row in rows]


def rainy_day(day_entries):
    rainiest = max(day_entries, key=itemgetter(1))
    inchiest = str(rainiest.rainfall / 100)
    date = rainiest.date
    datiest = date.split('-')
    print('{} {}, {}, saw the most rain, with {} inches.'.format(datiest[1], datiest[0], datiest[2], inchiest))


def test_run(file_path):
    # This function is for test runs only!
    text_lines = open_file(file_path)  # Check
    table_only = slice_text(text_lines)  # Check
    init_totals = split_daily_totals(table_only)  # Check
    final_totals = remove_nondata(init_totals)  # Check
    day_entries = day_tuples(final_totals)  # Check
    rainiest_day = rainy_day(day_entries)  # Check

test_run('sample_rain.txt')




# def rain_records(file_path):
#     # This function will run all of the functions preceding it
#     text_lines = open_file(file_path) #Check
#     table_text_lines = slice_text(text_lines) #Check
#     rows_of_data = split_daily_total(table_text_lines)
#     rows_of_complete_data = cut_non_valid_data(rows_of_data)
#     day_entries = convert_rows_to_day_entries(rows_of_complete_data)
#     day_with_most_rain = get_day_with_most_rain(day_entries)
#     output_day_with_most_rain(day_with_most_rain)
#     year_to_day_entries = group_by_year(day_entries)
#     yearly_entries = convert_from_year_to_day_entries_to_year_entries(year_to_day_entries)
#     year_with_most_rain = get_year_with_most_rain(yearly_entries)
#     output_year_with_most_rain(year_with_most_rain)