# import os
# # with open("/home/grey/Desktop/python_100_days/100_days_of_python/csv/weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
# import csv

# with open("/home/grey/Desktop/python_100_days/100_days_of_python/csv/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("/home/grey/Desktop/python_100_days/100_days_of_python/csv/weather_data.csv")
for days in data["day"]:
    print(days)

data_dict = data.to_dict()
print(data_dict)