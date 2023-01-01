# Question1:
id_Information = {("name", "last name"): 'raghda knaane', 'age:': 23, 'phone number:': '0522940944'}
print(id_Information)


# Question2:
def replace(lst):
    try:
        lst[5] = "@"
    except IndexError:
        print("relevant exception")
    finally:
        print(lst)


replace([1, 3, 5, 6, 9, 1, 4, 4])


# Question3:
def replace(lst):
    try:
        assert len(lst) >= 6, "relevant assertion"
        lst[5] = "@"
    except AssertionError as msg:
        print(msg)
    return lst


print(replace([1, 3, 5, 6, 9, 1, 4, 4]))


# Question 4:
def add(dic, key, value):
    dic[key] = value
    print(dic)


add({"name": "raghda", "age": 23}, "fav food", "pizza")


# Question 5:
n = int(input("please enter a number:",))
dic_new = {}
for x in range(1, n+1):
    dic_new[x] = x+3
print(dic_new)


# Question 6:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dic = {}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)
print(new_dic)


# Question 7:
str1 = "hanna"
dicn = {}


def func(str1):
    for char in str1:
        c = str1.count(char)
        dicn[char] = c
    return dicn


print(func(str1))

# Question 8:
d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
dic_new = d2
for i, j in d1.items():
    if i in d2:
        dic_new[i] = j + d2[i]
    else:
        dic_new[i] = j
print(dic_new)
