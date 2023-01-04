# part 1:
def func(file):
    dic = {}
    with open(file, "w+") as file:
        file.write("Puackich, hvhnkrally oaths phufhck. all ymr nhhd is Pykemn.\n")
        file.write("J.U.U.U Kmltin.\n")
        file.write("mmps iks nmk eio; ---> hkmu\n")
        file.seek(0)
        data = file.read()

    for letter in data:

        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
            count = dic.get(letter, 0)
            count += 1
            dic[letter] = count

    most_common = sorted(dic, key=dic.get, reverse=True)[:4]

    global dic_replace
    dic_replace = {most_common[0]: "e", most_common[1]: "t", most_common[2]: "o", most_common[3]: "r",
                   "e": most_common[0], "t": most_common[1], "o": most_common[2], "r": most_common[3]}

    print(dic)
    print(most_common)
    print(dic_replace)


func("file")

# part 2:
original_text = "Puackich, hvhnkrally oaths phufhck. all ymr nhhd is Pykemn.\
    \nJ.u.u.u kmltin.\nmmps iks nmk eio; ---> hkmu\n"


def replace(str_input):
    print("The original text", str_input)
    print("".join(dic_replace.get(char, char) for char in str_input))
    return "".join(dic_replace.get(char, char) for char in str_input)


replace(original_text)

# part 3:
file = open('file', 'a')


def add(text):
    file.write(" \n")
    file.write(" \n")
    file.write("The encryption for the above text is: \n")
    file.write(replace(original_text))

    with open("result.txt", "w+") as file_result:
        file_result.write(replace(original_text))


add(file)


# part 4:

import re


def long(txt):
    list_long = []
    with open("result.txt", "r") as f:
        txt = f.read().split()
        max_str = txt[0]
        for word in txt:
            word = re.sub(r'[^a-zA-Z0-9 ]+', '', word)
            if len(word) >= len(max_str):
                max_str = word
                max_str.strip(",.")
                list_long.append(max_str)

    return list_long


print(long("result.txt"))


def count(txt):
    with open("result.txt", "r") as f:
        len_result_file = len(f.readlines())
    return len_result_file


print("number of line in txt:", count("result.txt"))
