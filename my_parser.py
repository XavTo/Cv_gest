def recup_from_parser(str):
    i = 0
    recup = []
    while (str[i] != ':'):
        i += 1
    i += 3
    while (str[i] != '"'):
        if (str[i] == ','):
            break
        recup.append(str[i])
        i += 1
    ret = "".join(recup)
    return (ret)

def my_strncmp(str1, str2):
    count = 0
    if len(str1) < len(str2):
        return -1
    for exist in str2:
        if str1[count] != str2[count]:
            return 1
        count += 1
    return 0


def copy_str(str):
    i = 1
    new_str = ""
    while i < len(str):
        new_str += str[i]
        i = i + 1
    return new_str

def display_all_info(info):
    for element in info:
        print(element[0], element[1], element[2])

def my_void():
    stock = ["", "", ""]
    return stock

def my_parser(str):
    i = 0
    compt = -1
    info = []
    max = len(str)
    while i < max:
        if my_strncmp(str, "id") == 0:
            info.append(my_void())
            compt += 1
        if my_strncmp(str, "company") == 0:
            info[compt][0] = recup_from_parser(str)
        if my_strncmp(str, "date") == 0:
            info[compt][1] = recup_from_parser(str)
        if my_strncmp(str, "reply") == 0:
            info[compt][2] = recup_from_parser(str)
        i = i + 1
        str = copy_str(str)
    return info