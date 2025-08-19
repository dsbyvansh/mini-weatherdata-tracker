#Python project that tracks weather data from a csv file
'''This project contains an attached csv file which has a sample weather data. You can add your own csv file as well'''
import csv

with open("weather_data.csv", newline="",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    
    max_temp = 0
    hottest_day = None
    min_temp = float("inf")
    coolest_day = None
    count = 0
    total_rain = 0
# Finding the hottest day,coolest day and average rainfall   
    for row in reader:
        count += 1
        if row[1]:
            temp_value = int(row[1])
            if temp_value>max_temp:
                max_temp = temp_value
                hottest_day = row[0]
            if temp_value < min_temp:
                min_temp = temp_value
                coolest_day = row[0]
        if row[2]:
            total_rain += int(row[2])  # Incrementing the rainfall values
            avg_rainfall = total_rain/count
        
    print(f"The hottest day was: {hottest_day} with temparature {max_temp}")
    print(f"The coolest day was: {coolest_day} with temparature {min_temp}")
    print(f"The average rainfall is {avg_rainfall}")


