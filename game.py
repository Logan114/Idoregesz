
# encoding="utf-8"
# coding=utf-8
# -*- coding: utf-8 -*-



# szükséges: pip install opencv-python

import cv2 as cv
import time
#import motor


def Kepek(n):

	

	kepLista = ["0_kezdo.png", "1_kezdes.png", "2_mezo.png", "3_kut.png", "5_kastely.png", "6_szerzetes.png", "9_kamra.png", "10_faajto.png", "14_ajto.png"] 

	#utvonal = r'kepek\'' + kepLista[n].replace('',',')

	'''
	new_string = my_string.replace(' ', '_')
	print(new_string)
	'''

	for k in kepLista[:7]:
		if str(n) in k:
			print(f"k: {k}")
			kep = cv.imread(kepLista[n], cv.COLOR_BGR2GRAY)
			cv.imshow('KepSorszam: ',kep)
			cv.waitKey()
			print("Siker1")


	for j in kepLista[7:]:
		if str(n) in j:
			print(f"j: {j}")
			kep = cv.imread(kepLista[n], cv.COLOR_BGR2GRAY)
			cv.imshow('KepSorszam: ',kep)
			cv.waitKey()
			print("Siker2")





	#kep = cv.imread(kepLista[n], cv.COLOR_BGR2GRAY)
	#kep = cv.imread(utvonal, cv.COLOR_BGR2GRAY)
	#kep = cv.imread('00_kezdo.png', cv.COLOR_BGR2GRAY)

	#cv.imshow('KepSorszam: ',kep)
	#cv.waitKey()




	'''
	while not cv2.waitKey(1) & 0xFF == ord('enter'):
      cv2.imshow(...)

	'''



n = int(input("Szint? : "))
Kepek(n)





































