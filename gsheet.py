import gspread
import datetime as dt

today = dt.date.today()

sa = gspread.service_account()
sheet = sa.open('Blackhole')

work_sheet = sheet.worksheet('Blackhole')
login_list = []
date_list = []

with open('logins.txt', 'r') as f:
    for line in f:
        login = line.split(' ')[0] # extracts login from line
        login_sub = [login] #gspread.update() function requires a list of list
        date = line.split(' ')[1]
        date = date.replace('\n', '')
        date_sub = [date]
        login_list.append(login_sub)
        date_list.append(date_sub)

#loop does too many API calls
# for i in range(len(login_list)):
#     work_sheet.update_cell(2 + i, 1, login_list[i])

#this does one call but is a little weird
cell_range = "A2:A" + str(len(login_list) + 1)
work_sheet.update(cell_range, login_list)

for i in range(len(login_list)):
    login_list[i][0] = 'https://profile.intra.42.fr/users/' + login_list[i][0]

cell_range = "B2:B" + str(len(login_list) + 1)
work_sheet.update(cell_range, login_list)

cell_range = "C2:C" + str(len(date_list) + 1)
work_sheet.update(cell_range, date_list)

# change date cell color to match proximity to blackhole
for i in range(len(date_list)):
    date_object = dt.datetime.strptime(date_list[i][0], '%d/%m/%Y')

    work_sheet.format('C' + str(i + 2), {
    "backgroundColor": {
    "red": 1.0,
    "green": (date_object.date() - today).days / 30,
    "blue": 0.0
    }
})