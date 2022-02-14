# Medical Insurance - Portfolio Project
# CodeCademy Python Portfolio
# Details/Prompt:

import csv
import json
import math
# first thing we want to do is calculate the average age of people in the dataset

medical_records_dictionary = [] # this is actually a list not a dictionary
with open("insurance.txt") as medical_files_csv:
    parsed_csv = csv.DictReader(medical_files_csv)

    for line in parsed_csv:
        medical_records_dictionary.append(line)
print(medical_records_dictionary)
# the above is just a dictionary of medical records for each record

# below is a list comprehension to get values of a particular key in the list of dictionaries
ages = [sub['age'] for sub in medical_records_dictionary]
# ^ definitely a more advanced tricked, had to google this one.
print(ages)
print(len(ages))
def convert_to_int(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])
convert_to_int(ages)  
#print(type(ages[1]))
def calculate_average(list):
    total = 0
    for i in list:
        total += i
    return total
total_ages = calculate_average(ages)
average_age = total_ages / len(ages)
print("The average age of the people in this dataset is " + str(int(average_age)))
print()
# I believe that's that?

# now want to calculate where people are from
southwest_total = 0
southeast_total = 0
northwest_total = 0
northeast_total = 0

list_all_locations = [sub['region'] for sub in medical_records_dictionary]
for region in list_all_locations:
    if region == "southwest":
        southwest_total += 1
    elif region == "southeast":
        southeast_total += 1
    elif region == "northwest":
        northwest_total += 1
    elif region == "northeast":
        northeast_total += 1
    else:
        pass
#print(list_all_locations)
print("There are " + str(southwest_total) + " people from the Southwest region in our dataset.")
print("There are " + str(southeast_total) + " people from the Southeast region in our dataset.")
print("There are " + str(northwest_total) + " people from the Northwest region in our dataset.")
print("There are " + str(northeast_total) + " people from the Northeast region in our dataset.")
print()

# find the average cost of "charges"

charges = [sub['charges'] for sub in medical_records_dictionary]
#print(charges)
#print(type(charges[0]))
charges_float = [float(x) for x in charges]
#print(charges_float)
#print(type(charges_float[0]))
total_charges = 0
for x in charges_float:
    total_charges += x
#print(total_charges)
average_charge = total_charges / len(charges_float)
print("The average charge in our dataset is " +str(round(average_charge,2)))

# find average BMI for total dataset
bmi = [sub['bmi'] for sub in medical_records_dictionary]
float_bmi = [float(x) for x in bmi]
total_bmi = 0
for x in float_bmi:
    total_bmi += x
#print(round(total_bmi,2))
average_bmi = round(total_bmi / len(float_bmi),2)
print("The average BMI for the dataset is " +str(average_bmi))

# next find the average BMI for men, and then for women
male_records = []
for line in medical_records_dictionary:
    if line['sex'] == 'male':
        male_records.append(line)
print(male_records)
female_records = []
for line in medical_records_dictionary:
    if line['sex'] == 'female':
        female_records.append(line)
print(female_records)
# next want to figure out the difference in cost between smoker vs nonsmoker
# not sure how to calculate cost? Unless its same formula as used in previous Med Insurance projects
