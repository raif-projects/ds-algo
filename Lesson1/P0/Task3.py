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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

calls_from_bangalore_to = []

for call_record in calls:
    if call_record[0].startswith("(080)"):
        calls_from_bangalore_to.append(call_record[1])

unique_numbers_called_to = list(set(calls_from_bangalore_to))
unique_numbers_called_to.sort()

print("The numbers called by people in Bangalore have codes:")
unique_area_codes = []
for number_record in unique_numbers_called_to:
    if number_record.startswith("140") and "140" not in unique_area_codes:
        unique_area_codes.append("140")
        print("140")
    elif number_record.startswith("("):
        area_code_end_index = number_record.find(")") + 1
        if number_record[:area_code_end_index] not in unique_area_codes:
            print(number_record[:area_code_end_index])
            unique_area_codes.append(number_record[:area_code_end_index])
    elif number_record[:4] not in unique_area_codes:
        print(number_record[:4])
        unique_area_codes.append(number_record[:4])

calls_from_bangalore_to_bangalore_count = 0
for call_number in calls_from_bangalore_to:
    if call_number.startswith("(080)"):
        calls_from_bangalore_to_bangalore_count += 1

percentage_count = calls_from_bangalore_to_bangalore_count / \
    len(calls_from_bangalore_to)
print("{:.2} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    percentage_count))
