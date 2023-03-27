import random
from settings import *

# Random positions
def random_pos(iw, ih):
    w = SCREEN_SIZE[0]
    h = SCREEN_SIZE[1]
    x = random.randint(10, w-(10+iw))
    y = random.randint(10, h-(10+ih))
    if ih == 0: output = (x,0)
    elif iw == 0: output = (0,y)
    else: output = (x,y)
    return output

def random_width(iw):
    w = SCREEN_SIZE[0]
    x = random.randint(10, w-(10+iw))
    return x
def random_height(ih):
    while True:
        h = SCREEN_SIZE[1]
        y = random.randint(10, h-(10+ih))
        return y

# Sorting
def rev_list(lista):
    res =[]
    l = len(lista)
    for i in range(l-1,-1,-1):
        res.append(lista[i])
    return res

def bubble_sort_file():
    file = open("scores.txt", "r")
    l = file.readlines()
    n = len(l)
    for i in range(n):
        l[i] = l[i].split()
    for i in range(n):
        l[i][1] = l[i][1].replace("\n", " ")
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if int(l[j][0]) > int(l[j+1][0]):
                l[j], l[j + 1] = l[j + 1], l[j]
    l = rev_list(l)
    file.close()
    file2 = open("scores.txt", "w")
    for elem in l:
        file2.write(f"{elem[0]} {elem[1]}\n")
    file2.close()
    print("Score saved")



# Leaderboard
def lb_add(name,score):
    file = open("scores.txt", "r+")
    lines = file.readlines()
    for line in lines:
        line= line.replace("\n", "")
    new_score = f"{name}     {score}"
    file.write(new_score)
    file.close()


def lb_read(lines):
    file = open("scores.txt", "r")
    l = file.readlines()
    res = []
    j = 0
    for i in range(lines):
        if j >= len(l): res.append("")
        else: res.append(l[j])
        j += 1
    file.close()
    return res
print(lb_read(5))



