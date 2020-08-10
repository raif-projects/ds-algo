"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
september_records = {}

for call_record in calls:
    if "09-2016" in call_record[2]:
        if call_record[0] in list(september_records.keys()):
            september_records[call_record[0]] += int(call_record[3])
        else:
            september_records[call_record[0]] = int(call_record[3])
        if call_record[1] in list(september_records.keys()):
            september_records[call_record[1]] += int(call_record[3])
        else:
            september_records[call_record[1]] = int(call_record[3])

highest_time = 0
highest_number = '0'
for (key, value) in september_records.items():
    if value > highest_time:
        highest_time = value
        highest_number = key

print("{0} spent the longest time, {1} seconds, on the phone during September 2016.".format(
    highest_number, highest_time))
