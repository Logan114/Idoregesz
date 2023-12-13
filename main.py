from statusz import *
import motor
hatizsak = []
global penz
penz = 0
lvl = 0
n = 0
kulcs:bool = False
HP:int = 10

motor.kiolvas(lvl)


while n <= 13:
    bemenet = input("Mit csinálsz?")
    motor.parancsertelmezo(bemenet)
    
