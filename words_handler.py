import re


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F98D"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    return re.sub(emoji_pattern, "", string)


data = ""
with open("data/output_with_repost.txt", "r", encoding='utf-8') as file:
    for line in file.readlines():
        substr = re.sub("(http(s)?://(.)*(\.(\w)*)*)|(\u200d)|(\xa0)", '', line).rstrip().translate(
            str.maketrans('', '', r"""!"$%-&'()*+,.:;<=>?@[\]^_`{|}~«»—–•"""))
        substr = remove_emoji(substr)
        data += substr + " "

data = data.lower().split(" ")
data_set = set(data)

result_dict = {}

for word in data_set:
    result_dict[word] = data.count(word)

result_dict.pop('')

result_dict = {k: v for k, v in sorted(result_dict.items(), key=lambda item: item[1], reverse=True)}


with open('data/result.txt', 'w', encoding='utf-8') as file:
    i = 0
    for k, v in result_dict.items():
        if i == 100:
            break
        file.write(str(k) + ":" + str(v) + "\n")
        i += 1

# emoji_diapasons = list()


# def remove_emoji(stri: str):
#     for symb in stri:
#         print(symb)
#         if is_emoji(symb):
#             print("yes")
#             stri.replace(symb, "")
#
#
# def is_emoji(symb: str):
#     for rang in emoji_diapasons:
#         if ord(symb) == rang or (type(rang) == "range" and ord(symb) in rang):
#             return True
#     return False
#
#
# with open("correct_diapasons.txt", "r", encoding="utf-8") as file:
#     for line in file.readlines():
#         line = line.rstrip()
#         if len(line) == 8:
#             emoji_diapasons.append(int(line, 16))
#         else:
#             temp_diapasons = line.split("-")
#             emoji_diapasons.append(
#                 range(int(temp_diapasons[0], 16), int(temp_diapasons[1], 16))
#             )
