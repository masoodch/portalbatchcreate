import csv

domain = input("Please enter the customer primary email domain: ")


with open('regatta.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'add user {row[3]} -firstName {row[1]} -lastName {row[0]} -displayName "{row[1]} {row[0]}" -disabled false -primaryEmail {row[1]}@{domain} -groups "App_Basic_package"')
            line_count += 1
    print(f'Processed {line_count} lines.')


