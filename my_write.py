import my_parser as p
import datetime

def check_if_valid(date_str):
    count = 0
    for i in date_str:
        if (i == '/'):
            count += 1
    if count != 2:
        return 1
    day,month,year = date_str.split('/')
    isValidDate = True
    try :
        datetime.datetime(int(year), int(month), int(day))
    except ValueError :
        isValidDate = False
    if (isValidDate) :
        return 0
    else :
        return 1


def write_info(info):
    count = 0
    for i in info:
        count += 1
    if count == 0:
        fd = open("info.json", 'w')
        return 0
    count = 1
    fd = open("info.json", 'w')
    fd.write("[\n")
    for element in info:
        if count != 1:
            fd.write(",\n")
        fd.write("\t{\n\t\t")
        fd.write('"id": ' + str(count) + ',\n\t\t')
        fd.write('"Company": ')
        fd.write('"' + element[0] + '",\n\t\t')
        fd.write('"Speciality": ')
        fd.write('"' + element[1] + '",\n\t\t')
        fd.write('"Date": ')
        fd.write('"' + element[2] + '",\n\t\t')
        fd.write('"Reply": ')
        fd.write('"' + element[3] + '"\n\t}')
        count += 1
    fd.write('\n]')
    fd.close