def get_correct_diapason(diapason: str):
    if len(diapason) == 4:
        return "0000" + diapason
    else:
        return "000" + diapason


diapasons = set()
with open("data/emojiroaddata.txt", "r", encoding='utf-8') as file:
    for line in file.readlines():
        diapasons.add(line.split(";")[0].rstrip())
    diapasons.remove('')

with open('data/correct_diapasons.txt', 'w', encoding='utf-8') as file:
    for diapason in diapasons:
        if diapason.find('..') == -1:
            file.write(get_correct_diapason(diapason) + "\n")
        else:
            temp_diapasons = diapason.split("..")
            file.write(get_correct_diapason(temp_diapasons[0]) + "-")
            file.write(get_correct_diapason(temp_diapasons[1]) + "\n")
