def kiolvas():
    map = open("szintek.txt", "r", encoding="utf-8")
    szintek = map.readlines()


def parancsertelmezo(bemenet):
    parancs = bemenet.split()
    ige = parancs[0]
    fonev = parancs[1]
