import gspread
import sys

sa = gspread.service_account()
sheet = sa.open('Blackhole')

work_sheet = sheet.worksheet('Blackhole')
lst = []

with open('logins.txt', 'r') as f:
    for line in f:
        sub = line.split(', ') # extracts the line as a list of a single element to use with gspread.update()
        sub[0] = sub[0].replace('\n', '')
        lst.append(sub)


#probably a better way to do this, will look into it
cell_range = "A2:A" + str(len(lst) + 1)
work_sheet.update(cell_range, lst)

for i in range(len(lst)):
    lst[i][0] = 'https://profile.intra.42.fr/users/' + lst[i][0]

cell_range = "B2:B" + str(len(lst) + 1)
work_sheet.update(cell_range, lst)
