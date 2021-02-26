# Coding Challenge 3.3
# Working With CSV

# First, import csv
import csv

# Create three empty lists to use for calculations
years = []
months = []
values = []

# 2. Minimum, Maximum, and Average for Entire Dataset
# Doing this first to help get other parts, they would not work unless this was set up first
# First, open and read in the comma delimited csv file
# The lines will help with getting the average
# Use the next function to skip the header line and avoid errors
with open("co2-ppm-daily.csv") as co2_csv:
    csv_reader = csv.reader(co2_csv, delimiter=',')
    lines = 0
    next(co2_csv)

# Use for/if loop to split the data by years, months, and days (they are together in raw data),
# as well as put years and months into their own lists
    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in years:
            years.append(year)
        if month not in months:
            months.append(month)

# Put values into a list and lines counts the number of data points, which is used for average calculation
        values.append(float(row[1]))
        lines = lines + 1

# Print statements for the minimum, maximum, and average for entire dataset
print("Minimum for Entire Dataset = " + str(min(values)) + " ppm")
print("Maximum for Entire Dataset = " + str(max(values)) + " ppm")
print("Average for Entire Dataset = " + str(sum(values) / len(values)) + " ppm")

# 1. Average for Each Year in Dataset
# First, create empty dictionary to store values for each year
year_value_dict = {}

# Use for loop to create temporary list for each year
# Open and read in the comma delimited csv file
# Use next function to skip the header line and avoid errors
for year in years:
    temp_years = []
    with open("co2-ppm-daily.csv") as co2_csv:
        csv_reader = csv.reader(co2_csv, delimiter=',')
        next(co2_csv)

# Use for/if loop to split years, months, and days (they are together in raw data)
# _co2 needs to be added to year and month, otherwise only the average for last year in data (2017) is given
# Put values into temporary years list
        for row in csv_reader:
            year_co2, month_co2, day = row[0].split("-")
            if year_co2 == year:
                temp_years.append(float(row[1]))

# Populate the dictionary created at beginning with averages for each year
    year_value_dict[year] = str(sum(temp_years) / len(temp_years))

# Print the average for each year from 1958 to 2017
print(year_value_dict)

# 3. Seasonal Averages for Spring, Summer, Fall, and Winter
# First, create empty lists for each season
# Spring consists of March, April, and May
# Summer consists of June, July, and August
# Fall consists of September, October, and November
# Winter consists of December, January, and February
spring = []
summer = []
fall = []
winter = []

# Open and read in the comma delimited csv file
# Use next function to skip header line and avoid errors
with open("co2-ppm-daily.csv") as co2_csv:
    csv_reader = csv.reader(co2_csv, delimiter=',')
    next(co2_csv)

# Use for/if loop to split years, months, and days (they are together in raw data)
# Splitting allows you to put the values for the three months for each season into their own list
    for row in csv_reader:
        year, month, day = row[0].split("-")
        if month == "03" or month == "04" or month == "05":
            spring.append(float(row[1]))
        if month == "06" or month == "07" or month == "08":
            summer.append(float(row[1]))
        if month == "09" or month == "10" or month == "11":
            fall.append(float(row[1]))
        if month == "12" or month == "01" or month == "02":
            winter.append(float(row[1]))

# Print statements for seasonal averages
print("Spring Average = " + str(sum(spring) / len(spring)) + " ppm")
print("Summer Average = " + str(sum(summer) / len(summer)) + " ppm")
print("Fall Average = " + str(sum(fall) / len(fall)) + " ppm")
print("Winter Average = " + str(sum(winter) / len(winter)) + " ppm")

# 4. Anomalies Relative to Means for Entire Timeseries
# First, create object for average for entire timeseries and then create empty dictionary for anomalies
entire_average = sum(values) / len(values)
anomaly_dict = {}

# Open and read in the comma delimited csv file
# Use next function to skip the header line and avoid errors
with open("co2-ppm-daily.csv") as co2_csv:
    csv_reader = csv.reader(co2_csv, delimiter=',')
    next(co2_csv)

# Use for loop to split years, months, and days (they are together in raw data)
# Populate anomaly dictionary with anomalies for each value relative to the mean
    for row in csv_reader:
        year, month, day = row[0].split("-")
        anomaly_dict[year] = float(row[1]) - entire_average

# Print anomalies for each year from 1958 to 2017
print(anomaly_dict)
