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
    # Identifies the highest rainfall value in the namedtuple for day; converts to inches; reformats date for output
    rainiest = max(day_entries, key=itemgetter(1))
    inchiest = str(rainiest.rainfall / 100)  # Syntax note: .rainfall/.date to access namedtuple
    date = rainiest.date
    datiest = date.split('-')
    print('{} {}, {}, saw the most rain with {} inches.'.format(datiest[1], datiest[0], datiest[2], inchiest))
    # NEXT: to reformat date

def year_key(day_entry):
    return day_entry.date[-4:]


def group_years(day_entries):
    # Creates a key variable from the year in namedtuple[date]
    year_dict = {}  # Create an empty dictionary
    for item in day_entries:
        year = year_key(item)  # Set the variable to an actual key in the dictionary
        if year not in year_dict:  # Populate dictionary the dictionary
            year_dict[year] = []
        year_dict[year].append(item[1])  # We just need rainfall values
    return year_dict

def sum_totals(year_dict):
    # Sums rainfall values in namedtuples nested in the dictionary
    for year in year_dict:
        year_dict[year] = sum(year_dict[year])  # Replaces list of daily totals with the sum of daily totals
    return year_dict


def rainy_year(year_dict):
    # Identifies the highest rainfall value in the dictionary of rainy years; converts to inches; reformats for output
    rainiest = max(year_dict.items(), key=itemgetter(1))
    inchiest = str(rainiest[1] / 100)
    print('{} saw the most rain with {} inches.'.format(rainiest[0], inchiest))


def test_run(file_path):
    # This function is for test runs only!
    text_lines = open_file(file_path)  # Check
    table_only = slice_text(text_lines)  # Check
    init_totals = split_daily_totals(table_only)  # Check
    final_totals = remove_nondata(init_totals)  # Check
    day_entries = day_tuples(final_totals)  # Check
    rainiest_day = rainy_day(day_entries)  # Check
    year_dict = group_years(day_entries)  # Check
    totals_dict = sum_totals(year_dict)
    rainiest_year = rainy_year(totals_dict)

test_run('sample_rain.txt')

# NEXT: Run search function for days, yours; run averages; scrape website for data

