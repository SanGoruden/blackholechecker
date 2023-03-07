import gspread
import datetime as dt

today = dt.date.today()

sa = gspread.service_account()
sheet = sa.open('Blackhole')

work_sheet = sheet.worksheet('Blackhole')
date_list = []

ws_values = work_sheet.get_all_values()
updated_values = [['login', 'intra', 'date', 'note']]

def get_note(login):
    for list in ws_values:
        if login in list:
            return list[3]
    
    return ''

def update_cells():
    with open('.logins', 'r') as f:
        for line in f:
            splitted_line = line.split(' ')
            date = splitted_line[1].replace('\n', '')
            updated_values.append(
                [splitted_line[0],
                'https://profile.intra.42.fr/users/' + splitted_line[0],
                date,
                get_note(splitted_line[0])])
            date_list.append(date)

    work_sheet.update('A1:D' + str(len(updated_values)), updated_values)

# change date cell color to match proximity to blackhole
def apply_colors():
    for i in range(len(date_list)):
        date_object = dt.datetime.strptime(date_list[i], '%d/%m/%Y')

        work_sheet.format('C' + str(i + 2), {
        "backgroundColor": {
        "red": 1.0,
        "green": (date_object.date() - today).days / 30,
        "blue": 0.0
        }
        })


work_sheet.clear()
update_cells()
apply_colors()