from functions import *
from settings import *
from run import *

def copyList(list):
    copy=[]
    for i in list:
        copy.append(i)
    return copy

def max_elem():
    file = open("scores.txt", "r+")
    lines = file.readlines()
    for line in lines:
        line = line.replace("\n", "")
        line = line.split()
    max = lines[0][0]
    for i in range(1,len(lines)):
        if lines[i][0] > max: max=lines[i][0];
    file.close()
    return max

def test_max_elem():
    lista = [1,2,5,7,4]
    assert max_elem(lista)==str(sorted(lista)[-1])


def test_bubble_sort_file():
    file = open("scores.txt", "r")
    lines = file.readlines()
    w = True
    for line in lines:
        line = line.split(" ")
        if not len(line) == 2 or len(line) ==0 :
            w = False
    assert w == True
    file.close()

def test_bubble_sort_file_2():
    bubble_sort_file()
    lista = lb_read(10)
    max = max_elem(lista)
    assert lista[0][0] == max



def test_lb_read():
    n = 10
    assert n == len(lb_read(n))

def test_2_lb_read():
    x = lb_read(5)
    assert str(type(x))== "<class 'list'>"


def test_rev_list():
    lista = [2,11,8,5,4,7,13,2]
    lista2 = copyList(lista)
    lista2.reverse()
    assert lista2 == rev_list(lista)

def test_CONST():
    assert str(type(FONT_SIZE)) == "<class 'int'>"
    assert str(type(SCREEN_SIZE)) == "<class 'tuple'>"
    assert str(type(FONT_SIZE))== "<class 'int'>"
    assert str(type(CAPTION)) == "<class 'str'>"
