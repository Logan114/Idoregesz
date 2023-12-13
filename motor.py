from statusz import *

def kiolvas(n):
    map = open("szintek.txt", "r", encoding="utf-8")
    szintek = map.readlines()
    print(szintek[n])
    return n
    

def parancsertelmezo(bemenet):
    parancs = bemenet.split()
    ige = parancs[0]
    fonev = parancs[1]
    if ige == igek[0] and fonev == fonevek[0]:
        lvl:int = 1
        kiolvas(lvl)
    if ige == igek[0] and fonev == fonevek[1]:
        lvl:int = 2
        kiolvas(lvl)
    if ige == igek[2] and fonev == fonevek[3]:
        lvl:int = 3
        kiolvas(lvl)
    if ige == igek[0] and fonev == fonevek[0] or fonev == fonevek[2]:
        lvl:int = 4
        kiolvas(lvl)
    if ige == igek[0] and fonev == fonevek[4]:
        lvl:int = 5
        kiolvas(lvl)
    if ige == igek[1] and fonev == fonevek[3]:
        lvl:int = 6
        kiolvas(lvl)
    if ige == igek[2] and fonev == fonevek[7]:
        lvl:int = 7
        kiolvas(lvl)
    if ige == igek[0] and fonev == fonevek[5]:
        lvl:int = 8
        kiolvas(lvl)
    if ige == igek[0] and fonev == fonevek[8]:
        lvl:int = 9
        kiolvas(lvl)
    if ige == igek[3] and fonev == fonevek[7]:
        lvl:int = 10
        kiolvas(lvl)
    if ige == igek[4] and fonev == fonevek[9]:
        lvl:int = 11
        kiolvas(lvl)
    if ige == igek[0] and fonev == fonevek[6]:
        lvl:int = 12
        kiolvas(lvl)
    if ige == igek[2] and fonev == fonevek[7]:
        lvl:int = 13
        kiolvas(lvl)
    if ige not in igek and fonev not in fonevek:
        print("hibas parancs")

    
""" 0 = megy
1 = ad
2 = felvesz
3 = hasznal
4 = eszik
5 = vizsgal

0"epulet"
1"kut"
2"kastely"
3 "penz"
4 "vartemplom"
5 "kamra"
6 "ajto"
7 "kulcs"
8 "faajto"
9 "etel
10 "nyugat"
"""
"""
while True:
    try:
        bemenet = input("Mit csinálsz? ")
    except ValueError:
        print ("Hibás parancs")
        continue
    if bemenet not in igek or fonevek:
        break
"""
bemenet = input("Mit csinálsz? ")
parancsertelmezo(bemenet)

