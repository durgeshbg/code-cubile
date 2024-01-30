import csv
import sys

# Checking files in arguments
if len(sys.argv) != 3:
    print('Invalid set of arguments')
    print('Syntax: python dna.py <database> <sequence>')
    sys.exit(1)

# Open files and creating objects
# CSV Object -> database & TEXT Object -> sequence
database_arg = open(sys.argv[1])
database_obj = csv.DictReader(database_arg)
sequence_arg = open(sys.argv[2])
sequence = sequence_arg.read()

# Creating an empty database of STRs same in main database
# Adding new value of success in database
sequencebase = {}
database = []
no_of_strs = 0
for row in database_obj:
    row['success'] = 0
    database.append(row)
    for str in row:
        if str != 'name' and str != 'success' and str not in sequencebase:
            sequencebase[str] = 0
            no_of_strs += 1

# Finding the largest STR match
max_strs = 0
for str in sequencebase:
    for first_str_index in range(len(sequence)):
        first_str = sequence[first_str_index:first_str_index+len(str)]
        if first_str == str:
            for continuos_strs_index in range(first_str_index,len(sequence)-len(str),len(str)):
                secondary_str = sequence[continuos_strs_index:continuos_strs_index+len(str)]
                if secondary_str == str:
                    max_strs += 1
                    if max_strs > sequencebase[str]:
                        sequencebase[str] = max_strs
                else:
                    max_strs = 0
                    break

# Finding a match
for row in database:
    for str in sequencebase:
        if int(row[str]) == sequencebase[str]:
            row['success'] += 1
            if row['success'] == no_of_strs:
                print(row['name'])
                sys.exit(0)
print('No Match')
sys.exit(1)

# Closing the files
database_arg.close()
sequence_arg.close()