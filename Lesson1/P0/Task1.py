"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
different_numbers = []
for text_record in texts:
    if text_record[0] not in different_numbers:
        different_numbers.append(text_record[0])
    if text_record[1] not in different_numbers:
        different_numbers.append(text_record[1])

for call_record in calls:
    if call_record[0] not in different_numbers:
        different_numbers.append(call_record[0])
    if call_record[1] not in different_numbers:
        different_numbers.append(call_record[1])
print("There are {0} different telephone numbers in the records.".format(
    len(different_numbers)))
