months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input('Date: ')

    if '/' in date:
        month,day,year = date.split('/')
        month = int(month)
        if int(month) > 12:
            continue

    elif ',' in date:
        date = date.replace(',', '')
        month,day,year = date.split(' ')
        if month not in months:
            continue
        else:
            month = months.index(month) + 1

    if int(day) <= 31 and len(year) <= 4 :
        day = int(day)
        year = int(year)
        break

print(f'{year}-{month:02}-{day:02}')
