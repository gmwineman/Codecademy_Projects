import csv
import json
import math

medical_records_dictionary = [] # this is actually a list not a dictionary
with open("insurance.txt") as medical_files_csv:
    parsed_csv = csv.DictReader(medical_files_csv)

    for line in parsed_csv:
        medical_records_dictionary.append(line)
print(medical_records_dictionary)
print() #adding blank print statements to break sections up

# going to find what region everyone in the dataset is from
southwest_total = 0
southeast_total = 0
northwest_total = 0
northeast_total = 0

list_all_locations = [sub['region'] for sub in medical_records_dictionary] #def a more advanced method, that was found off google
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

# next going to break down the entire record set by sex
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
print() #adding blank print statements to break sections up

# now calc average age, bmi, and charges for the entire dataset AND both men and women
#average charges for all
print("Charges Calculations")
all_charges = [sub['charges'] for sub in medical_records_dictionary]
charges_float = [float(x) for x in all_charges]
total_charges = 0
for x in charges_float:
    total_charges += x
average_charge = total_charges / len(charges_float)
print("The average charges for our dataset is " +str(round(average_charge,2)))

male_charges = [sub['charges'] for sub in male_records]
male_charges_float = [float(x) for x in male_charges]
total_charges = 0
for x in male_charges_float:
    total_charges += x
average_male_charge = total_charges / len(male_charges_float)
print("The average charges for males in our dataset is " + str(round(average_male_charge,2)))

female_charges = [sub['charges'] for sub in female_records]
female_charges_float = [float(x) for x in female_charges]
total_charges = 0
for x in female_charges_float:
    total_charges += x
average_female_charge = total_charges / len(female_charges_float)
print("The average charges for females in our dataset is " + str(round(average_female_charge,2)))

print() #creating space between types of calculations
#Age is next
print("Ages Calculations")
ages = [sub['age'] for sub in medical_records_dictionary]
ages_int = [int(x) for x in ages]
total_ages = 0
for x in ages_int:
    total_ages += x
average_age = total_ages / len(ages_int)
print("The average age for this dataset is " + str(round(average_age,2)))

male_ages = [sub['age'] for sub in male_records]
male_ages_int = [int(x) for x in male_ages]
total_ages = 0
for x in male_ages_int:
    total_ages += x
average_male_age = total_ages / len(male_ages_int)
print("The average age of the males in our dataset is " + str(round(average_male_age,2)))

female_ages = [sub['age'] for sub in female_records]
female_ages_int = [int(x) for x in female_ages]
total_ages = 0
for x in female_ages_int:
    total_ages += x
average_female_age = total_ages / len(female_ages_int)
print("The average age of the females in our dataset is " +str(round(average_female_age,2)))

# Next is bmi
print("BMI Calculations")

bmi = [sub['bmi'] for sub in medical_records_dictionary]
bmi_float = [float(x) for x in bmi]
total_bmi = 0
for x in bmi_float:
    total_bmi += 0
average_bmi = total_bmi / len(bmi_float)
print("The average BMI for the dataset is " + str(round(average_bmi,2)))
