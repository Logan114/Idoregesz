import statusz

def kiolvas():
    map = open("szintek.txt", "r", encoding="utf-8")
    szintek = map.readlines()


def parancsertelmezo(bemenet):
    parancs = bemenet.split()
    ige = parancs[0]
    fonev = parancs[1]

def statuszjelenito(kimenet):
    if input == input("s"):
        print(f"HP: {statusz.HP}")
        print(f"Pénz: {statusz.penz}")
        if statusz.kulcs == False:
            print("Nincs kulcsod")
        else:
            print("Van kulcsod")